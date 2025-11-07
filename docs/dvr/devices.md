# Devices

Media grabbers provide ways for media to be obtained for a given protocol. The simplest ones are `stream` and `download`. More complex grabbers can have associated devices

Network tuners can present themselves on the network using the Simple Service Discovery Protocol and Plex Media Server will discover them. The following XML is an example of the data returned from SSDP. The `deviceType`, `serviceType`, and `serviceId` values must remain as they are in the example in order for PMS to properly discover the device. Other less-obvious fields are described in the parameters section below.

Example SSDP output
```
<root xmlns="urn:schemas-upnp-org:device-1-0">
    <specVersion>
        <major>1</major>
        <minor>0</minor>
    </specVersion>
    <device>
        <deviceType>urn:plex-tv:device:Media:1</deviceType>
        <friendlyName>Turing Hopper 3000</friendlyName>
        <manufacturer>Plex, Inc.</manufacturer>
        <manufacturerURL>https://plex.tv/</manufacturerURL>
        <modelDescription>Turing Hopper 3000 Media Grabber</modelDescription>
        <modelName>Plex Media Grabber</modelName>
        <modelNumber>1</modelNumber>
        <modelURL>https://plex.tv</modelURL>
        <UDN>uuid:42fde8e4-93b6-41e5-8a63-12d848655811</UDN>
        <serviceList>
            <service>
                <URLBase>http://10.0.0.5:8088</URLBase>
                <serviceType>urn:plex-tv:service:MediaGrabber:1</serviceType>
                <serviceId>urn:plex-tv:serviceId:MediaGrabber</serviceId>
            </service>
        </serviceList>
    </device>
</root>
```

  - UDN: (string) A UUID for the device. This should be unique across models of a device at minimum.
  - URLBase: (string) The base HTTP URL for the device from which all of the other endpoints are hosted.


**Category:** Dvr

---

### GET /media/grabbers

**Operation ID:** `mediaGrabberGetSlash`

**Summary:** Get available grabbers

Get available grabbers visible to the server

#### Parameters

- **`protocol`** (query) - string
  Only return grabbers providing this protocol.

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /media/grabbers/devices

**Operation ID:** `mediaGrabberGetDevices`

**Summary:** Get all devices

Get the list of all devices present

#### Responses

**200** - OK

Content-Type: `application/json`

---

### POST /media/grabbers/devices

**Operation ID:** `mediaGrabberPostDevices`

**Summary:** Add a device

This endpoint adds a device to an existing grabber. The device is identified, and added to the correct grabber.

#### Parameters

- **`uri`** (query) - string
  The URI of the device.

#### Responses

**200** - OK

Content-Type: `application/json`

**400** - 

---

### POST /media/grabbers/devices/discover

**Operation ID:** `mediaGrabberPostDeviceDiscover`

**Summary:** Tell grabbers to discover devices

Tell grabbers to discover devices

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /media/grabbers/devices/{deviceId}

**Operation ID:** `mediaGrabberDevicesDeviceGetSlash`

**Summary:** Get device details

Get a device's details by its id

#### Parameters

- **`deviceId`** (path) **(required)** - integer
  The ID of the device.

#### Responses

**200** - OK

Content-Type: `application/json`

**404** - Device not found

Content-Type: `text/html`

---

### DELETE /media/grabbers/devices/{deviceId}

**Operation ID:** `mediaGrabberDevicesDeviceDeleteSlash`

**Summary:** Remove a device

Remove a devices by its id along with its channel mappings

#### Parameters

- **`deviceId`** (path) **(required)** - integer
  The ID of the device.

#### Responses

**200** - OK

Content-Type: `application/json`

**404** - Device not found

Content-Type: `text/html`

---

### PUT /media/grabbers/devices/{deviceId}

**Operation ID:** `mediaGrabberDevicesDevicePutSlash`

**Summary:** Enable or disable a device

Enable or disable a device by its id

#### Parameters

- **`deviceId`** (path) **(required)** - integer
  The ID of the device.
- **`enabled`** (query) - integer
  Whether to enable the device

#### Responses

**200** - OK

Content-Type: `application/json`

**404** - Device not found

Content-Type: `text/html`

---

### PUT /media/grabbers/devices/{deviceId}/channelmap

**Operation ID:** `mediaGrabberDevicesDevicePutChannelmap`

**Summary:** Set a device's channel mapping

Set a device's channel mapping

#### Parameters

- **`deviceId`** (path) **(required)** - integer
  The ID of the device.
- **`channelMapping`** (query) - object
  The mapping of changes, passed as a map of device channel to lineup VCN.
- **`channelMappingByKey`** (query) - object
  The mapping of changes, passed as a map of device channel to lineup key.
- **`channelsEnabled`** (query) - array
  The channels which are enabled.

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /media/grabbers/devices/{deviceId}/channels

**Operation ID:** `mediaGrabberDevicesDeviceGetChannels`

**Summary:** Get a device's channels

Get a device's channels by its id

#### Parameters

- **`deviceId`** (path) **(required)** - integer
  The ID of the device.

#### Responses

**200** - OK

Content-Type: `application/json`

**404** - Device not found

Content-Type: `text/html`

---

### PUT /media/grabbers/devices/{deviceId}/prefs

**Operation ID:** `mediaGrabberDevicesDevicePutPrefs`

**Summary:** Set device preferences

Set device preferences by its id

#### Parameters

- **`deviceId`** (path) **(required)** - integer
  The ID of the device.
- **`name`** (query) - string
  The preference names and values.

#### Responses

**200** - 

---

### POST /media/grabbers/devices/{deviceId}/scan

**Operation ID:** `mediaGrabberDevicesDevicePostScan`

**Summary:** Tell a device to scan for channels

Tell a device to scan for channels

#### Parameters

- **`deviceId`** (path) **(required)** - integer
  The ID of the device.
- **`source`** (query) - string
  A valid source for the scan

#### Responses

**200** - OK

Content-Type: `application/json`

---

### DELETE /media/grabbers/devices/{deviceId}/scan

**Operation ID:** `mediaGrabberDeleteDevicesDeviceScan`

**Summary:** Tell a device to stop scanning for channels

Tell a device to stop scanning for channels

#### Parameters

- **`deviceId`** (path) **(required)** - integer
  The ID of the device.

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /media/grabbers/devices/{deviceId}/thumb/{version}

**Operation ID:** `mediaGrabberDevicesDeviceGetThumbVersion`

**Summary:** Get device thumb

Get a device's thumb for display to the user

#### Parameters

- **`deviceId`** (path) **(required)** - integer
  The ID of the device.
- **`version`** (path) **(required)** - integer
  A version number of the thumb used for busting cache

#### Responses

**200** - The thumbnail for the device

**301** - The thumb URL on the device

**404** - No thumb found for this device

Content-Type: `text/html`

---

