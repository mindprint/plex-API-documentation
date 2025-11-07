# Library Playlists

Endpoints for manipulating playlists.

**Category:** General

---

### POST /playlists

**Operation ID:** `playlistPostSlash`

**Summary:** Create a Playlist

Create a new playlist. By default the playlist is blank.

#### Parameters

- **`uri`** (query) - string
  The content URI for what we're playing (e.g. `library://...`).
- **`playQueueID`** (query) - integer
  To create a playlist from an existing play queue.

#### Responses

**200** - OK

Content-Type: `application/json`

**400** - 

---

### DELETE /playlists/{playlistId}

**Operation ID:** `playlistDeletePlaylist`

**Summary:** Delete a Playlist

Deletes a playlist by provided id

#### Parameters

- **`playlistId`** (path) **(required)** - integer
  The ID of the playlist

#### Responses

**204** - 

**404** - Playlist not found (or user may not have permission to access playlist)

Content-Type: `text/html`

---

### PUT /playlists/{playlistId}

**Operation ID:** `playlistPutPlaylist`

**Summary:** Editing a Playlist

Edits a playlist in the same manner as [editing metadata](#tag/Provider/operation/metadataPutItem)

#### Parameters

- **`playlistId`** (path) **(required)** - integer
  The ID of the playlist

#### Responses

**204** - 

**404** - Playlist not found (or user may not have permission to access playlist)

Content-Type: `text/html`

---

### DELETE /playlists/{playlistId}/items

**Operation ID:** `playlistDeleteItems`

**Summary:** Clearing a playlist

Clears a playlist, only works with dumb playlists. Returns the playlist.

#### Parameters

- **`playlistId`** (path) **(required)** - integer
  The ID of the playlist

#### Responses

**200** - 

**400** - 

**404** - Playlist not found (or user may not have permission to access playlist)

Content-Type: `text/html`

---

### PUT /playlists/{playlistId}/items

**Operation ID:** `playlistPutItems`

**Summary:** Adding to  a Playlist

Adds a generator to a playlist, same parameters as the POST above. With a dumb playlist, this adds the specified items to the playlist. With a smart playlist, passing a new `uri` parameter replaces the rules for the playlist. Returns the playlist.

#### Parameters

- **`playlistId`** (path) **(required)** - integer
  The ID of the playlist
- **`uri`** (query) - string
  The content URI for the playlist.
- **`playQueueID`** (query) - integer
  The play queue to add to a playlist.

#### Responses

**200** - 

**400** - 

**404** - Playlist not found (or user may not have permission to access playlist)

Content-Type: `text/html`

---

### GET /playlists/{playlistId}/items/{generatorId}

**Operation ID:** `playlistGetItemsGenerator`

**Summary:** Get a playlist generator

Get a playlist's generator.  Only used for optimized versions

#### Parameters

- **`playlistId`** (path) **(required)** - integer
  The ID of the playlist
- **`generatorId`** (path) **(required)** - integer
  The generator item ID to delete.

#### Responses

**200** - OK

Content-Type: `application/json`

**400** - 

**404** - Playlist not found (or user may not have permission to access playlist) or generator not found

Content-Type: `text/html`

---

### DELETE /playlists/{playlistId}/items/{generatorId}

**Operation ID:** `playlistDeleteItemsGenerator`

**Summary:** Delete a Generator

Deletes an item from a playlist. Only works with dumb playlists.

#### Parameters

- **`playlistId`** (path) **(required)** - integer
  The ID of the playlist
- **`generatorId`** (path) **(required)** - integer
  The generator item ID to delete.

#### Responses

**200** - 

**400** - 

**404** - Playlist not found (or user may not have permission to access playlist) or generator not found

Content-Type: `text/html`

---

### PUT /playlists/{playlistId}/items/{generatorId}

**Operation ID:** `playlistPutItemsGenerator`

**Summary:** Modify a Generator

Modify a playlist generator.  Only used for optimizer

#### Parameters

- **`playlistId`** (path) **(required)** - integer
  The ID of the playlist
- **`generatorId`** (path) **(required)** - integer
  The generator item ID to modify.
- **`Item`** (query) - object
  Note: OpenAPI cannot properly render this query parameter example ([See GHI](https://github.com/OAI/OpenAPI-Specification/issues/1706)).  It should be rendered as:

Item[type]=42&Item[title]=Jack-Jack Attack&Item[target]=&Item[targetTagID]=1&Item[locationID]=-1&Item[Location][uri]=library://82503060-0d68-4603-b594-8b071d54819e/item//library/metadata/146&Item[Policy][scope]=all&Item[Policy][value]=&Item[Policy][unwatched]=0


#### Responses

**200** - 

**400** - 

**404** - Playlist not found (or user may not have permission to access playlist) or generator not found

Content-Type: `text/html`

---

### GET /playlists/{playlistId}/items/{generatorId}/items

**Operation ID:** `playlistGetItemsGeneratorItems`

**Summary:** Get a playlist generator's items

Get a playlist generator's items

#### Parameters

- **`playlistId`** (path) **(required)** - integer
  The ID of the playlist
- **`generatorId`** (path) **(required)** - integer
  The generator item ID to delete.

#### Responses

**200** - OK

Content-Type: `application/json`

**400** - 

**404** - Playlist not found (or user may not have permission to access playlist) or generator not found

Content-Type: `text/html`

---

### PUT /playlists/{playlistId}/items/{generatorId}/{metadataId}/{action}

**Operation ID:** `playlistPutItemsGeneratorReprocess`

**Summary:** Reprocess a generator

Make a generator reprocess (refresh)

#### Parameters

- **`playlistId`** (path) **(required)** - integer
  The ID of the playlist
- **`generatorId`** (path) **(required)** - integer
  The generator item ID to act on
- **`metadataId`** (path) **(required)** - integer
  The metadata item ID to act on
- **`action`** (path) **(required)** - string
  The action to perform for this item on this optimizer queue

#### Responses

**200** - 

**400** - 

**404** - Playlist not found (or user may not have permission to access playlist) or generator or metadata item not found

Content-Type: `text/html`

---

### PUT /playlists/{playlistId}/items/{playlistItemId}/move

**Operation ID:** `playlistPutItemsMove`

**Summary:** Moving items in a playlist

Moves an item in a playlist. Only works with dumb playlists.

#### Parameters

- **`playlistId`** (path) **(required)** - integer
  The ID of the playlist
- **`playlistItemId`** (path) **(required)** - integer
  The playlist item ID to move.
- **`after`** (query) - integer
  The playlist item ID to insert the new item after.  If not provided, item is moved to beginning of playlist

#### Responses

**200** - 

**400** - 

**404** - Playlist not found (or user may not have permission to access playlist)

Content-Type: `text/html`

---

### GET /playlists/{playlistId}/generators

**Operation ID:** `playlistGetGenerators`

**Summary:** Get a playlist's generators

Get all the generators in a playlist

#### Parameters

- **`playlistId`** (path) **(required)** - integer
  The ID of the playlist

#### Responses

**200** - OK

Content-Type: `application/json`

**404** - Playlist not found (or user may not have permission to access playlist) or generator not found

Content-Type: `text/html`

---

### POST /playlists/upload

**Operation ID:** `playlistPostUpload`

**Summary:** Upload

Imports m3u playlists by passing a path on the server to scan for m3u-formatted playlist files, or a path to a single playlist file.

#### Parameters

- **`path`** (query) - string
  Absolute path to a directory on the server where m3u files are stored, or the absolute path to a playlist file on the server. If the `path` argument is a directory, that path will be scanned for playlist files to be processed. Each file in that directory creates a separate playlist, with a name based on the filename of the file that created it. The GUID of each playlist is based on the filename. If the `path` argument is a file, that file will be used to create a new playlist, with the name based on the filename of the file that created it. The GUID of each playlist is based on the filename.
- **`force`** (query) - integer
  Force overwriting of duplicate playlists. By default, a playlist file uploaded with the same path will overwrite the existing playlist. The `force` argument is used to disable overwriting. If the `force` argument is set to 0, a new playlist will be created suffixed with the date and time that the duplicate was uploaded.

#### Responses

**200** - 

**403** - 

**500** - The playlist could not be imported

Content-Type: `text/html`

---

