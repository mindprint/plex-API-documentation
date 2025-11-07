#!/usr/bin/env python3
"""
Generate LLM-friendly markdown documentation from Plex API OpenAPI spec.
Each file is kept under 256KB for optimal LLM consumption.
"""
import json
import os
import re
from pathlib import Path
from typing import Dict, List, Any
from collections import defaultdict


def slugify(text: str) -> str:
    """Convert text to URL-friendly slug."""
    return re.sub(r'[^\w\s-]', '', text.lower()).replace(' ', '-')


def estimate_size(content: str) -> int:
    """Estimate size in bytes."""
    return len(content.encode('utf-8'))


def format_parameter(param: Dict[str, Any]) -> str:
    """Format a parameter for markdown display."""
    name = param.get('name', '')
    param_in = param.get('in', '')
    required = ' **(required)**' if param.get('required', False) else ''
    param_type = param.get('schema', {}).get('type', 'string')
    description = param.get('description', '')

    return f"- **`{name}`** ({param_in}){required} - {param_type}\n  {description}\n"


def format_response(status_code: str, response: Dict[str, Any]) -> str:
    """Format a response for markdown display."""
    description = response.get('description', '')
    content_type = list(response.get('content', {}).keys())[0] if response.get('content') else 'N/A'

    md = f"**{status_code}** - {description}\n\n"
    if response.get('content'):
        md += f"Content-Type: `{content_type}`\n\n"
    return md


def format_endpoint(path: str, method: str, details: Dict[str, Any]) -> str:
    """Format a single endpoint as markdown."""
    operation_id = details.get('operationId', 'unknown')
    summary = details.get('summary', '')
    description = details.get('description', '')
    deprecated = details.get('deprecated', False)

    md = f"### {method.upper()} {path}\n\n"

    if deprecated:
        md += "> ⚠️ **DEPRECATED**\n\n"

    md += f"**Operation ID:** `{operation_id}`\n\n"

    if summary:
        md += f"**Summary:** {summary}\n\n"

    if description:
        md += f"{description}\n\n"

    # Parameters
    parameters = details.get('parameters', [])
    if parameters:
        md += "#### Parameters\n\n"
        for param in parameters:
            md += format_parameter(param)
        md += "\n"

    # Request body
    request_body = details.get('requestBody')
    if request_body:
        md += "#### Request Body\n\n"
        md += f"{request_body.get('description', '')}\n\n"
        if request_body.get('required'):
            md += "**(required)**\n\n"

        content = request_body.get('content', {})
        for content_type, schema_info in content.items():
            md += f"Content-Type: `{content_type}`\n\n"

    # Responses
    responses = details.get('responses', {})
    if responses:
        md += "#### Responses\n\n"
        for status_code, response in responses.items():
            md += format_response(status_code, response)

    md += "---\n\n"
    return md


def format_schema(schema_name: str, schema: Dict[str, Any]) -> str:
    """Format a schema definition as markdown."""
    md = f"## {schema_name}\n\n"

    description = schema.get('description', '')
    if description:
        md += f"{description}\n\n"

    schema_type = schema.get('type', 'object')
    md += f"**Type:** `{schema_type}`\n\n"

    # Properties
    properties = schema.get('properties', {})
    if properties:
        md += "### Properties\n\n"
        for prop_name, prop_details in properties.items():
            prop_type = prop_details.get('type', 'any')
            prop_desc = prop_details.get('description', '')
            required = ' **(required)**' if prop_name in schema.get('required', []) else ''

            md += f"- **`{prop_name}`**{required} - `{prop_type}`\n"
            if prop_desc:
                md += f"  {prop_desc}\n"
            md += "\n"

    # AllOf, AnyOf, OneOf
    if 'allOf' in schema:
        md += "### Composed of (allOf)\n\n"
        for item in schema['allOf']:
            if '$ref' in item:
                ref = item['$ref'].split('/')[-1]
                md += f"- [{ref}](#{slugify(ref)})\n"

    md += "---\n\n"
    return md


