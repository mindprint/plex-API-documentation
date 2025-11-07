# Download Queue



**Category:** General

---

### POST /downloadQueue

**Operation ID:** `downloadQueuePost`

**Summary:** Get or create a download queue

Available: 0.2.0

Get or create a download queue for this client by its client id and for this user as identified by the token


#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /downloadQueue/{queueId}

**Operation ID:** `downloadQueueGetQueue`

**Summary:** Get a download queue

Available: 0.2.0

Get a download queue by its id


#### Parameters

- **`queueId`** (path) **(required)** - integer
  The queue id

#### Responses

**200** - OK

Content-Type: `application/json`

---

### POST /downloadQueue/{queueId}/add

**Operation ID:** `downloadQueuePostQueueAdd`

**Summary:** Add to download queue

Available: 0.2.0

Add items to the download queue


#### Parameters

- **`queueId`** (path) **(required)** - integer
  The queue id
- **`keys`** (query) **(required)** - array
  Keys to add
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  
- **``** () - string
  

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /downloadQueue/{queueId}/item/{itemId}/media

**Operation ID:** `downloadQueueGetQueueItemItemMedia`

**Summary:** Grab download queue media

Available: 0.2.0

Grab the media for a download queue item


#### Parameters

- **`queueId`** (path) **(required)** - integer
  The queue id
- **`itemId`** (path) **(required)** - integer
  The item ids

#### Responses

**200** - The raw media file

**503** - ![503](https://http.cat/503.jpg)

The queue item is not yet complete and is currently transcoding or waiting to transcode


---

### GET /downloadQueue/{queueId}/item/{itemId}/decision

**Operation ID:** `downloadQueueGetQueueItemItemDecision`

**Summary:** Grab download queue item decision

Available: 0.2.0

Grab the decision for a download queue item


#### Parameters

- **`queueId`** (path) **(required)** - integer
  The queue id
- **`itemId`** (path) **(required)** - integer
  The item ids

#### Responses

**200** - OK

Content-Type: `application/json`

**400** - The item is not in a state where a decision is available

Content-Type: `text/html`

---

### GET /downloadQueue/{queueId}/items

**Operation ID:** `downloadQueueGetQueueItems`

**Summary:** Get download queue items

Available: 0.2.0

Get items from a download queue


#### Parameters

- **`queueId`** (path) **(required)** - integer
  The queue id

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /downloadQueue/{queueId}/items/{itemId}

**Operation ID:** `downloadQueueGetQueueItemsItem`

**Summary:** Get download queue items

Available: 0.2.0

Get items from a download queue


#### Parameters

- **`queueId`** (path) **(required)** - integer
  The queue id
- **`itemId`** (path) **(required)** - array
  The item ids

#### Responses

**200** - OK

Content-Type: `application/json`

---

### DELETE /downloadQueue/{queueId}/items/{itemId}

**Operation ID:** `downloadQueueDeleteQueueItemsItem`

**Summary:** Delete download queue items

delete items from a download queue

#### Parameters

- **`queueId`** (path) **(required)** - integer
  The queue id
- **`itemId`** (path) **(required)** - array
  The item id

#### Responses

**200** - 

---

### POST /downloadQueue/{queueId}/items/{itemId}/restart

**Operation ID:** `downloadQueuePostQueueItemsItemRestart`

**Summary:** Restart processing of items from the decision

Available: 0.2.0

Reprocess download queue items with previous decision parameters


#### Parameters

- **`queueId`** (path) **(required)** - integer
  The queue id
- **`itemId`** (path) **(required)** - array
  The item ids

#### Responses

**200** - 

---

