# Library Collections

Endpoints for manipulating collections.  In addition to these endpoints, `/library/collections/:collectionId/X` will be rerouted to `/library/metadata/:collectionId/X` and respond to those endpoints as well.

**Category:** General

---

### PUT /library/collections/{collectionId}/items

**Operation ID:** `libraryCollectionCollectionPutItems`

**Summary:** Add items to a collection

Add items to a collection by uri

#### Parameters

- **`collectionId`** (path) **(required)** - integer
  The collection id
- **`uri`** (query) **(required)** - string
  The URI describing the items to add to this collection

#### Responses

**200** - OK

Content-Type: `application/json`

**404** - Collection not found

Content-Type: `text/html`

---

### PUT /library/collections/{collectionId}/items/{itemId}

**Operation ID:** `libraryCollectionCollectionPutItemsItem`

**Summary:** Delete an item from a collection

Delete an item from a collection

#### Parameters

- **`collectionId`** (path) **(required)** - integer
  The collection id
- **`itemId`** (path) **(required)** - integer
  The item to delete

#### Responses

**200** - OK

Content-Type: `application/json`

**400** - Item not found

Content-Type: `text/html`

**404** - Collection not found

Content-Type: `text/html`

---

### PUT /library/collections/{collectionId}/items/{itemId}/move

**Operation ID:** `libraryCollectionCollectionPutItemsItemMove`

**Summary:** Reorder an item in the collection

Reorder items in a collection with one item after another

#### Parameters

- **`collectionId`** (path) **(required)** - integer
  The collection id
- **`itemId`** (path) **(required)** - integer
  The item to move
- **`after`** (query) - integer
  The item to move this item after.  If not provided, this item will be moved to the beginning

#### Responses

**200** - OK

Content-Type: `application/json`

**400** - Item not found

Content-Type: `text/html`

**404** - Collection not found

Content-Type: `text/html`

---

