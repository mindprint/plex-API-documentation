# Play Queue

The playqueue feature within a media provider
A play queue represents the current list of media for playback. Although queues are persisted by the server, they should be regarded by the user as a fairly lightweight, an ephemeral list of items queued up for playback in a session.  There is generally one active queue for each type of media (music, video, photos) that can be added to or destroyed and replaced with a fresh queue.
Play Queues has a region, which we refer to in this doc (partially for historical reasons) as "Up Next". This region is defined by `playQueueLastAddedItemID` existing on the media container. This follows iTunes' terminology. It is a special region after the currently playing item but before the originally-played items. This enables "Party Mode" listening/viewing, where items can be added on-the-fly, and normal queue playback resumed when completed. 
You can visualize the play queue as a sliding window in the complete list of media queued for playback. This model is important when scaling to larger play queues (e.g. shuffling 40,000 audio tracks). The client only needs visibility into small areas of the queue at any given time, and the server can optimize access in this fashion.
All created play queues will have an empty "Up Next" area - unless the item is an album and no `key` is provided. In this case the "Up Next" area will be populated by the contents of the album. This is to allow queueing of multiple albums - since the 'Add to Up Next' will insert after all the tracks. This means that If you're creating a PQ from an album, you can only shuffle it if you set `key`. This is due to the above implicit queueing of albums when no `key` is provided as well as the current limitation that you cannot shuffle a PQ with an "Up Next" area.
The play queue window advances as the server receives timeline requests. The client needs to retrieve the play queue as the “now playing” item changes. There is no play queue API to update the playing item.

**Category:** Media Provider

---

### POST /playQueues

**Operation ID:** `playQueuePostSlash`

**Summary:** Create a play queue

Makes a new play queue for a device. The source of the playqueue can either be a URI, or a playlist. The response is a media container with the initial items in the queue. Each item in the queue will be a regular item but with `playQueueItemID` - a unique ID since the queue could have repeated items with the same `ratingKey`.
Note: Either `uri` or `playlistID` must be specified

#### Parameters

- **`uri`** (query) - string
  The content URI for what we're playing.
- **`playlistID`** (query) - integer
  the ID of the playlist we're playing.
- **`type`** (query) **(required)** - string
  The type of play queue to create
- **`key`** (query) - string
  The key of the first item to play, defaults to the first in the play queue.
- **`shuffle`** (query) - integer
  Whether to shuffle the playlist, defaults to 0.
- **`repeat`** (query) - integer
  If the PQ is bigger than the window, fill any empty space with wraparound items, defaults to 0.
- **`continuous`** (query) - integer
  Whether to create a continuous play queue (e.g. from an episode), defaults to 0.
- **`extrasPrefixCount`** (query) - integer
  Number of trailers to prepend a movie with not including the pre-roll. If omitted the pre-roll will not be returned in the play queue. When resuming a movie `extrasPrefixCount` should be omitted as a parameter instead of passing 0.
- **`recursive`** (query) - integer
  Only applies to queues of type photo, whether to retrieve all descendent photos from an album or section, defaults to 1.
- **`onDeck`** (query) - integer
  Only applies to queues of type show or seasons, whether to return a queue that is started on the On Deck episode if one exists. Otherwise begins the play queue on the beginning of the show or season.

#### Responses

**200** - OK

Content-Type: `application/json`

**400** - 

---

### GET /playQueues/{playQueueId}

**Operation ID:** `playQueueQueueGetSlash`

**Summary:** Retrieve a play queue

Retrieves the play queue, centered at current item. This can be treated as a regular container by play queue-oblivious clients, but they may wish to request a large window onto the queue since they won't know to refresh.

#### Parameters

- **`playQueueId`** (path) **(required)** - integer
  The ID of the play queue.
- **`own`** (query) - integer
  If the server should transfer ownership to the requesting client (used in remote control scenarios).
- **`center`** (query) - string
  The play queue item ID for the center of the window - this doesn't change the current selected item.
- **`window`** (query) - integer
  How many items on each side of the center of the window
- **`includeBefore`** (query) - integer
  Whether to include the items before the center (if 0, center is not included either), defaults to 1.
