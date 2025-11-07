# Events

The server can notify clients in real-time of a wide range of events, from library scanning, to preferences being modified, to changes to media, and many other things. This is also the mechanism by which activity progress is reported.

Two protocols for receiving the events are available: EventSource (also known as SSE), and WebSocket.


**Category:** General

---

### GET /:/eventsource/notifications

**Operation ID:** `eventsourceGetSlash`

**Summary:** Connect to Eventsource

Connect to the event source to get a stream of events

#### Parameters

- **`filter`** (query) - array
  By default, all events except logs are sent. A rich filtering mechanism is provided to allow clients to opt into or out of each event type using the `filters` parameter. For example:

- `filters=-log`: All event types except logs (the default).
- `filters=foo,bar`: Only the foo and bar event types.
- `filters=`: All events types.
- `filters=-foo,bar`: All event types except foo and bar.


#### Responses

**200** - OK

Content-Type: `application/octet-stream`

---

### GET /:/websocket/notifications

**Operation ID:** `websocketGetSlash`

**Summary:** Connect to WebSocket

Connect to the web socket to get a stream of events

#### Parameters

- **`filter`** (query) - array
  By default, all events except logs are sent. A rich filtering mechanism is provided to allow clients to opt into or out of each event type using the `filters` parameter. For example:

- `filters=-log`: All event types except logs (the default).
- `filters=foo,bar`: Only the foo and bar event types.
- `filters=`: All events types.
- `filters=-foo,bar`: All event types except foo and bar.


#### Responses

**200** - OK

Content-Type: `application/octet-stream`

---

