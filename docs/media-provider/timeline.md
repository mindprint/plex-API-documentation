# Timeline

The actions feature within a media provider

**Category:** Media Provider

---

### PUT /:/scrobble

**Operation ID:** `putScrobble`

**Summary:** Mark an item as played

Mark an item as played.  Note, this does not create any view history of this item but rather just sets the state as played. The client must provide either the `key` or `uri` query parameter
This API does respond to the GET verb but applications should use PUT

#### Parameters

- **`identifier`** (query) **(required)** - string
  The identifier of the media provider containing the media to rate.  Typically `com.plexapp.plugins.library`
- **`key`** (query) - string
  The key of the item to rate.  This is the `ratingKey` found in metadata items
- **`uri`** (query) - string
  The URI of the item to mark as played.  See intro for description of the URIs

#### Responses

**200** - 

**400** - Bad Request.  Can occur when parameters are of the wrong type, or missing

Content-Type: `text/html`

**404** - Indicates that no library with the provide identifier can be found or no item can be found with the rating key

Content-Type: `text/html`

---

### POST /:/timeline

**Operation ID:** `timelinePostSlash`

**Summary:** Report media timeline

This endpoint is hit during media playback for an item. It must be hit whenever the play state changes, or in the absence of a play state change, in a regular fashion (generally this means every 10 seconds on a LAN/WAN, and every 20 seconds over cellular).


#### Parameters

- **`key`** (query) - string
  The details key for the item.
- **`ratingKey`** (query) - string
  The rating key attribute for the item.
- **`state`** (query) - string
  The current state of the media.
- **`playQueueItemID`** (query) - string
  If playing media from a play queue, the play queue's ID.
- **`time`** (query) - integer
  The current time offset of playback in ms.
- **`duration`** (query) - integer
  The total duration of the item in ms.
- **`continuing`** (query) - integer
  When state is `stopped`, a flag indicating whether or not the client is going to continue playing anothe item.
- **`updated`** (query) - integer
  Used when a sync client comes online and is syncing media timelines, holds the time at which the playback state was last updated.
- **`offline`** (query) - integer
  Also used by sync clients, used to indicate that a timeline is being synced from being offline, as opposed to being "live".
- **`timeToFirstFrame`** (query) - integer
  Time in seconds till first frame is displayed.  Sent only on the first playing timeline request.
- **`timeStalled`** (query) - integer
  Time in seconds spent buffering since last request.
- **`bandwidth`** (query) - integer
  Bandwidth in kbps as estimated by the client.
- **`bufferedTime`** (query) - integer
  Amount of time in seconds buffered by client.  Omit if computed by `bufferedSize` below.
- **`bufferedSize`** (query) - integer
  Size in kilobytes of data buffered by client.  Omit if computed by `bufferedTime` above
- **`X-Plex-Client-Identifier`** (header) **(required)** - string
  Unique per client.
- **`X-Plex-Session-Identifier`** (header) - string
  Unique per client playback session.  Used if a client can playback multiple items at a time (such as a browser with multiple tabs)

#### Responses

**200** - OK

Content-Type: `application/json`

**400** - 

---

### PUT /:/unscrobble

**Operation ID:** `putUnscrobble`

**Summary:** Mark an item as unplayed

Mark an item as unplayed. The client must provide either the `key` or `uri` query parameter
This API does respond to the GET verb but applications should use PUT

#### Parameters

- **`identifier`** (query) **(required)** - string
  The identifier of the media provider containing the media to rate.  Typically `com.plexapp.plugins.library`
- **`key`** (query) - string
  The key of the item to rate.  This is the `ratingKey` found in metadata items
- **`uri`** (query) - string
  The URI of the item to mark as played.  See intro for description of the URIs

#### Responses

**200** - 

**400** - Bad Request.  Can occur when parameters are of the wrong type, or missing

Content-Type: `text/html`

**404** - Indicates that no library with the provide identifier can be found or no item can be found with the rating key

Content-Type: `text/html`

---