def generate_documentation(api_spec: Dict[str, Any], output_dir: Path):
    """Generate the complete documentation structure."""

    # Create output directory structure
    docs_dir = output_dir / 'docs'
    docs_dir.mkdir(exist_ok=True)

    (docs_dir / 'getting-started').mkdir(exist_ok=True)
    (docs_dir / 'general').mkdir(exist_ok=True)
    (docs_dir / 'media-provider').mkdir(exist_ok=True)
    (docs_dir / 'dvr').mkdir(exist_ok=True)
    (docs_dir / 'schemas').mkdir(exist_ok=True)

    # Tag to category mapping
    tag_to_category = {
        'General': 'general',
        'Library': 'general',
        'Library Playlists': 'general',
        'Library Collections': 'general',
        'Status': 'general',
        'Activities': 'general',
        'Updater': 'general',
        'Butler': 'general',
        'Events': 'general',
        'Log': 'general',
        'Preferences': 'general',
        'Download Queue': 'general',
        'UltraBlur': 'general',
        'Transcoder': 'general',
        'Provider': 'media-provider',
        'Content': 'media-provider',
        'Hubs': 'media-provider',
        'Search': 'media-provider',
        'Rate': 'media-provider',
        'Playlist': 'media-provider',
        'Play Queue': 'media-provider',
        'Timeline': 'media-provider',
        'DVRs': 'dvr',
        'Devices': 'dvr',
        'EPG': 'dvr',
        'Subscriptions': 'dvr',
        'Live TV': 'dvr',
    }

    # Group endpoints by tag
    endpoints_by_tag = defaultdict(list)

    for path, methods in api_spec.get('paths', {}).items():
        for method, details in methods.items():
            if method in ['get', 'post', 'put', 'delete', 'patch']:
                tags = details.get('tags', ['General'])
                for tag in tags:
                    endpoints_by_tag[tag].append({
                        'path': path,
                        'method': method,
                        'details': details
                    })

    # Generate files for each tag
    for tag, endpoints in endpoints_by_tag.items():
        category = tag_to_category.get(tag, 'general')
        tag_slug = slugify(tag)

        # Get tag description
        tag_info = next((t for t in api_spec.get('tags', []) if t['name'] == tag), {})
        tag_description = tag_info.get('description', '')

        # Build content
        content = f"# {tag}\n\n"
        content += f"{tag_description}\n\n"
        content += f"**Category:** {category.replace('-', ' ').title()}\n\n"
        content += "---\n\n"

        # Add endpoints
        for endpoint in endpoints:
            endpoint_md = format_endpoint(
                endpoint['path'],
                endpoint['method'],
                endpoint['details']
            )
            content += endpoint_md

        # Check size and write
        size = estimate_size(content)
        file_path = docs_dir / category / f"{tag_slug}.md"

        if size > 250_000:  # 250KB buffer
            print(f"Warning: {tag} file is {size} bytes, splitting...")
            # Split into multiple files if needed
            parts = []
            current_part = f"# {tag} (Part {{part}})\n\n{tag_description}\n\n---\n\n"

            for endpoint in endpoints:
                endpoint_md = format_endpoint(
                    endpoint['path'],
                    endpoint['method'],
                    endpoint['details']
                )

                if estimate_size(current_part + endpoint_md) > 250_000:
                    parts.append(current_part)
                    current_part = f"# {tag} (Part {{part}})\n\n{tag_description}\n\n---\n\n"

                current_part += endpoint_md

            parts.append(current_part)

            # Write parts
            for i, part_content in enumerate(parts, 1):
                part_content = part_content.replace('{part}', str(i))
                part_file = docs_dir / category / f"{tag_slug}-part-{i}.md"
                with open(part_file, 'w', encoding='utf-8') as f:
                    f.write(part_content)
                print(f"Generated: {part_file} ({estimate_size(part_content)} bytes)")
        else:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Generated: {file_path} ({size} bytes)")

    # Generate schemas documentation
    schemas = api_spec.get('components', {}).get('schemas', {})

    # Split schemas into reasonable chunks
    schema_chunks = []
    current_chunk = "# API Schemas\n\n"
    current_chunk += "This document contains the data model schemas used throughout the Plex API.\n\n"
    current_chunk += "---\n\n"

    for schema_name, schema in schemas.items():
        schema_md = format_schema(schema_name, schema)

        if estimate_size(current_chunk + schema_md) > 250_000:
            schema_chunks.append(current_chunk)
            current_chunk = "# API Schemas (Continued)\n\n---\n\n"

        current_chunk += schema_md

    schema_chunks.append(current_chunk)

    # Write schema files
    if len(schema_chunks) == 1:
        schema_file = docs_dir / 'schemas' / 'index.md'
        with open(schema_file, 'w', encoding='utf-8') as f:
            f.write(schema_chunks[0])
        print(f"Generated: {schema_file} ({estimate_size(schema_chunks[0])} bytes)")
    else:
        for i, chunk in enumerate(schema_chunks, 1):
            schema_file = docs_dir / 'schemas' / f'schemas-part-{i}.md'
            with open(schema_file, 'w', encoding='utf-8') as f:
                f.write(chunk)
            print(f"Generated: {schema_file} ({estimate_size(chunk)} bytes)")

    # Generate getting started documentation
    info = api_spec.get('info', {})
    description = info.get('description', '')

    getting_started = f"# Getting Started with Plex API {info.get('version', '')}\n\n"
    getting_started += description

    gs_file = docs_dir / 'getting-started' / 'index.md'
    with open(gs_file, 'w', encoding='utf-8') as f:
        f.write(getting_started)
    print(f"Generated: {gs_file} ({estimate_size(getting_started)} bytes)")

    # Generate main README
    generate_main_readme(api_spec, docs_dir, endpoints_by_tag)


