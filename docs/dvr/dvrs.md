# DVRs

The DVR provides means to watch and record live TV.  This section of endpoints describes how to setup the DVR itself


**Category:** Dvr

---

### GET /livetv/dvrs

**Operation ID:** `livetvDvrGetSlash`

**Summary:** Get DVRs

Get the list of all available DVRs

#### Responses

**200** - OK

Content-Type: `application/json`

---

### POST /livetv/dvrs

**Operation ID:** `livetvDvrPostSlash`

**Summary:** Create a DVR

Creation of a DVR, after creation of a devcie and a lineup is selected

#### Parameters

- **`lineup`** (query) - string
  The EPG lineup.
- **`device`** (query) - array
  The device.
- **`language`** (query) - string
  The language.

#### Responses

**200** - 

---

### GET /livetv/dvrs/{dvrId}

**Operation ID:** `livetvDvrGetDVR`

**Summary:** Get a single DVR

Get a single DVR by its id (key)

#### Parameters

- **`dvrId`** (path) **(required)** - integer
  The ID of the DVR.

#### Responses

**200** - OK

Content-Type: `application/json`

---

### DELETE /livetv/dvrs/{dvrId}

**Operation ID:** `livetvDvrDeleteDVR`

**Summary:** Delete a single DVR

Delete a single DVR by its id (key)

#### Parameters

- **`dvrId`** (path) **(required)** - integer
  The ID of the DVR.

#### Responses

**200** - 

---

### POST /livetv/dvrs/{dvrId}/channels/{channel}/tune

**Operation ID:** `livetvDvrPostChannelsChannelTune`

**Summary:** Tune a channel on a DVR

Tune a channel on a DVR to the provided channel

#### Parameters

- **`dvrId`** (path) **(required)** - integer
  The ID of the DVR.
- **`channel`** (path) **(required)** - string
  The channel ID to tune

#### Responses

**200** - OK

Content-Type: `application/json`

**500** - Tuning failed

Content-Type: `text/html`

---

### PUT /livetv/dvrs/{dvrId}/devices/{deviceId}

**Operation ID:** `livetvDvrPutDvrDevice`

**Summary:** Add a device to an existing DVR

Add a device to an existing DVR

#### Parameters

- **`dvrId`** (path) **(required)** - integer
  The ID of the DVR.
- **`deviceId`** (path) **(required)** - integer
  The ID of the device to add.

#### Responses

**200** - OK

Content-Type: `application/json`

---

### DELETE /livetv/dvrs/{dvrId}/devices/{deviceId}

**Operation ID:** `livetvDvrDeleteDvrDevice`

**Summary:** Remove a device from an existing DVR

Remove a device from an existing DVR

#### Parameters

- **`dvrId`** (path) **(required)** - integer
  The ID of the DVR.
- **`deviceId`** (path) **(required)** - integer
  The ID of the device to add.

#### Responses

**200** - OK

Content-Type: `application/json`

---

### PUT /livetv/dvrs/{dvrId}/lineups

**Operation ID:** `livetvDvrPutLineup`

**Summary:** Add a DVR Lineup

Add a lineup to a DVR device's set of lineups.

#### Parameters

- **`dvrId`** (path) **(required)** - integer
  The ID of the DVR.
- **`lineup`** (query) **(required)** - string
  The lineup to delete

#### Responses

**200** - OK

Content-Type: `application/json`

---

### DELETE /livetv/dvrs/{dvrId}/lineups

**Operation ID:** `livetvDvrDeleteLineup`

**Summary:** Delete a DVR Lineup

Deletes a DVR device's lineup.

#### Parameters

- **`dvrId`** (path) **(required)** - integer
  The ID of the DVR.
- **`lineup`** (query) **(required)** - string
  The lineup to delete

#### Responses

**200** - OK

Content-Type: `application/json`

---

### PUT /livetv/dvrs/{dvrId}/prefs

**Operation ID:** `livetvDvrPutPrefs`

**Summary:** Set DVR preferences

Set DVR preferences by name avd value

#### Parameters

- **`dvrId`** (path) **(required)** - integer
  The ID of the DVR.
- **`name`** (query) - string
  Set the `name` preference to the provided value

#### Responses

**200** - OK

Content-Type: `application/json`

---

### POST /livetv/dvrs/{dvrId}/reloadGuide

**Operation ID:** `livetvDvrPostReloadGuide`

**Summary:** Tell a DVR to reload program guide

Tell a DVR to reload program guide

#### Parameters

- **`dvrId`** (path) **(required)** - integer
  The ID of the DVR.

#### Responses

**200** - OK

Content-Type: `text/html`

---

### DELETE /livetv/dvrs/{dvrId}/reloadGuide

**Operation ID:** `livetvDvrDeleteReloadGuide`

**Summary:** Tell a DVR to stop reloading program guide

Tell a DVR to stop reloading program guide

#### Parameters

- **`dvrId`** (path) **(required)** - integer
  The ID of the DVR.

#### Responses

**200** - 

---

