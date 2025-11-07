# Updater

This describes the API for searching and applying updates to the Plex Media Server.
Updates to the status can be observed via the Event API.


**Category:** General

---

### GET /updater/status

**Operation ID:** `updaterGetStatus`

**Summary:** Querying status of updates

Get the status of updating the server

#### Responses

**200** - OK

Content-Type: `application/json`

---

### PUT /updater/check

**Operation ID:** `updaterPutCheck`

**Summary:** Checking for updates

Perform an update check and potentially download

#### Parameters

- **`download`** (query) - integer
  Indicate that you want to start download any updates found.

#### Responses

**200** - 

---

### PUT /updater/apply

**Operation ID:** `updaterPutApply`

**Summary:** Applying updates

Apply any downloaded updates.  Note that the two parameters `tonight` and `skip` are effectively mutually exclusive. The `tonight` parameter takes precedence and `skip` will be ignored if `tonight` is also passed.

#### Parameters

- **`tonight`** (query) - integer
  Indicate that you want the update to run during the next Butler execution. Omitting this or setting it to false indicates that the update should install immediately.
- **`skip`** (query) - integer
  Indicate that the latest version should be marked as skipped. The <Release> entry for this version will have the `state` set to `skipped`.

#### Responses

**200** - The update process started correctly

Content-Type: `text/html`

**400** - This system cannot install updates

Content-Type: `text/html`

**500** - The update process failed to start

Content-Type: `text/html`

---

