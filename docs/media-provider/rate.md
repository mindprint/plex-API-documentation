# Rate

The rate feature within a media provider

**Category:** Media Provider

---

### PUT /:/rate

**Operation ID:** `putRate`

**Summary:** Rate an item

Set the rating on an item.
This API does respond to the GET verb but applications should use PUT

#### Parameters

- **`identifier`** (query) **(required)** - string
  The identifier of the media provider containing the media to rate.  Typically `com.plexapp.plugins.library`
- **`key`** (query) **(required)** - string
  The key of the item to rate.  This is the `ratingKey` found in metadata items
- **`rating`** (query) **(required)** - number
  The rating to give the item.
- **`ratedAt`** (query) - integer
  The time when the rating occurred.  If not present, interpreted as now.

#### Responses

**200** - 

**400** - Bad Request.  Can occur when parameters are of the wrong type, missing, or if the `ratedAt` is in the future

Content-Type: `text/html`

**404** - Indicates that no library with the provide identifier can be found or no item can be found with the rating key

Content-Type: `text/html`

---

