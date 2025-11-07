# Content

The actual content of the media provider

**Category:** Media Provider

---

### GET /library/collections/{collectionId}/composite/{updatedAt}

**Operation ID:** `libraryCollectionCollectionGetComposite`

**Summary:** Get a collection's image

Get an image for the collection based on the items within

#### Parameters

- **`collectionId`** (path) **(required)** - integer
  The collection id
- **`updatedAt`** (path) **(required)** - integer
  The update time of the image.  Used for busting cache.
- **``** () - string
  

#### Responses

**200** - OK

Content-Type: `image/jpeg`

**404** - Collection not found

Content-Type: `text/html`

---

### GET /library/collections/{collectionId}/items

**Operation ID:** `libraryCollectionCollectionGetItems`

**Summary:** Get items in a collection

Get items in a collection.  Note if this collection contains more than 100 items, paging must be used.

#### Parameters

- **`collectionId`** (path) **(required)** - integer
  The collection id

#### Responses

**200** - OK

Content-Type: `application/json`

**404** - Collection not found

Content-Type: `text/html`

---

### GET /library/metadata/{ids}

**Operation ID:** `libraryMetadataGetSlash`

**Summary:** Get a metadata item

Get one or more metadata items.

#### Parameters

- **`ids`** (path) **(required)** - array
  
- **`asyncCheckFiles`** (query) - integer
  Determines if file check should be performed asynchronously.  An activity is created to indicate progress.  Default is false.
- **`asyncRefreshLocalMediaAgent`** (query) - integer
  Determines if local media agent refresh should be performed asynchronously.  An activity is created to indicate progress.  Default is false.
- **`asyncRefreshAnalysis`** (query) - integer
  Determines if analysis refresh should be performed asynchronously.  An activity is created to indicate progress.  Default is false.
- **`checkFiles`** (query) - integer
  Determines if file check should be performed synchronously.  Specifying `asyncCheckFiles` will cause this option to be ignored.  Default is false.
- **`skipRefresh`** (query) - integer
  Determines if synchronous local media agent and analysis refresh should be skipped.  Specifying async versions will cause synchronous versions to be skipped.  Default is false.
- **`checkFileAvailability`** (query) - integer
  Determines if file existence check should be performed synchronously.  Specifying `checkFiles` will imply this option.  Default is false.
- **`asyncAugmentMetadata`** (query) - integer
  Add metadata augmentations.  An activity is created to indicate progress.  Option will be ignored if specified by non-admin or if multiple metadata items are requested.  Default is false.
- **`augmentCount`** (query) - integer
  Number of augmentations to add.  Requires `asyncAugmentMetadata` to be specified.

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /library/sections/{sectionId}/all

**Operation ID:** `librarySectionGetAll`

**Summary:** Get items in the section

Get the items in a section, potentially filtering them

#### Parameters

- **``** () - string
  
- **`sectionId`** (path) **(required)** - string
  The id of the section

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /library/sections/{sectionId}/allLeaves

**Operation ID:** `librarySectionGetAllLeaves`

**Summary:** Set section leaves

Get all leaves in a section (such as episodes in a show section)

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  Section identifier

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /library/sections/{sectionId}/arts

**Operation ID:** `librarySectionGetArts`

**Summary:** Set section artwork

Get artwork for a library section

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  Section identifier

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /library/sections/{sectionId}/albums

**Operation ID:** `librarySectionGetAlbums`

**Summary:** Set section albums

Get all albums in a music section

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  Section identifier

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /library/sections/{sectionId}/categories

**Operation ID:** `librarySectionGetCategories`

**Summary:** Set section categories

Get categories in a library section

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  Section identifier

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /library/sections/{sectionId}/cluster

**Operation ID:** `librarySectionGetCluster`

**Summary:** Set section clusters

Get clusters in a library section (typically for photos)

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  Section identifier

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /library/sections/{sectionId}/computePath

**Operation ID:** `librarySectionGetComputePath`

**Summary:** Similar tracks to transition from one to another

Get a list of audio tracks starting at one and ending at another which are similar across the path

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  Section identifier
- **`startID`** (query) **(required)** - integer
  The starting metadata item id
- **`endID`** (query) **(required)** - integer
  The ending metadata item id
- **`count`** (query) - integer
  The number of items along the path; defaults to 50
- **`maxDistance`** (query) - number
  The maximum distance allowed along the path; defaults to 0.25

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /library/sections/{sectionId}/location

**Operation ID:** `librarySectionGetLocations`

**Summary:** Get all folder locations

Get all folder locations of the media in a section

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  Section identifier

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /library/sections/{sectionId}/nearest

**Operation ID:** `librarySectionGetNearest`

**Summary:** The nearest audio tracks

Get the nearest audio tracks to a particular analysis

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  Section identifier
- **`type`** (query) - integer
  The metadata type to fetch (should be 10 for audio track)
- **`values`** (query) **(required)** - array
  The music analysis to center the search.  Typically obtained from the `musicAnalysis` of a track
- **`limit`** (query) - integer
  The limit of the number of items to fetch; defaults to 50
- **`maxDistance`** (query) - number
  The maximum distance to search, defaults to 0.25

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /library/sections/{sectionId}/moment

**Operation ID:** `librarySectionGetMoment`

**Summary:** Set section moments

Get moments in a library section (typically for photos)

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  Section identifier

#### Responses

**200** - OK

Content-Type: `application/json`

---

