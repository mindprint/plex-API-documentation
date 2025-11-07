# Activities

Activities provide a way to monitor and control asynchronous operations on the server. In order to receive real-time updates for activities, a client would normally subscribe via either EventSource or Websocket endpoints.

Activities are associated with HTTP replies via a special `X-Plex-Activity` header which contains the UUID of the activity.

Activities are optional cancellable. If cancellable, they may be cancelled via the `DELETE` endpoint.


**Category:** General

---

### GET /activities

**Operation ID:** `activitiesGetSlash`

**Summary:** Get all activities

List all activities on the server.  Admins can see all activities but other users can only see their own

#### Responses

**200** - OK

Content-Type: `application/json`

---

### DELETE /activities/{activityId}

**Operation ID:** `activitiesDeleteActivity`

**Summary:** Cancel a running activity

Cancel a running activity.  Admins can cancel all activities but other users can only cancel their own

#### Parameters

- **`activityId`** (path) **(required)** - string
  The UUID of the activity to cancel.

#### Responses

**200** - 

**400** - Activity is not cancellable

Content-Type: `text/html`

**404** - No activity with the provided id is found

Content-Type: `text/html`

---

