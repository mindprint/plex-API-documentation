# Log

Logging mechanism to allow clients to log to the server

**Category:** General

---

### PUT /log

**Operation ID:** `logPutSlash`

**Summary:** Logging a single-line message to the Plex Media Server log

This endpoint will write a single-line log message, including a level and source to the main Plex Media Server log.

Note: This endpoint responds to all HTTP verbs **except POST** but PUT is preferred


#### Parameters

- **`level`** (query) - integer
  An integer log level to write to the PMS log with.
  - 0: Error
  - 1: Warning
  - 2: Info
  - 3: Debug
  - 4: Verbose

- **`message`** (query) - string
  The text of the message to write to the log.
- **`source`** (query) - string
  A string indicating the source of the message.

#### Responses

**200** - 

---

### POST /log

**Operation ID:** `logPostSlash`

**Summary:** Logging a multi-line message to the Plex Media Server log

This endpoint will write multiple lines to the main Plex Media Server log in a single request. It takes a set of query strings as would normally sent to the above PUT endpoint as a linefeed-separated block of POST data. The parameters for each query string match as above.


#### Request Body

Line separated list of log items

Content-Type: `text/plain`

#### Responses

**200** - 

**400** - 

---

### POST /log/networked

**Operation ID:** `logPostPapertrail`

**Summary:** Enabling Papertrail

This endpoint will enable all Plex Media Serverlogs to be sent to the Papertrail networked logging site for a period of time

Note: This endpoint responds to all HTTP verbs but POST is preferred


#### Parameters

- **`minutes`** (query) - integer
  The number of minutes logging should be sent to Papertrail

#### Responses

**200** - 

**403** - User doesn't have permission

Content-Type: `text/html`

---

