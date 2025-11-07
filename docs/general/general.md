# General

General endpoints for basic PMS operation not specific to any media provider

**Category:** General

---

### GET /

**Operation ID:** `getSlash`

**Summary:** Get PMS info

Information about this PMS setup and configuration

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /identity

**Operation ID:** `getIdentity`

**Summary:** Get PMS identity

Get details about this PMS's identity

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /security/resources

**Operation ID:** `securityGetResources`

**Summary:** Get Source Connection Information

If a caller requires connection details and a transient token for a source that is known to the server, for example a cloud media provider or shared PMS, then this endpoint can be called. This endpoint is only accessible with either an admin token or a valid transient token generated from an admin token.

#### Parameters

- **`source`** (query) **(required)** - string
  The source identifier with an included prefix.
- **`refresh`** (query) - integer
  Force refresh

#### Responses

**200** - OK

Content-Type: `application/json`

**400** - A query param is missing or the wrong value

Content-Type: `text/html`

**403** - Invalid or no token provided or a transient token could not be created

Content-Type: `text/html`

---

### POST /security/token

**Operation ID:** `securityPostToken`

**Summary:** Get Transient Tokens

This endpoint provides the caller with a temporary token with the same access level as the caller's token. These tokens are valid for up to 48 hours and are destroyed if the server instance is restarted.
Note: This endpoint responds to all HTTP verbs but POST in preferred

#### Parameters

- **`type`** (query) **(required)** - string
  The value `delegation` is the only supported `type` parameter.
- **`scope`** (query) **(required)** - string
  The value `all` is the only supported `scope` parameter.

#### Responses

**200** - OK

Content-Type: `application/json`

**400** - A query param is missing or the wrong value

Content-Type: `text/html`

**403** - Invalid or no token provided or a transient token could not be created

Content-Type: `text/html`

---

