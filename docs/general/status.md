# Status

The status endpoints give you information about current playbacks, play history, and even terminating sessions.

**Category:** General

---

### GET /status/sessions

**Operation ID:** `statusGetSlash`

**Summary:** List Sessions

List all current playbacks on this server

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /status/sessions/background

**Operation ID:** `statusGetBackground`

**Summary:** Get background tasks

Get the list of all background tasks

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /status/sessions/history/all

**Operation ID:** `statusGetHistoryAll`

**Summary:** List Playback History

List all playback history (Admin can see all users, others can only see their own).
Pagination should be used on this endpoint.  Additionally this endpoint supports `includeFields`, `excludeFields`, `includeElements`, and `excludeElements` parameters.

#### Parameters

- **`accountID`** (query) - integer
  The account id to restrict view history
- **`viewedAt`** (query) - integer
  The time period to restrict history (typically of the form `viewedAt>=12456789`)
- **`librarySectionID`** (query) - integer
  The library section id to restrict view history
- **`metadataItemID`** (query) - integer
  The metadata item to restrict view history (can provide the id for a show to see all of that show's view history).  Note this is translated to `metadata_items.id`, `parents.id`, or `grandparents.id` internally depending on the metadata type.
- **`sort`** (query) - array
  The field on which to sort.  Multiple orderings can be specified separated by `,` and the direction specified following a `:` (`desc` or `asc`; `asc` is assumed if not provided).  Note `metadataItemID` may not be used here.

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /status/sessions/history/{historyId}

**Operation ID:** `statusGetHistory`

**Summary:** Get Single History Item

Get a single history item by id

#### Parameters

- **`historyId`** (path) **(required)** - integer
  The id of the history item (the `historyKey` from above)

#### Responses

**200** - 

**404** - History item not found

Content-Type: `text/html`

---

### DELETE /status/sessions/history/{historyId}

**Operation ID:** `statusDeleteHistory`

**Summary:** Delete Single History Item

Delete a single history item by id

#### Parameters

- **`historyId`** (path) **(required)** - integer
  The id of the history item (the `historyKey` from above)

#### Responses

**200** - OK

Content-Type: `application/json`

**404** - History item not found

Content-Type: `text/html`

---

### POST /status/sessions/terminate

**Operation ID:** `statusPostTerminate`

**Summary:** Terminate a session

Terminate a playback session kicking off the user

#### Parameters

- **`sessionId`** (query) **(required)** - string
  The session id (found in the `Session` element in [/status/sessions](#tag/Status/operation/statusGetSlash))
- **`reason`** (query) - string
  The reason to give to the user (typically displayed in the client)

#### Responses

**200** - 

**401** - Server does not have the feature enabled

Content-Type: `text/html`

**403** - sessionId is empty

Content-Type: `text/html`

**404** - Session not found

Content-Type: `text/html`

---

