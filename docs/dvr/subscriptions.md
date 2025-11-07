# Subscriptions

Subscriptions determine which media will be recorded and the criteria for selecting an airing when multiple are available


**Category:** Dvr

---

### DELETE /media/grabbers/operations/{operationId}

**Operation ID:** `mediaGrabberDeleteOperationsOperation`

**Summary:** Cancel an existing grab

Cancels an existing media grab (recording). It can be used to resolve a conflict which exists for a rolling subscription.
Note: This cancellation does not persist across a server restart, but neither does a rolling subscription itself.

#### Parameters

- **`operationId`** (path) **(required)** - string
  The ID of the operation.

#### Responses

**200** - 

**403** - User is not owner of the grab and not the admin

Content-Type: `text/html`

**404** - 

---

### GET /media/subscriptions

**Operation ID:** `mediaSubscriptionsGetSlash`

**Summary:** Get all subscriptions

Get all subscriptions and potentially the grabs too

#### Parameters

- **`includeGrabs`** (query) - integer
  Indicates whether the active grabs should be included as well
- **`includeStorage`** (query) - integer
  Compute the storage of recorded items desired by this subscription

#### Responses

**200** - OK

Content-Type: `application/json`

**403** - User cannot access DVR on this server

Content-Type: `text/html`

---

### POST /media/subscriptions

**Operation ID:** `mediaSubscriptionsPostSlash`

**Summary:** Create a subscription

Create a subscription.  The query parameters should be mostly derived from the [template](#tag/Subscriptions/operation/mediaSubscriptionsGetTemplate)

#### Parameters

- **`targetLibrarySectionID`** (query) - integer
  The library section into which we'll grab the media.  Not actually required when the subscription is to a playlist.
- **`targetSectionLocationID`** (query) - integer
  The section location into which to grab.
- **`type`** (query) - integer
  The type of the thing we're subscribing too (e.g. show, season).
- **`hints`** (query) - object
  Hints describing what we're looking for.  Note: The hint `ratingKey` is required for downloading from a PMS remote.
- **`prefs`** (query) - object
  Subscription preferences.
- **`params`** (query) - object
  Subscription parameters.
  - `mediaProviderID`: Required for downloads to indicate which MP the subscription will download into
  - `source`: Required for downloads to indicate the source of the downloaded content.


#### Responses

**200** - OK

Content-Type: `application/json`

**400** - 

**403** - User cannot access DVR on this server

Content-Type: `text/html`

**409** - An subscription with the same parameters already exists

Content-Type: `text/html`

---

### POST /media/subscriptions/process

**Operation ID:** `mediaSubscriptionsPostProcess`

**Summary:** Process all subscriptions

Process all subscriptions asynchronously

#### Responses

**200** - OK

Content-Type: `text/html`

**403** - User cannot access DVR on this server

Content-Type: `text/html`

---

### GET /media/subscriptions/{subscriptionId}

**Operation ID:** `mediaSubscriptionsGetSubscription`

**Summary:** Get a single subscription

Get a single subscription and potentially the grabs too

#### Parameters

- **`subscriptionId`** (path) **(required)** - integer
  
- **`includeGrabs`** (query) - integer
  Indicates whether the active grabs should be included as well
- **`includeStorage`** (query) - integer
  Compute the storage of recorded items desired by this subscription

#### Responses

**200** - OK

Content-Type: `application/json`

**400** - 

**403** - User cannot access DVR on this server or cannot access this subscription

Content-Type: `text/html`

**404** - 

---

### DELETE /media/subscriptions/{subscriptionId}

**Operation ID:** `mediaSubscriptionsDeleteSubscription`

**Summary:** Delete a subscription

Delete a subscription, cancelling all of its grabs as well

#### Parameters

- **`subscriptionId`** (path) **(required)** - integer
  

#### Responses

**200** - 

**400** - 

**403** - User cannot access DVR on this server or cannot access this subscription

Content-Type: `text/html`

**404** - 

---

### PUT /media/subscriptions/{subscriptionId}

**Operation ID:** `mediaSubscriptionsPutSubscription`

**Summary:** Edit a subscription

Edit a subscription's preferences

#### Parameters

- **`subscriptionId`** (path) **(required)** - integer
  
- **`prefs`** (query) - object
  

#### Responses

**200** - OK

Content-Type: `application/json`

**400** - 

**403** - User cannot access DVR on this server or cannot access this subscription

Content-Type: `text/html`

**404** - 

---

### PUT /media/subscriptions/{subscriptionId}/move

**Operation ID:** `mediaSubscriptionsPutSubscriptionMove`

**Summary:** Re-order a subscription

Re-order a subscription to change its priority

#### Parameters

- **`subscriptionId`** (path) **(required)** - integer
  
- **`after`** (query) - integer
  The subscription to move this sub after.  If missing will insert at the beginning of the list

#### Responses

**200** - OK

Content-Type: `application/json`

**400** - 

**403** - User cannot access DVR on this server or cannot access this subscription

Content-Type: `text/html`

**404** - 

---

### GET /media/subscriptions/scheduled

**Operation ID:** `mediaSubscriptionsGetScheduled`

**Summary:** Get all scheduled recordings

Get all scheduled recordings across all subscriptions

#### Responses

**200** - OK

Content-Type: `application/json`

**403** - User cannot access DVR on this server

Content-Type: `text/html`

---

### GET /media/subscriptions/template

**Operation ID:** `mediaSubscriptionsGetTemplate`

**Summary:** Get the subscription template

Get the templates for a piece of media which could include fetching one airing, season, the whole show, etc.

#### Parameters

- **`guid`** (query) - string
  The guid of the item for which to get the template

#### Responses

**200** - OK

Content-Type: `application/json`

**403** - User cannot access DVR on this server

Content-Type: `text/html`

---

