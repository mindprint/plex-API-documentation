# Collections



**Category:** General

---

### POST /library/collections

**Operation ID:** `libraryCollectionPostSlash`

**Summary:** Create a collection

Create a collection in the library

#### Parameters

- **`sectionId`** (query) **(required)** - string
  The section where this collection will be created
- **`title`** (query) **(required)** - string
  The title of this collection
- **`smart`** (query) - boolean
  Whether this is a smart collection.  Defaults to false
- **`uri`** (query) - string
  The URI for processing the smart collection.  Required for a smart collection
- **`type`** (query) - integer
  The type of metadata this collection will hold

#### Responses

**200** - OK

Content-Type: `application/json`

**400** - The uri is missing for a smart collection or the section could not be found

Content-Type: `text/html`

---

