# Plex Media Server API 1.1.1
 Documentation

Welcome to the LLM-friendly documentation for the Plex Media Server API.

## Overview

- **Version:** 1.1.1

- **License:** Apache 2.0
- **Total Endpoints:** 237
- **Base URL:** `https://{IP}.{identifier}.plex.direct:{port}`

## Documentation Structure

This documentation is organized into logical sections to make it easy to find what you need.
Each file is kept under 256KB for optimal consumption by Large Language Models.

### 📚 Getting Started

Start here if you're new to the Plex API:

- [Getting Started Guide](./getting-started/index.md) - API basics, authentication, headers, and concepts

### 🔧 General Endpoints

Core Plex Media Server functionality:

- [General](./general/general.md) (4 endpoints)
- [Library](./general/library.md) (79 endpoints)
- [Library Playlists](./general/library-playlists.md) (13 endpoints)
- [Library Collections](./general/library-collections.md) (3 endpoints)
- [Status](./general/status.md) (6 endpoints)
- [Activities](./general/activities.md) (2 endpoints)
- [Updater](./general/updater.md) (3 endpoints)
- [Butler](./general/butler.md) (5 endpoints)
- [Events](./general/events.md) (2 endpoints)
- [Log](./general/log.md) (3 endpoints)
- [Preferences](./general/preferences.md) (3 endpoints)
- [Download Queue](./general/download-queue.md) (9 endpoints)
- [UltraBlur](./general/ultrablur.md) (2 endpoints)
- [Transcoder](./general/transcoder.md) (5 endpoints)

### 📺 Media Provider Endpoints

Core media catalog and playback features:

- [Provider](./media-provider/provider.md) (4 endpoints)
- [Content](./media-provider/content.md) (13 endpoints)
- [Hubs](./media-provider/hubs.md) (14 endpoints)
- [Search](./media-provider/search.md) (2 endpoints)
- [Rate](./media-provider/rate.md) (1 endpoints)
- [Playlist](./media-provider/playlist.md) (3 endpoints)
- [Play Queue](./media-provider/play-queue.md) (9 endpoints)
- [Timeline](./media-provider/timeline.md) (3 endpoints)

### 📡 DVR & Live TV Endpoints

Digital Video Recording and Live TV features:

- [DVRs](./dvr/dvrs.md) (12 endpoints)
- [Devices](./dvr/devices.md) (13 endpoints)
- [EPG](./dvr/epg.md) (9 endpoints)
- [Subscriptions](./dvr/subscriptions.md) (10 endpoints)
- [Live TV](./dvr/live-tv.md) (4 endpoints)

### 📋 Data Schemas

API data models and object schemas:

- [API Schemas](./schemas/index.md)

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
