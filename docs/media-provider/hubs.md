# Hubs

The hubs within a media provider

**Category:** Media Provider

---

### GET /hubs

**Operation ID:** `hubsGetSlash`

**Summary:** Get global hubs

Get the global hubs in this PMS

#### Parameters

- **`count`** (query) - integer
  Limit hub entries to count items
- **`onlyTransient`** (query) - integer
  Only return hubs which are "transient", meaning those which are prone to changing after media playback or addition (e.g. On Deck, or Recently Added)
- **`identifier`** (query) - array
  If provided, limit to only specified hubs

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /hubs/items

**Operation ID:** `hubsGetItems`

**Summary:** Get a hub's items

Get the items within a single hub specified by identifier

#### Parameters

- **`count`** (query) - integer
  Limit hub entry to count items
- **`identifier`** (query) **(required)** - array
  If provided, limit to only specified hubs

#### Responses

**200** - OK

Content-Type: `application/json`

**404** - The specified hub could not be found

Content-Type: `text/html`

---

### GET /hubs/continueWatching

**Operation ID:** `hubsGetContinueWatching`

**Summary:** Get the continue watching hub

Get the global continue watching hub

#### Parameters

- **`count`** (query) - integer
  Limit hub entry to count items

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /hubs/promoted

**Operation ID:** `hubsGetPromoted`

**Summary:** Get the hubs which are promoted

Get the global hubs which are promoted (should be displayed on the home screen)

#### Parameters

- **`count`** (query) - integer
  Limit hub entry to count items

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /hubs/metadata/{metadataId}

**Operation ID:** `hubsGetMetadataMetadata`

**Summary:** Get hubs for a section by metadata item

Get the hubs for a section by metadata item.  Currently only for music sections

#### Parameters

- **`metadataId`** (path) **(required)** - integer
  The metadata ID for the hubs to fetch
- **`count`** (query) - integer
  Limit hub entries to count items
- **`onlyTransient`** (query) - integer
  Only return hubs which are "transient", meaning those which are prone to changing after media playback or addition (e.g. On Deck, or Recently Added)

#### Responses

**200** - 

**400** - No metadata with that id or permission is denied

Content-Type: `text/html`

---

### GET /hubs/metadata/{metadataId}/related

**Operation ID:** `hubsGetMetadataMetadataRelated`

**Summary:** Get related hubs

Get the hubs for a metadata related to the provided metadata item

#### Parameters

- **`metadataId`** (path) **(required)** - integer
  The metadata ID for the hubs to fetch
- **`count`** (query) - integer
  Limit hub entries to count items
- **`onlyTransient`** (query) - integer
  Only return hubs which are "transient", meaning those which are prone to changing after media playback or addition (e.g. On Deck, or Recently Added)

#### Responses

**200** - 

**400** - No metadata with that id or permission is denied

Content-Type: `text/html`

---

### GET /hubs/metadata/{metadataId}/postplay

**Operation ID:** `hubsGetMetadataMetadataPostplay`

**Summary:** Get postplay hubs

Get the hubs for a metadata to be displayed in post play

#### Parameters

- **`metadataId`** (path) **(required)** - integer
  The metadata ID for the hubs to fetch
- **`count`** (query) - integer
  Limit hub entries to count items
- **`onlyTransient`** (query) - integer
  Only return hubs which are "transient", meaning those which are prone to changing after media playback or addition (e.g. On Deck, or Recently Added)

#### Responses

**200** - 

**400** - No metadata with that id or permission is denied

Content-Type: `text/html`

---

### GET /hubs/sections/{sectionId}

**Operation ID:** `hubsGetSection`

**Summary:** Get section hubs

Get the hubs for a single section

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  The section ID for the hubs to fetch
- **`count`** (query) - integer
  Limit hub entries to count items
- **`onlyTransient`** (query) - integer
  Only return hubs which are "transient", meaning those which are prone to changing after media playback or addition (e.g. On Deck, or Recently Added)

#### Responses

**200** - OK

Content-Type: `application/json`

**400** - No section with that id or permission is denied

Content-Type: `text/html`

---

### GET /hubs/sections/{sectionId}/manage

**Operation ID:** `hubsSectionsSectionManageGetSlash`

**Summary:** Get hubs

Get the list of hubs including both built-in and custom

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  The section ID for the hubs to reorder
- **`metadataItemId`** (query) - integer
  Restrict hubs to ones relevant to the provided metadata item

#### Responses

**200** - OK

Content-Type: `application/json`

**403** - 

**404** - Section id was not found

Content-Type: `text/html`

---

### DELETE /hubs/sections/{sectionId}/manage

**Operation ID:** `hubsSectionsSectionManageDeleteSlash`

**Summary:** Reset hubs to defaults

Reset hubs for this section to defaults and delete custom hubs

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  The section ID for the hubs to reorder

#### Responses

**200** - 

**403** - 

**404** - Section id was not found

Content-Type: `text/html`

---

### POST /hubs/sections/{sectionId}/manage

**Operation ID:** `hubsSectionsSectionManagePostSlash`

**Summary:** Create a custom hub

Create a custom hub based on a metadata item

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  The section ID for the hubs to reorder
- **`metadataItemId`** (query) **(required)** - integer
  The metadata item on which to base this hub.  This must currently be a collection
- **`promotedToRecommended`** (query) - integer
  Whether this hub should be displayed in recommended
- **`promotedToOwnHome`** (query) - integer
  Whether this hub should be displayed in admin's home
- **`promotedToSharedHome`** (query) - integer
  Whether this hub should be displayed in shared user's home

#### Responses

**200** - 

**400** - A hub could not be created with this metadata item

Content-Type: `text/html`

**403** - 

**404** - Section id or metadata item was not found

Content-Type: `text/html`

---

### PUT /hubs/sections/{sectionId}/manage/move

**Operation ID:** `hubsSectionsSectionManagePutMove`

**Summary:** Move Hub

Changed the ordering of a hub among others hubs

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  The section ID for the hubs to reorder
- **`identifier`** (query) **(required)** - string
  The identifier of the hub to move
- **`after`** (query) - string
  The identifier of the hub to order this hub after (or empty/missing to put this hub first)

#### Responses

**200** - 

**403** - 

**404** - Section id was not found

Content-Type: `text/html`

---

### PUT /hubs/sections/{sectionId}/manage/{identifier}

**Operation ID:** `hubsSectionsSectionManagePutIdentifier`

**Summary:** Change hub visibility

Changed the visibility of a hub for both the admin and shared users

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  The section ID for the hubs to change
- **`identifier`** (path) **(required)** - string
  The identifier of the hub to change
- **`promotedToRecommended`** (query) - integer
  Whether this hub should be displayed in recommended
- **`promotedToOwnHome`** (query) - integer
  Whether this hub should be displayed in admin's home
- **`promotedToSharedHome`** (query) - integer
  Whether this hub should be displayed in shared user's home

#### Responses

**200** - 

**403** - 

**404** - Section id was not found

Content-Type: `text/html`

---

### DELETE /hubs/sections/{sectionId}/manage/{identifier}

**Operation ID:** `hubsSectionsSectionManageDeleteIdentifier`

**Summary:** Delete a custom hub

Delete a custom hub from the server

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  The section ID for the hubs to change
- **`identifier`** (path) **(required)** - string
  The identifier of the hub to change

#### Responses

**200** - 

**400** - The hub is not a custom hub

Content-Type: `text/html`

**403** - 

**404** - The section or hub was not found

Content-Type: `text/html`

---