- **`includeAfter`** (query) - integer
  Whether to include the items after the center (if 0, center is not included either), defaults to 1.

#### Responses

**200** - 

**400** - 

**404** - Play queue not found

Content-Type: `text/html`

---

### PUT /playQueues/{playQueueId}

**Operation ID:** `playQueueQueuePutSlash`

**Summary:** Add a generator or playlist to a play queue

Adds an item to a play queue (e.g. party mode). Increments the version of the play queue. Takes the following parameters (`uri` and `playlistID` are mutually exclusive). Returns the modified play queue.

#### Parameters

- **`playQueueId`** (path) **(required)** - integer
  The ID of the play queue.
- **`uri`** (query) - string
  The content URI for what we're adding to the queue.
- **`playlistID`** (query) - string
  The ID of the playlist to add to the playQueue.
- **`next`** (query) - integer
  Play this item next (defaults to 0 - queueing at the end of manually queued items).

#### Responses

**200** - 

**400** - 

**404** - Play queue not found

Content-Type: `text/html`

---

### DELETE /playQueues/{playQueueId}/items

**Operation ID:** `playQueueQueueDeleteItems`

**Summary:** Clear a play queue

Deletes all items in the play queue, and increases the version of the play queue.

#### Parameters

- **`playQueueId`** (path) **(required)** - integer
  The ID of the play queue.

#### Responses

**200** - OK

Content-Type: `application/json`

---

### DELETE /playQueues/{playQueueId}/items/{playQueueItemId}

**Operation ID:** `playQueueQueueDeleteItemsItem`

**Summary:** Delete an item from a play queue

Deletes an item in a play queue. Increments the version of the play queue. Returns the modified play queue.

#### Parameters

- **`playQueueId`** (path) **(required)** - integer
  The ID of the play queue.
- **`playQueueItemId`** (path) **(required)** - integer
  The play queue item ID to delete.

#### Responses

**200** - 

**400** - 

**404** - Play queue not found

Content-Type: `text/html`

---

### PUT /playQueues/{playQueueId}/items/{playQueueItemId}/move

**Operation ID:** `playQueueQueuePutItemsMove`

**Summary:** Move an item in a play queue

Moves an item in a play queue, and increases the version of the play queue. Returns the modified play queue.

#### Parameters

- **`playQueueId`** (path) **(required)** - integer
  The ID of the play queue.
- **`playQueueItemId`** (path) **(required)** - integer
  The play queue item ID to delete.
- **`after`** (query) - integer
  The play queue item ID to insert the new item after. If not present, moves to the beginning.

#### Responses

**200** - 

**400** - 

**404** - Play queue or queue item not found

Content-Type: `text/html`

---

### PUT /playQueues/{playQueueId}/reset

**Operation ID:** `playQueuePlayQueueReset`

**Summary:** Reset a play queue

Reset a play queue to the first item being the current item

#### Parameters

- **`playQueueId`** (path) **(required)** - integer
  The ID of the play queue.

#### Responses

**200** - 

**400** - 

**404** - Play queue not found

Content-Type: `text/html`

---

### PUT /playQueues/{playQueueId}/shuffle

**Operation ID:** `playQueueQueuePutItemsShuffle`

**Summary:** Shuffle a play queue

Shuffle a play queue (or reshuffles if already shuffled). The currently selected item is maintained. Note that this is currently only supported for play queues *without* an Up Next area. Returns the modified play queue.

#### Parameters

- **`playQueueId`** (path) **(required)** - integer
  The ID of the play queue.

#### Responses

**200** - OK

Content-Type: `application/json`

**400** - 

**404** - Play queue not found or current item not found

Content-Type: `text/html`

---

### PUT /playQueues/{playQueueId}/unshuffle

**Operation ID:** `playQueueQueuePutItemsUnshuffle`

**Summary:** Unshuffle a play queue

Unshuffles a play queue and restores "natural order". Note that this is currently only supported for play queues *without* an Up Next area. Returns the modified play queue.

#### Parameters

- **`playQueueId`** (path) **(required)** - integer
  The ID of the play queue.

#### Responses

**200** - 

**400** - 

**404** - Play queue not found or current item not found

Content-Type: `text/html`

---

