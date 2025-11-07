# Butler

The butler is responsible for running periodic tasks.  Some tasks run daily, others every few days, and some weekly.  These includes database maintenance, metadata updating, thumbnail generation, media analysis, and other tasks.

**Category:** General

---

### GET /butler

**Operation ID:** `butlerGetSlash`

**Summary:** Get all Butler tasks

Get the list of butler tasks and their scheduling


#### Responses

**200** - Butler tasks

Content-Type: `application/json`

---

### POST /butler

**Operation ID:** `butlerPostSlash`

**Summary:** Start all Butler tasks

This endpoint will attempt to start all Butler tasks that are enabled in the settings. Butler tasks normally run automatically during a time window configured on the server's Settings page but can be manually started using this endpoint. Tasks will run with the following criteria:

  1. Any tasks not scheduled to run on the current day will be skipped.
  2. If a task is configured to run at a random time during the configured window and we are outside that window, the task will start immediately.
  3. If a task is configured to run at a random time during the configured window and we are within that window, the task will be scheduled at a random time within the window.
  4. If we are outside the configured window, the task will start immediately.


#### Responses

**200** - 

---

### DELETE /butler

**Operation ID:** `butlerDeleteSlash`

**Summary:** Stop all Butler tasks

This endpoint will stop all currently running tasks and remove any scheduled tasks from the queue.

#### Responses

**200** - 

---

### POST /butler/{task}

**Operation ID:** `butlerPostTask`

**Summary:** Start a single Butler task

This endpoint will attempt to start a specific Butler task by name.


#### Parameters

- **`task`** (path) **(required)** - string
  The task name

#### Responses

**200** - Task started

Content-Type: `text/html`

**202** - Task is already running

Content-Type: `text/html`

**404** - No task with this name was found

Content-Type: `text/html`

---

### DELETE /butler/{task}

**Operation ID:** `butlerDeleteTask`

**Summary:** Stop a single Butler task

This endpoint will stop a currently running task by name, or remove it from the list of scheduled tasks if it exists


#### Parameters

- **`task`** (path) **(required)** - string
  The task name

#### Responses

**200** - 

**404** - No task with this name was found or no task with this name was running

Content-Type: `text/html`

---

