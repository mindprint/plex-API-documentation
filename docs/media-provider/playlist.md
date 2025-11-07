# Playlist

The playlist feature within a media provider
Playlists are ordered collections of media. They can be dumb (just a list of media) or smart (based on a media query, such as "all albums from 2017"). They can be organized in (optionally nesting) folders.
Retrieving a playlist, or its items, will trigger a refresh of its metadata. This may cause the duration and number of items to change.

**Category:** Media Provider

---

### GET /playlists

**Operation ID:** `playlistGetSlash`

**Summary:** Retrieve Playlists

Gets a list of playlists and playlist folders for a user. General filters are permitted, such as `sort=lastViewedAt:desc`. A flat playlist list can be retrieved using `type=15` to limit the collection to just playlists.

#### Parameters

- **`playlistType`** (query) - string
  Limit to a type of playlist
- **`smart`** (query) - integer
  Type of playlists to return, smart or not.  When not provided, will return both.

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /playlists/{playlistId}

**Operation ID:** `playlistGetPlaylist`

**Summary:** Retrieve Playlist

Gets detailed metadata for a playlist. A playlist for many purposes (rating, editing metadata, tagging), can be treated like a regular metadata item:
Smart playlist details contain the `content` attribute. This is the content URI for the generator. This can then be parsed by a client to provide smart playlist editing.

#### Parameters

- **`playlistId`** (path) **(required)** - integer
  The ID of the playlist

#### Responses

**200** - OK

Content-Type: `application/json`

**404** - Playlist not found (or user may not have permission to access playlist)

Content-Type: `text/html`

---

### GET /playlists/{playlistId}/items

**Operation ID:** `playlistGetItems`

**Summary:** Retrieve Playlist Contents

Gets the contents if a playlist. Should be paged by clients via standard mechanisms. By default leaves are returned (e.g. episodes, movies). In order to return other types you can use the `type` parameter. For example, you could use this to display a list of recently added albums vis a smart playlist. Note that for dumb playlists, items have a `playlistItemID` attribute which is used for deleting or moving items.

#### Parameters

- **`playlistId`** (path) **(required)** - integer
  The ID of the playlist
- **`type`** (query) - array
  The metadata types of the item to return.  Values past the first are only used in fetching items from the background processing playlist.

#### Responses

**200** - OK

Content-Type: `application/json`

**404** - Playlist not found (or user may not have permission to access playlist)

Content-Type: `text/html`

---