def generate_main_readme(api_spec: Dict[str, Any], docs_dir: Path, endpoints_by_tag: Dict):
    """Generate the main README with navigation."""

    info = api_spec.get('info', {})

    readme = f"""# Plex Media Server API {info.get('version', '')} Documentation

Welcome to the LLM-friendly documentation for the Plex Media Server API.

## Overview

- **Version:** {info.get('version', '')}
- **License:** {info.get('license', {}).get('name', 'N/A')}
- **Total Endpoints:** {sum(len(endpoints) for endpoints in endpoints_by_tag.values())}
- **Base URL:** `https://{{IP}}.{{identifier}}.plex.direct:{{port}}`

## Documentation Structure

This documentation is organized into logical sections to make it easy to find what you need.
Each file is kept under 256KB for optimal consumption by Large Language Models.

### 📚 Getting Started

Start here if you're new to the Plex API:

- [Getting Started Guide](./getting-started/index.md) - API basics, authentication, headers, and concepts

### 🔧 General Endpoints

Core Plex Media Server functionality:

"""

    # Add general endpoints
    general_tags = [
        'General', 'Library', 'Library Playlists', 'Library Collections',
        'Status', 'Activities', 'Updater', 'Butler', 'Events', 'Log',
        'Preferences', 'Download Queue', 'UltraBlur', 'Transcoder'
    ]

    for tag in general_tags:
        if tag in endpoints_by_tag:
            tag_slug = slugify(tag)
            count = len(endpoints_by_tag[tag])

            # Check if split into parts
            parts = list((docs_dir / 'general').glob(f"{tag_slug}-part-*.md"))
            if parts:
                readme += f"- **{tag}** ({count} endpoints)\n"
                for i, _ in enumerate(sorted(parts), 1):
                    readme += f"  - [Part {i}](./general/{tag_slug}-part-{i}.md)\n"
            else:
                readme += f"- [{tag}](./general/{tag_slug}.md) ({count} endpoints)\n"

    readme += "\n### 📺 Media Provider Endpoints\n\n"
    readme += "Core media catalog and playback features:\n\n"

    media_tags = [
        'Provider', 'Content', 'Hubs', 'Search', 'Rate',
        'Playlist', 'Play Queue', 'Timeline'
    ]

    for tag in media_tags:
        if tag in endpoints_by_tag:
            tag_slug = slugify(tag)
            count = len(endpoints_by_tag[tag])
            readme += f"- [{tag}](./media-provider/{tag_slug}.md) ({count} endpoints)\n"

    readme += "\n### 📡 DVR & Live TV Endpoints\n\n"
    readme += "Digital Video Recording and Live TV features:\n\n"

    dvr_tags = ['DVRs', 'Devices', 'EPG', 'Subscriptions', 'Live TV']

    for tag in dvr_tags:
        if tag in endpoints_by_tag:
            tag_slug = slugify(tag)
            count = len(endpoints_by_tag[tag])
            readme += f"- [{tag}](./dvr/{tag_slug}.md) ({count} endpoints)\n"

    readme += "\n### 📋 Data Schemas\n\n"
    readme += "API data models and object schemas:\n\n"

    schema_files = sorted((docs_dir / 'schemas').glob('*.md'))
    if len(schema_files) == 1:
        readme += f"- [API Schemas](./schemas/index.md)\n"
    else:
        readme += f"- **API Schemas** (split into {len(schema_files)} parts)\n"
        for i, _ in enumerate(schema_files, 1):
            readme += f"  - [Part {i}](./schemas/schemas-part-{i}.md)\n"

    readme += """
## Quick Reference

### Authentication

The Plex API supports two authentication methods:

1. **JWT Authentication (Recommended)** - Short-lived tokens with enhanced security
2. **Traditional Token Authentication** - Legacy auth tokens from plex.tv

See the [Getting Started Guide](./getting-started/index.md) for detailed authentication instructions.

### Common Headers

All requests should include these headers:

```
X-Plex-Client-Identifier: <unique-client-id>
X-Plex-Token: <auth-token>
X-Plex-Product: <your-app-name>
Accept: application/json
```

### Response Formats

The API supports both XML and JSON. Use `Accept: application/json` for JSON responses (recommended).

## Key Concepts

- **Media Providers** - Starting points for accessing media libraries
- **Keys** - Path references that can be fetched (similar to URLs)
- **Types** - Metadata type identifiers (movie=1, show=2, episode=4, etc.)
- **Pagination** - Use `X-Plex-Container-Start` and `X-Plex-Container-Size` headers
- **Media Queries** - Advanced filtering and sorting language

## Resources

- [Plex API Forums](https://forums.plex.tv/c/api-discussions/)
- [Plex Support](https://support.plex.tv/)

---

**Generated from Plex API OpenAPI Specification v{info.get('version', '')}**

*This documentation is optimized for consumption by Large Language Models with each file under 256KB.*
"""

    readme_file = docs_dir / 'README.md'
    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write(readme)
    print(f"Generated: {readme_file} ({estimate_size(readme)} bytes)")


def main():
    """Main entry point."""
    script_dir = Path(__file__).parent
    json_file = script_dir / 'docs' / 'plex-API-docs.json'

    print(f"Loading API specification from {json_file}...")
    with open(json_file, 'r', encoding='utf-8') as f:
        api_spec = json.load(f)

    print(f"Generating documentation...")
    generate_documentation(api_spec, script_dir)

    print("\n✅ Documentation generation complete!")
    print(f"📁 Output directory: {script_dir / 'docs'}")


if __name__ == '__main__':
    main()
