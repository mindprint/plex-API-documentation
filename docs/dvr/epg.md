# EPG

The EPG (Electronic Program Guide) is responsible for obtaining metadata for what is airing on each channel and when


**Category:** Dvr

---

### GET /livetv/epg/channelmap

**Operation ID:** `livetvEpgGetChannelmap`

**Summary:** Compute the best channel map

Compute the best channel map, given device and lineup

#### Parameters

- **`device`** (query) **(required)** - string
  The URI describing the device
- **`lineup`** (query) **(required)** - string
  The URI describing the lineup

#### Responses

**200** - OK

Content-Type: `application/json`

**404** - No device or provider with the identifier was found

Content-Type: `text/html`

**500** - Failed to compute channel map

Content-Type: `text/html`

---

### GET /livetv/epg/channels

**Operation ID:** `livetvEpgGetChannels`

**Summary:** Get channels for a lineup

Get channels for a lineup within an EPG provider

#### Parameters

- **`lineup`** (query) **(required)** - string
  The URI describing the lineup

#### Responses

**200** - OK

Content-Type: `application/json`

**404** - No provider with the identifier was found

Content-Type: `text/html`

---

### GET /livetv/epg/countries

**Operation ID:** `livetvEpgGetCountries`

**Summary:** Get all countries

This endpoint returns a list of countries which EPG data is available for. There are three flavors, as specfied by the `flavor` attribute

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /livetv/epg/countries/{country}/{epgId}/lineups

**Operation ID:** `livetvEpgGetCountriesCountryLineups`

**Summary:** Get lineups for a country via postal code

Returns a list of lineups for a given country, EPG provider and postal code

#### Parameters

- **`country`** (path) **(required)** - string
  3 letter country code
- **`epgId`** (path) **(required)** - string
  The `providerIdentifier` of the provider
- **`postalCode`** (query) - string
  The postal code for the lineups to fetch

#### Responses

**200** - OK

Content-Type: `application/json`

**404** - No provider with the identifier was found

Content-Type: `text/html`

---

### GET /livetv/epg/countries/{country}/{epgId}/regions

**Operation ID:** `livetvEpgGetCountriesCountryRegions`

**Summary:** Get regions for a country

Get regions for a country within an EPG provider

#### Parameters

- **`country`** (path) **(required)** - string
  3 letter country code
- **`epgId`** (path) **(required)** - string
  The `providerIdentifier` of the provider

#### Responses

**200** - OK

Content-Type: `application/json`

**404** - No provider with the identifier was found

Content-Type: `text/html`

---

### GET /livetv/epg/countries/{country}/{epgId}/regions/{region}/lineups

**Operation ID:** `livetvEpgGetCountriesCountryRegionsRegionLineups`

**Summary:** Get lineups for a region

Get lineups for a region within an EPG provider

#### Parameters

- **`country`** (path) **(required)** - string
  3 letter country code
- **`epgId`** (path) **(required)** - string
  The `providerIdentifier` of the provider
- **`region`** (path) **(required)** - string
  The region for the lineup

#### Responses

**200** - OK

Content-Type: `application/json`

**404** - No provider with the identifier was found

Content-Type: `text/html`

---

### GET /livetv/epg/languages

**Operation ID:** `livetvEpgGetLanguages`

**Summary:** Get all languages

Returns a list of all possible languages for EPG data.

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /livetv/epg/lineup

**Operation ID:** `livetvEpgGetLineup`

**Summary:** Compute the best lineup

Compute the best lineup, given lineup group and device

#### Parameters

- **`device`** (query) **(required)** - string
  The URI describing the device
- **`lineupGroup`** (query) **(required)** - string
  The URI describing the lineupGroup

#### Responses

**200** - OK

**404** - No device or provider with the identifier was found

Content-Type: `text/html`

**500** - Could not get device's channels

Content-Type: `text/html`

---

### GET /livetv/epg/lineupchannels

**Operation ID:** `livetvEpgGetLineupchannels`

**Summary:** Get the channels for mulitple lineups

Get the channels across multiple lineups

#### Parameters

- **`lineup`** (query) **(required)** - array
  The URIs describing the lineups

#### Responses

**200** - OK

Content-Type: `application/json`

**404** - No provider with the identifier was found

Content-Type: `text/html`

---

