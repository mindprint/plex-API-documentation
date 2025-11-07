# Provider

Media providers are the starting points for the entire Plex Media Server media library API.  It defines the paths for the groups of endpoints.  The `/media/providers` should be the only hard-coded path in clients when accessing the media library.  Non-media library endpoints are outside the scope of the media provider.  See the description in See [the section in API Info](#section/API-Info/Media-Providers) for more information on how to use media providers.

**Category:** Media Provider

---

### GET /media/providers

**Operation ID:** `getMediaProviders`

**Summary:** Get the list of available media providers

Get the list of all available media providers for this PMS.  This will generally include the library provider and possibly EPG if DVR is set up.

#### Responses

**200** - OK

Content-Type: `application/json`

---

### POST /media/providers

**Operation ID:** `postMediaProviders`

**Summary:** Add a media provider

This endpoint registers a media provider with the server. Once registered, the media server acts as a reverse proxy to the provider, allowing both local and remote providers to work.

#### Parameters

- **`url`** (query) **(required)** - string
  The URL of the media provider to add.

#### Responses

**200** - 

**400** - 

---

### POST /media/providers/refresh

**Operation ID:** `postMediaProvidersRefresh`

**Summary:** Refresh media providers

Refresh all known media providers. This is useful in case a provider has updated features.

#### Responses

**200** - 

---

### DELETE /media/providers/{provider}

**Operation ID:** `deleteMediaProvider`

**Summary:** Delete a media provider

Deletes a media provider with the given id

#### Parameters

- **`provider`** (path) **(required)** - string
  The ID of the media provider to delete

#### Responses

**200** - 

**400** - 

**403** - Cannot delete a provider which is a child of another provider

Content-Type: `text/html`

---

