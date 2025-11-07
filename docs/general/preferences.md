# Preferences



**Category:** General

---

### GET /:/prefs

**Operation ID:** `preferencesGetSlash`

**Summary:** Get all preferences

Get the list of all preferences

#### Responses

**200** - OK

Content-Type: `application/json`

---

### PUT /:/prefs

**Operation ID:** `preferencesPutSlash`

**Summary:** Set preferences

Set a set of preferences in query parameters

#### Parameters

- **`prefs`** (query) **(required)** - object
  

#### Responses

**200** - 

**400** - Attempt to set a preferences that doesn't exist

Content-Type: `text/html`

**403** - Attempt to set a preferences that doesn't exist

Content-Type: `text/html`

---

### GET /:/prefs/get

**Operation ID:** `preferencesGetGet`

**Summary:** Get a preferences

Get a single preference and value

#### Parameters

- **`id`** (query) - string
  The preference to fetch

#### Responses

**200** - OK

Content-Type: `application/json`

**404** - No preference with the provided name found.

Content-Type: `text/html`

---

