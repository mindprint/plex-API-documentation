# Live TV

LiveTV contains the playback sessions of a channel from a DVR device


**Category:** Dvr

---

### GET /livetv/sessions

**Operation ID:** `livetvSessionsGetSlash`

**Summary:** Get all sessions

Get all livetv sessions and metadata

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /livetv/sessions/{sessionId}

**Operation ID:** `livetvSessionsGetSession`

**Summary:** Get a single session

Get a single livetv session and metadata

#### Parameters

- **`sessionId`** (path) **(required)** - string
  The session id

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /livetv/sessions/{sessionId}/{consumerId}/index.m3u8

**Operation ID:** `livetvSessionsGetSessionConsumerIndex`

**Summary:** Get a session playlist index

Get a playlist index for playing this session

#### Parameters

- **`sessionId`** (path) **(required)** - string
  The session id
- **`consumerId`** (path) **(required)** - string
  The consumer id

#### Responses

**200** - Index playlist for playing HLS content

Content-Type: `application/vnd.apple.mpegurl`

**404** - Session or consumer not found

---

### GET /livetv/sessions/{sessionId}/{consumerId}/{segmentId}

**Operation ID:** `livetvSessionsGetSessionConsumerSegment`

**Summary:** Get a single session segment

Get a single livetv session segment

#### Parameters

- **`sessionId`** (path) **(required)** - string
  The session id
- **`consumerId`** (path) **(required)** - string
  The consumer id
- **`segmentId`** (path) **(required)** - string
  The segment id

#### Responses

**200** - MPEG-TS segment for playing HLS content

**404** - Session, consumer, or segment not found

---

