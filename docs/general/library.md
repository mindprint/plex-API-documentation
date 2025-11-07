# Library

Library endpoints which are outside of the Media Provider API.  Typically this is manipulation of the library (adding/removing sections, modifying preferences, etc).

**Category:** General

---

### GET /library/all

**Operation ID:** `libraryGetAll`

**Summary:** Get all items in library

Request all metadata items according to a query.

#### Parameters

- **``** () - string
  

#### Responses

**200** - OK

Content-Type: `application/json`

---

### DELETE /library/caches

**Operation ID:** `libraryDeleteCaches`

**Summary:** Delete library caches

Delete the hub caches so they are recomputed on next request

#### Responses

**200** - 

---

### PUT /library/clean/bundles

**Operation ID:** `libraryPutCleanBundles`

**Summary:** Clean bundles

Clean out any now unused bundles.  Bundles can become unused when media is deleted

#### Responses

**200** - 

---

### POST /library/file

**Operation ID:** `libraryPostFile`

**Summary:** Ingest a transient item

This endpoint takes a file path specified in the `url` parameter, matches it using the scanner's match mechanism, downloads rich metadata, and then ingests the item as a transient item (without a library section). In the case where the file represents an episode, the entire tree (show, season, and episode) is added as transient items. At this time, movies and episodes are the only supported types, which are gleaned automatically from the file path.
Note that any of the parameters passed to the metadata details endpoint (e.g. `includeExtras=1`) work here.

#### Parameters

- **`url`** (query) - string
  The file of the file to ingest.
- **`virtualFilePath`** (query) - string
  A virtual path to use when the url is opaque.
- **`computeHashes`** (query) - integer
  Whether or not to compute Plex and OpenSubtitle hashes for the file. Defaults to 0.
- **`ingestNonMatches`** (query) - integer
  Whether or not non matching media should be stored. Defaults to 0.

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /library/matches

**Operation ID:** `libraryGetMatches`

**Summary:** Get library matches

The matches endpoint is used to match content external to the library with content inside the library. This is done by passing a series of semantic "hints" about the content (its type, name, or release year). Each type (e.g. movie) has a canonical set of minimal required hints.
This ability to match content is useful in a variety of scenarios. For example, in the DVR, the EPG uses the endpoint to match recording rules against airing content. And in the cloud, the UMP uses the endpoint to match up a piece of media with rich metadata.
The endpoint response can including multiple matches, if there is ambiguity, each one containing a `score` from 0 to 100. For somewhat historical reasons, anything over 85 is considered a positive match (we prefer false negatives over false positives in general for matching).
The `guid` hint is somewhat special, in that it generally represents a unique identity for a piece of media (e.g. the IMDB `ttXXX`) identifier, in contrast with other hints which can be much more ambiguous (e.g. a title of `Jane Eyre`, which could refer to the 1943 or the 2011 version).
Episodes require either a season/episode pair, or an air date (or both). Either the path must be sent, or the show title

#### Parameters

- **`type`** (query) **(required)** - integer
  The metadata type to match against
- **`includeFullMetadata`** (query) - integer
  
- **`includeAncestorMetadata`** (query) - integer
  
- **`includeAlternateMetadataSources`** (query) - integer
  
- **`guid`** (query) - string
  Used for movies, shows, artists, albums, and tracks.  Allowed for various URI schemes, to be defined.
- **`title`** (query) - string
  Used for movies, shows, artists, and albums.  Required if `path` is not specified.
- **`year`** (query) - integer
  Used for movies shows, and albums.  Optional.
- **`path`** (query) - string
  Used for movies, episodes, and tracks.  The full path to the media file, used for "cloud-scanning" an item.
- **`grandparentTitle`** (query) - string
  Used for episodes and tracks.  The title of the show/artist. Required if `path` isn't passed.
- **`grandparentYear`** (query) - integer
  Used for episodes.  The year of the show.
- **`parentIndex`** (query) - integer
  Used for episodes and tracks.  The season/album number.
- **`index`** (query) - integer
  Used for episodes and tracks.  The episode/tracks number in the season/album.
- **`originallyAvailableAt`** (query) - string
  Used for episodes.  In the format `YYYY-MM-DD`.
- **`parentTitle`** (query) - string
  Used for albums and tracks. The artist name for albums or the album name for tracks.

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /library/media/{mediaId}/chapterImages/{chapter}

**Operation ID:** `libraryGetMediaMediaChapterImagesChapter`

**Summary:** Get a chapter image

Get a single chapter image for a piece of media

#### Parameters

- **`mediaId`** (path) **(required)** - integer
  The id of the media item
- **`chapter`** (path) **(required)** - integer
  The index of the chapter

#### Responses

**200** - OK

Content-Type: `image/jpeg`

**404** - Either the media item or the chapter image was not found

Content-Type: `text/html`

---

### PUT /library/metadata/{ids}

**Operation ID:** `libraryMetadataPutSlash`

**Summary:** Edit a metadata item

Edit metadata items setting fields

#### Parameters

- **`ids`** (path) **(required)** - array
  
- **`args`** (query) - object
  The new values for the metadata item

#### Responses

**200** - 

**400** - Media items could not be deleted

Content-Type: `text/html`

---

### DELETE /library/metadata/{ids}

**Operation ID:** `libraryMetadataDeleteSlash`

**Summary:** Delete a metadata item

Delete a single metadata item from the library, deleting media as well

#### Parameters

- **`ids`** (path) **(required)** - string
  
- **`proxy`** (query) - integer
  Whether proxy items, such as media optimized versions, should also be deleted.  Defaults to false.

#### Responses

**200** - 

**400** - Media items could not be deleted

Content-Type: `text/html`

---

### PUT /library/metadata/{ids}/addetect

**Operation ID:** `libraryMetadataPutAddetect`

**Summary:** Ad-detect an item

Start the detection of ads in a metadata item

#### Parameters

- **`ids`** (path) **(required)** - string
  

#### Responses

**200** - 

---

### GET /library/metadata/{ids}/allLeaves

**Operation ID:** `libraryMetadataGetAllLeaves`

**Summary:** Get the leaves of an item

Get the leaves for a metadata item such as the episodes in a show

#### Parameters

- **`ids`** (path) **(required)** - string
  

#### Responses

**200** - OK

Content-Type: `application/json`

---

### PUT /library/metadata/{ids}/analyze

**Operation ID:** `libraryMetadataPutAnalyze`

**Summary:** Analyze an item

Start the analysis of a metadata item

#### Parameters

- **`ids`** (path) **(required)** - string
  
- **`thumbOffset`** (query) - number
  Set the offset to be used for thumbnails
- **`artOffset`** (query) - number
  Set the offset to be used for artwork

#### Responses

**200** - 

---

### PUT /library/metadata/{ids}/chapterThumbs

**Operation ID:** `libraryMetadataPutChapterThumbs`

**Summary:** Generate thumbs of chapters for an item

Start the chapter thumb generation for an item

#### Parameters

- **`ids`** (path) **(required)** - string
  
- **`force`** (query) - integer
  

#### Responses

**200** - 

---

### PUT /library/metadata/{ids}/credits

**Operation ID:** `libraryMetadataPutCredits`

**Summary:** Credit detect a metadata item

Start credit detection on a metadata item

#### Parameters

- **`ids`** (path) **(required)** - string
  
- **`force`** (query) - integer
  
- **`manual`** (query) - integer
  

#### Responses

**200** - 

---

### GET /library/metadata/{ids}/extras

**Operation ID:** `libraryMetadataGetExtras`

**Summary:** Get an item's extras

Get the extras for a metadata item

#### Parameters

- **`ids`** (path) **(required)** - string
  

#### Responses

**200** - OK

Content-Type: `application/json`

---

### POST /library/metadata/{ids}/extras

**Operation ID:** `libraryMetadataPostExtras`

**Summary:** Add to an item's extras

Add an extra to a metadata item

#### Parameters

- **`ids`** (path) **(required)** - string
  
- **`extraType`** (query) - integer
  The metadata type of the extra
- **`url`** (query) **(required)** - string
  The URL of the extra
- **`title`** (query) **(required)** - string
  The title of the extra

#### Responses

**200** - 

**404** - Either the metadata item is not present or the extra could not be added

Content-Type: `text/html`

---

### GET /library/metadata/{ids}/file

**Operation ID:** `libraryMetadataGetFile`

**Summary:** Get a file from a metadata or media bundle

Get a bundle file for a metadata or media item.  This is either an image or a mp3 (for a show's theme)

#### Parameters

- **`ids`** (path) **(required)** - string
  
- **`url`** (query) - string
  The bundle url, typically starting with `metadata://` or `media://`

#### Responses

**200** - OK

Content-Type: `audio/mpeg3`

---

### PUT /library/metadata/{ids}/index

**Operation ID:** `libraryMetadataPutIndex`

**Summary:** Start BIF generation of an item

Start the indexing (BIF generation) of an item

#### Parameters

- **`ids`** (path) **(required)** - string
  
- **`force`** (query) - integer
  

#### Responses

**200** - 

---

### PUT /library/metadata/{ids}/intro

**Operation ID:** `libraryMetadataPutIntro`

**Summary:** Intro detect an item

Start the detection of intros in a metadata item

#### Parameters

- **`ids`** (path) **(required)** - string
  
- **`force`** (query) - integer
  Indicate whether detection should be re-run
- **`threshold`** (query) - number
  The threshold for determining if content is an intro or not

#### Responses

**200** - 

---

### POST /library/metadata/{ids}/marker

**Operation ID:** `libraryMetadataPostMarker`

**Summary:** Create a marker

Create a marker for this user on the metadata item

#### Parameters

- **`ids`** (path) **(required)** - string
  
- **`type`** (query) **(required)** - integer
  The type of marker to edit/create
- **`startTimeOffset`** (query) **(required)** - integer
  The start time of the marker
- **`endTimeOffset`** (query) - integer
  The end time of the marker
- **`attributes`** (query) - object
  The attributes to assign to this marker

#### Responses

**200** - OK

Content-Type: `application/json`

**400** - Request parameters are bad, such as an `endTimeOffset` prior to the `startTimeOffset`

Content-Type: `text/html`

---

### DELETE /library/metadata/{ids}/marker/{marker}

**Operation ID:** `libraryMetadataDeleteMarkerMarker`

**Summary:** Delete a marker

Delete a marker for this user on the metadata item

#### Parameters

- **`ids`** (path) **(required)** - string
  
- **`marker`** (path) **(required)** - string
  

#### Responses

**200** - 

**400** - Marker is not a bookmark

Content-Type: `text/html`

**404** - Marker could not be found

Content-Type: `text/html`

---

### PUT /library/metadata/{ids}/marker/{marker}

**Operation ID:** `libraryMetadataPutMarkerMarker`

**Summary:** Edit a marker

Edit a marker for this user on the metadata item

#### Parameters

- **`ids`** (path) **(required)** - string
  
- **`marker`** (path) **(required)** - string
  The id of the marker to edit
- **`type`** (query) **(required)** - integer
  The type of marker to edit/create
- **`startTimeOffset`** (query) **(required)** - integer
  The start time of the marker
- **`endTimeOffset`** (query) - integer
  The end time of the marker
- **`attributes`** (query) - object
  The attributes to assign to this marker

#### Responses

**200** - 

**400** - 

**404** - The marker could not be found

Content-Type: `text/html`

---

### PUT /library/metadata/{ids}/match

**Operation ID:** `libraryMetadataPutMatch`

**Summary:** Match a metadata item

Match a metadata item to a guid

#### Parameters

- **`ids`** (path) **(required)** - string
  
- **`guid`** (query) - string
  
- **`name`** (query) - string
  
- **`year`** (query) - integer
  

#### Responses

**200** - 

---

### PUT /library/metadata/{ids}/matches

**Operation ID:** `libraryMetadataGetMatches`

**Summary:** Get metadata matches for an item

Get the list of metadata matches for a metadata item

#### Parameters

- **`ids`** (path) **(required)** - string
  
- **`title`** (query) - string
  
- **`parentTitle`** (query) - string
  
- **`agent`** (query) - string
  
- **`language`** (query) - string
  
- **`year`** (query) - integer
  
- **`manual`** (query) - integer
  

#### Responses

**200** - OK

Content-Type: `application/json`

---

### DELETE /library/metadata/{ids}/media/{mediaItem}

**Operation ID:** `libraryMetadataDeleteMediaMediaItem`

**Summary:** Delete a media item

Delete a single media from a metadata item in the library

#### Parameters

- **`ids`** (path) **(required)** - string
  
- **`mediaItem`** (path) **(required)** - string
  
- **`proxy`** (query) - integer
  Whether proxy items, such as media optimized versions, should also be deleted.  Defaults to false.

#### Responses

**200** - 

**400** - Media item could not be deleted

Content-Type: `text/html`

**404** - Media item could not be found

Content-Type: `text/html`

---

### PUT /library/metadata/{ids}/merge

**Operation ID:** `libraryMetadataPutMerge`

**Summary:** Merge a metadata item

Merge a metadata item with other items

#### Parameters

- **`ids`** (path) **(required)** - string
  
- **`ids`** (query) - array
  

#### Responses

**200** - 

---

### GET /library/metadata/{ids}/nearest

**Operation ID:** `libraryMetadataGetNearest`

**Summary:** Get nearest tracks to metadata item

Get the nearest tracks, sonically, to the provided track

#### Parameters

- **`ids`** (path) **(required)** - string
  
- **`excludeParentID`** (query) - integer
  
- **`excludeGrandparentID`** (query) - integer
  
- **`limit`** (query) - integer
  
- **`maxDistance`** (query) - number
  

#### Responses

**200** - OK

Content-Type: `application/json`

---

### PUT /library/metadata/{ids}/prefs

**Operation ID:** `libraryMetadataPutPrefs`

**Summary:** Set metadata preferences

Set the preferences on a metadata item

#### Parameters

- **`ids`** (path) **(required)** - string
  
- **`args`** (query) - object
  

#### Responses

**200** - 

---

### PUT /library/metadata/{ids}/refresh

**Operation ID:** `libraryMetadataPutRefresh`

**Summary:** Refresh a metadata item

Refresh a metadata item from the agent

#### Parameters

- **`ids`** (path) **(required)** - string
  
- **`agent`** (query) - string
  
- **`markUpdated`** (query) - integer
  

#### Responses

**200** - 

---

### GET /library/metadata/{ids}/related

**Operation ID:** `libraryMetadataGetRelated`

**Summary:** Get related items

Get a hub of related items to a metadata item

#### Parameters

- **`ids`** (path) **(required)** - string
  

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /library/metadata/{ids}/similar

**Operation ID:** `libraryMetadataGetSimilar`

**Summary:** Get similar items

Get a list of similar items to a metadata item

#### Parameters

- **`ids`** (path) **(required)** - string
  
- **`count`** (query) - integer
  The maximum number of similar items; defaults to 200

#### Responses

**200** - OK

Content-Type: `application/json`

---

### PUT /library/metadata/{ids}/split

**Operation ID:** `libraryMetadataPutSplit`

**Summary:** Split a metadata item

Split a metadata item into multiple items

#### Parameters

- **`ids`** (path) **(required)** - string
  

#### Responses

**200** - 

---

### GET /library/metadata/{ids}/subtitles

**Operation ID:** `libraryMetadataPostSubtitles`

**Summary:** Add subtitles

Add a subtitle to a metadata item

#### Parameters

- **`ids`** (path) **(required)** - string
  
- **`title`** (query) - string
  
- **`language`** (query) - string
  
- **`mediaItemID`** (query) - integer
  
- **`url`** (query) - string
  The URL of the subtitle.  If not provided, the contents of the subtitle must be in the post body
- **`format`** (query) - string
  
- **`forced`** (query) - integer
  
- **`hearingImpaired`** (query) - integer
  

#### Responses

**200** - 

---

### GET /library/metadata/{ids}/tree

**Operation ID:** `libraryMetadataGetTree`

**Summary:** Get metadata items as a tree

Get a tree of metadata items, such as the seasons/episodes of a show

#### Parameters

- **`ids`** (path) **(required)** - string
  

#### Responses

**200** - OK

Content-Type: `application/json`

---

### PUT /library/metadata/{ids}/unmatch

**Operation ID:** `libraryMetadataPutUnmatch`

**Summary:** Unmatch a metadata item

Unmatch a metadata item to info fetched from the agent

#### Parameters

- **`ids`** (path) **(required)** - string
  

#### Responses

**200** - 

---

### GET /library/metadata/{ids}/users/top

**Operation ID:** `libraryMetadataGetUsersTop`

**Summary:** Get metadata top users

Get the list of users which have played this item starting with the most

#### Parameters

- **`ids`** (path) **(required)** - string
  

#### Responses

**200** - OK

Content-Type: `application/json`

---

### PUT /library/metadata/{ids}/voiceActivity

**Operation ID:** `libraryMetadataPutVoiceActivity`

**Summary:** Detect voice activity

Start the detection of voice in a metadata item

#### Parameters

- **`ids`** (path) **(required)** - string
  
- **`force`** (query) - integer
  Indicate whether detection should be re-run
- **`manual`** (query) - integer
  Indicate whether detection is manually run

#### Responses

**200** - 

---

### POST /library/metadata/{ids}/{element}

**Operation ID:** `libraryMetadataPostElement`

**Summary:** Set an item's artwork, theme, etc

Set the artwork, thumb, element for a metadata item
Generally only the admin can perform this action.  The exception is if the metadata is a playlist created by the user

#### Parameters

- **`ids`** (path) **(required)** - string
  
- **`element`** (path) **(required)** - string
  
- **`url`** (query) - string
  The url of the new asset.  If not provided, the binary of the asset must be provided in the post body.

#### Responses

**200** - 

---

### PUT /library/metadata/{ids}/{element}

**Operation ID:** `libraryMetadataPutElement`

**Summary:** Set an item's artwork, theme, etc

Set the artwork, thumb, element for a metadata item
Generally only the admin can perform this action.  The exception is if the metadata is a playlist created by the user

#### Parameters

- **`ids`** (path) **(required)** - string
  
- **`element`** (path) **(required)** - string
  
- **`url`** (query) - string
  The url of the new asset.

#### Responses

**200** - 

---

### GET /library/metadata/{ids}/{element}/{timestamp}

**Operation ID:** `libraryMetadataGetElement`

**Summary:** Get an item's artwork, theme, etc

Get the artwork, thumb, element for a metadata item

#### Parameters

- **`ids`** (path) **(required)** - string
  
- **`element`** (path) **(required)** - string
  
- **`timestamp`** (path) **(required)** - integer
  A timestamp on the element used for cache management in the client

#### Responses

**200** - OK

Content-Type: `audio/mpeg3`

---

### GET /library/metadata/augmentations/{augmentationId}

**Operation ID:** `libraryGetMetadataAugmentationsAugmentation`

**Summary:** Get augmentation status

Get augmentation status and potentially wait for completion

#### Parameters

- **`augmentationId`** (path) **(required)** - string
  The id of the augmentation
- **`wait`** (query) - integer
  Wait for augmentation completion before returning

#### Responses

**204** - 

**401** - This augmentation is not owned by the requesting user

Content-Type: `text/html`

**404** - No augmentation found

Content-Type: `text/html`

---

### PUT /library/optimize

**Operation ID:** `libraryPutOptimize`

**Summary:** Optimize the Database

Initiate optimize on the database.

#### Parameters

- **`async`** (query) - integer
  If set, don't wait for completion but return an activity

#### Responses

**200** - 

---

### PUT /library/parts/{partId}

**Operation ID:** `libraryPutPartsPart`

**Summary:** Set stream selection

Set which streams (audio/subtitle) are selected by this user

#### Parameters

- **`partId`** (path) **(required)** - integer
  The id of the part to select streams on
- **`audioStreamID`** (query) - integer
  The id of the audio stream to select in this part
- **`subtitleStreamID`** (query) - integer
  The id of the subtitle stream to select in this part.  Specify 0 to select no subtitle
- **`allParts`** (query) - integer
  Perform the same for all parts of this media selecting similar streams in each

#### Responses

**200** - 

**400** - One of the audio or subtitle streams does not belong to this part

Content-Type: `text/html`

---

### GET /library/parts/{partId}/indexes/{index}

**Operation ID:** `libraryGetPartsPartIndexesIndex`

**Summary:** Get BIF index for a part

Get BIF index for a part by index type

#### Parameters

- **`partId`** (path) **(required)** - integer
  The part id who's index is to be fetched
- **`index`** (path) **(required)** - string
  The type of index to grab.
- **`interval`** (query) - integer
  The interval between images to return in ms.

#### Responses

**200** - OK

Content-Type: `application/octet-stream`

**404** - The part or the index doesn't exist or the interval is too small

Content-Type: `text/html`

---

### GET /library/parts/{partId}/indexes/{index}/{offset}

**Operation ID:** `libraryGetPartsPartIndexesIndexOffset`

**Summary:** Get an image from part BIF

Extract an image from the BIF for a part at a particular offset

#### Parameters

- **`partId`** (path) **(required)** - integer
  The part id who's index is to be fetched
- **`index`** (path) **(required)** - string
  The type of index to grab.
- **`offset`** (path) **(required)** - integer
  The offset to seek in ms.

#### Responses

**200** - OK

Content-Type: `image/jpeg`

**404** - The part or the index doesn't exist

Content-Type: `text/html`

---

### GET /library/parts/{partId}/{changestamp}/{filename}

**Operation ID:** `libraryGetPartsPartChangestampFilename`

**Summary:** Get a media part

Get a media part for streaming or download.
  - streaming: This is the default scenario.  Bandwidth usage on this endpoint will be guaranteed (on the server's end) to be at least the bandwidth reservation given in the decision.  If no decision exists, an ad-hoc decision will be created if sufficient bandwidth exists.  Clients should not rely on ad-hoc decisions being made as this may be removed in the future.
  - download: Indicated if the query parameter indicates this is a download.  Bandwidth will be prioritized behind playbacks and will get a fair share of what remains.


#### Parameters

- **`partId`** (path) **(required)** - integer
  The part id who's index is to be fetched
- **`changestamp`** (path) **(required)** - integer
  The changestamp of the part; used for busting potential caches.  Provided in the `key` for the part
- **`filename`** (path) **(required)** - string
  A generic filename used for a client media stack which relies on the extension in the request.  Provided in the `key` for the part
- **`download`** (query) - integer
  Whether this is a file download

#### Responses

**200** - OK

**403** - Client requested download and server owner has forbidden download of media

Content-Type: `text/html`

**404** - The part doesn't exist

Content-Type: `text/html`

**503** - Client requested the part without a decision and no decision could be made or decision is for a transcode

Content-Type: `text/html`

**509** - Client requested the part without a decision and no decision could be made because there is insufficient bandwidth for client to direct play this part

Content-Type: `text/html`

---

### GET /library/people/{personId}

**Operation ID:** `libraryGetPeoplePerson`

**Summary:** Get person details

Get details for a single actor.

#### Parameters

- **`personId`** (path) **(required)** - string
  Either the PMS tag `id` of the person or `tagKey` of the actor.  Note the `tagKey` is the hex portion of the plex guid for the actor

#### Responses

**200** - OK

Content-Type: `application/json`

**404** - 

---

### GET /library/people/{personId}/media

**Operation ID:** `libraryGetPeoplePersonMedia`

**Summary:** Get media for a person

Get all the media for a single actor.

#### Parameters

- **`personId`** (path) **(required)** - string
  Either the PMS tag `id` of the person or `tagKey` of the actor.  Note the `tagKey` is the hex portion of the plex guid for the actor

#### Responses

**200** - OK

Content-Type: `application/json`

**404** - 

---

### GET /library/randomArtwork

**Operation ID:** `libraryGetRandomArtwork`

**Summary:** Get random artwork

Get random artwork across sections.  This is commonly used for a screensaver.

This retrieves 100 random artwork paths in the specified sections and returns them.  Restrictions are put in place to not return artwork for items the user is not allowed to access.  Artwork will be for Movies, Shows, and Artists only.


#### Parameters

- **`sections`** (query) - array
  The sections for which to fetch artwork.

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /library/sections/all

**Operation ID:** `libraryGetSections`

**Summary:** Get library sections (main Media Provider Only)

A library section (commonly referred to as just a library) is a collection of media. Libraries are typed, and depending on their type provide either a flat or a hierarchical view of the media. For example, a music library has an artist > albums > tracks structure, whereas a movie library is flat.
Libraries have features beyond just being a collection of media; for starters, they include information about supported types, filters and sorts. This allows a client to provide a rich interface around the media (e.g. allow sorting movies by release year).

#### Responses

**200** - OK

Content-Type: `application/json`

---

### POST /library/sections/all

**Operation ID:** `libraryPostSection`

**Summary:** Add a library section

Add a new library section to the server

#### Parameters

- **`name`** (query) **(required)** - string
  The name of the new section
- **`type`** (query) **(required)** - integer
  The type of library section
- **`scanner`** (query) - string
  The scanner this section should use
- **`agent`** (query) **(required)** - string
  The agent this section should use for metadata
- **`metadataAgentProviderGroupId`** (query) - string
  The agent group id for this section
- **`language`** (query) **(required)** - string
  The language of this section
- **`locations`** (query) - array
  The locations on disk to add to this section
- **`prefs`** (query) - object
  The preferences for this section
- **`relative`** (query) - integer
  If set, paths are relative to `Media Upload` path
- **`importFromiTunes`** (query) - integer
  If set, import media from iTunes.

#### Responses

**200** - 

**400** - Section cannot be created due to bad parameters in request

Content-Type: `text/html`

---

### DELETE /library/sections/all/refresh

**Operation ID:** `libraryDeleteSectionsAllRefresh`

**Summary:** Stop refresh

Stop all refreshes across all sections

#### Responses

**200** - 

---

### GET /library/sections/prefs

**Operation ID:** `libraryGetSectionsPrefs`

**Summary:** Get section prefs

Get a section's preferences for a metadata type

#### Parameters

- **`type`** (query) **(required)** - integer
  The metadata type
- **`agent`** (query) - string
  The metadata agent in use

#### Responses

**200** - 

**400** - type not provided or not an integer

Content-Type: `text/html`

---

### POST /library/sections/refresh

**Operation ID:** `libraryPostSectionsRefresh`

**Summary:** Refresh all sections

Tell PMS to refresh all section metadata

#### Parameters

- **`force`** (query) - boolean
  Force refresh of metadata

#### Responses

**200** - 

**503** - Server cannot refresh a music library when not signed in

Content-Type: `text/html`

---

### GET /library/sections/{sectionId}

**Operation ID:** `librarySectionGetSection`

**Summary:** Get a library section by id

Returns details for the library. This can be thought of as an interstitial endpoint because it contains information about the library, rather than content itself. It often contains a list of `Directory` metadata objects: These used to be used by clients to build a menuing system.

#### Parameters

- **`sectionId`** (path) **(required)** - string
  The section identifier
- **`includeDetails`** (query) - integer
  Whether or not to include details for a section (types, filters, and sorts). Only exists for backwards compatibility, media providers other than the server libraries have it on always.

#### Responses

**200** - OK

Content-Type: `application/json`

---

### DELETE /library/sections/{sectionId}

**Operation ID:** `libraryDeleteSection`

**Summary:** Delete a library section

Delete a library section by id

#### Parameters

- **`sectionId`** (path) **(required)** - string
  The section identifier
- **`async`** (query) - integer
  If set, response will return an activity with the actual deletion process.  Otherwise request will return when deletion is complete

#### Responses

**200** - 

---

### PUT /library/sections/{sectionId}

**Operation ID:** `librarySectionPutSection`

**Summary:** Edit a library section

Edit a library section by id setting parameters

#### Parameters

- **`sectionId`** (path) **(required)** - string
  The section identifier
- **`name`** (query) - string
  The name of the new section
- **`scanner`** (query) - string
  The scanner this section should use
- **`agent`** (query) **(required)** - string
  The agent this section should use for metadata
- **`metadataAgentProviderGroupId`** (query) - string
  The agent group id for this section
- **`language`** (query) - string
  The language of this section
- **`locations`** (query) - array
  The locations on disk to add to this section
- **`prefs`** (query) - object
  The preferences for this section

#### Responses

**200** - 

**400** - Section cannot be created due to bad parameters in request

Content-Type: `text/html`

---

### PUT /library/sections/{sectionId}/all

**Operation ID:** `librarySectionPutAll`

**Summary:** Set the fields of the filtered items

This endpoint takes an large possible set of values.  Here are some examples.
- **Parameters, extra documentation**
  - artist.title.value
      - When used with track, both artist.title.value and album.title.value need to be specified
  - title.value usage
      - Summary
          - Tracks always rename and never merge
          - Albums and Artists
              - if single item and item without title does not exist, it is renamed.
              - if single item and item with title does exist they are merged.
              - if multiple they are always merged.
      - Tracks
          - Works as expected will update the track's title
          - Single track:    `/library/sections/{id}/all?type=10&id=42&title.value=NewName`
          - Multiple tracks: `/library/sections/{id}/all?type=10&id=42,43,44&title.value=NewName`
          - All tracks:      `/library/sections/{id}/all?type=10&title.value=NewName`
      - Albums
          - Functionality changes depending on the existence of an album with the same title
          - Album exists
              - Single album: `/library/sections/{id}/all?type=9&id=42&title.value=Album 2`
                  - Album with id 42 is merged into album titled "Album 2"
              - Multiple/All albums: `/library/sections/{id}/all?type=9&title.value=Moo Album`
                  - All albums are merged into the existing album titled "Moo Album"
          - Album does not exist
              - Single album: `/library/sections/{id}/all?type=9&id=42&title.value=NewAlbumTitle`
                  - Album with id 42 has title modified to "NewAlbumTitle"
              - Multiple/All albums: `/library/sections/{id}/all?type=9&title.value=NewAlbumTitle`
                  - All albums are merged into a new album with title="NewAlbumTitle"
      - Artists
          - Functionaly changes depending on the existence of an artist with the same title.
          - Artist exists
              - Single artist: `/library/sections/{id}/all?type=8&id=42&title.value=Artist 2`
                  - Artist with id 42 is merged into existing artist titled "Artist 2"
              - Multiple/All artists: `/library/sections/{id}/all?type=8&title.value=Artist 3`
                  - All artists are merged into the existing artist titled "Artist 3"
          - Artist does not exist
              - Single artist: `/library/sections/{id}/all?type=8&id=42&title.value=NewArtistTitle`
                  - Artist with id 42 has title modified to "NewArtistTitle"
              - Multiple/All artists: `/library/sections/{id}/all?type=8&title.value=NewArtistTitle`
                  - All artists are merged into a new artist with title="NewArtistTitle"

- **Notes**
    - Technically square brackets are not allowed in an URI except the Internet Protocol Literal Address
    - RFC3513: A host identified by an Internet Protocol literal address, version 6 [RFC3513] or later, is distinguished by enclosing the IP literal within square brackets ("[" and "]"). This is the only place where square bracket characters are allowed in the URI syntax.
    - Escaped square brackets are allowed, but don't render well

#### Parameters

- **`sectionId`** (path) **(required)** - string
  The id of the section
- **`type`** (query) - string
  
- **`filters`** (query) - string
  The filters to apply to determine which items should be modified
- **`field.value`** (query) - string
  Set the specified field to a new value
- **`field.locked`** (query) - integer
  Set the specified field to locked (or unlocked if set to 0)
- **`title.value`** (query) - string
  This field is treated specially by albums or artists and may be used for implicit reparenting.
- **`artist.title.value`** (query) - string
  Reparents set of Tracks or Albums - used with album.title.* in the case of tracks
- **`artist.title.id`** (query) - string
  Reparents set of Tracks or Albums - used with album.title.* in the case of tracks
- **`album.title.value`** (query) - string
  Reparents set of Tracks - Must be used in conjunction with artist.title.value or id
- **`album.title.id`** (query) - string
  Reparents set of Tracks - Must be used in conjunction with artist.title.value or id
- **`tagtype[idx].tag.tag`** (query) - string
  Creates tag and associates it with each item in the set. - [idx] links this and the next parameters together
- **`tagtype[idx].tagging.object`** (query) - string
  Here `object` may be text/thumb/art/theme - Optionally used in conjunction with tag.tag, to update association info across the set.
- **`tagtype[].tag.tag-`** (query) - string
  Remove comma separated tags from the set of items
- **`tagtype[].tag`** (query) - string
  Remove associations of this type (e.g. genre) from the set of items

#### Responses

**200** - 

**400** - The set of parameters are inconsistent or invalid values

Content-Type: `text/html`

**404** - A required item could not be found

Content-Type: `text/html`

**409** - Rename of a collection to a name that's already taken

Content-Type: `text/html`

---

### PUT /library/sections/{sectionId}/analyze

**Operation ID:** `librarySectionPutAnalyze`

**Summary:** Analyze a section

Start analysis of all items in a section.  If BIF generation is enabled, this will also be started on this section

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  Section identifier

#### Responses

**200** - 

---

### GET /library/sections/{sectionId}/autocomplete

**Operation ID:** `librarySectionGetAutocomplete`

**Summary:** Get autocompletions for search

The field to autocomplete on is specified by the {field}.query parameter. For example `genre.query` or `title.query`.
Returns a set of items from the filtered items whose {field} starts with {field}.query.  In the results, a {field}.queryRange will be present to express the range of the match

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  Section identifier
- **`type`** (query) - integer
  Item type
- **`field.query`** (query) - string
  The "field" stands in for any field, the value is a partial string for matching
- **``** () - string
  

#### Responses

**200** - OK

Content-Type: `application/json`

**400** - A paramater is either invalid or missing

Content-Type: `text/html`

---

### GET /library/sections/{sectionId}/collections

**Operation ID:** `librarySectionGetCollections`

**Summary:** Get collections in a section

Get all collections in a section

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  Section identifier
- **``** () - string
  

#### Responses

**200** - OK

Content-Type: `application/json`

---

### DELETE /library/sections/{sectionId}/collection/{collectionId}

**Operation ID:** `librarySectionDeleteCollectionCollection`

**Summary:** Delete a collection

Delete a library collection from the PMS

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  Section identifier
- **`collectionId`** (path) **(required)** - integer
  Collection Id

#### Responses

**200** - 

**404** - Collection not found

Content-Type: `text/html`

---

### GET /library/sections/{sectionId}/common

**Operation ID:** `librarySectionGetCommon`

**Summary:** Get common fields for items

Represents a "Common" item. It contains only the common attributes of the items selected by the provided filter
Fields which are not common will be expressed in the `mixedFields` field

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  Section identifier
- **`type`** (query) - integer
  Item type
- **``** () - string
  

#### Responses

**200** - OK

Content-Type: `application/json`

**400** - 

**404** - 

---

### GET /library/sections/{sectionId}/composite/{updatedAt}

**Operation ID:** `librarySectionGetComposite`

**Summary:** Get a section composite image

Get a composite image of images in this section

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  Section identifier
- **`updatedAt`** (path) **(required)** - integer
  The update time of the image.  Used for busting cache.
- **``** () - string
  
- **``** () - string
  

#### Responses

**200** - 

---

### PUT /library/sections/{sectionId}/emptyTrash

**Operation ID:** `librarySectionPutEmptyTrash`

**Summary:** Empty section trash

Empty trash in the section, permanently deleting media/metadata for missing media

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  Section identifier

#### Responses

**200** - 

---

### GET /library/sections/{sectionId}/filters

**Operation ID:** `librarySectionGetFilters`

**Summary:** Get section filters

Get common filters on a section

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  Section identifier

#### Responses

**200** - The filters on the section

Content-Type: `application/json`

---

### GET /library/sections/{sectionId}/firstCharacters

**Operation ID:** `librarySectionGetFirstCharaters`

**Summary:** Get list of first characters

Get list of first characters in this section

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  Section identifier
- **`type`** (query) - integer
  The metadata type to filter on
- **`sort`** (query) - integer
  The metadata type to filter on
- **``** () - string
  

#### Responses

**200** - OK

Content-Type: `application/json`

---

### DELETE /library/sections/{sectionId}/indexes

**Operation ID:** `librarySectionDeleteIndexes`

**Summary:** Delete section indexes

Delete all the indexes in a section

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  Section identifier

#### Responses

**200** - 

---

### DELETE /library/sections/{sectionId}/intros

**Operation ID:** `librarySectionDeleteIntros`

**Summary:** Delete section intro markers

Delete all the intro markers in a section

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  Section identifier

#### Responses

**200** - 

---

### GET /library/sections/{sectionId}/prefs

**Operation ID:** `librarySectionGetPrefs`

**Summary:** Get section prefs

Get the prefs for a section by id and potentially overriding the agent

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  Section identifier
- **`agent`** (query) - string
  

#### Responses

**200** - OK

Content-Type: `application/json`

---

### PUT /library/sections/{sectionId}/prefs

**Operation ID:** `librarySectionPutPrefs`

**Summary:** Set section prefs

Set the prefs for a section by id

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  Section identifier
- **`prefs`** (query) **(required)** - object
  

#### Responses

**200** - 

---

### POST /library/sections/{sectionId}/refresh

**Operation ID:** `librarySectionPostRefresh`

**Summary:** Refresh section

Start a refresh of this section

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  Section identifier
- **`force`** (query) - integer
  Whether the update of metadata and items should be performed even if modification dates indicate the items have not change
- **`path`** (query) - string
  Restrict refresh to the specified path

#### Responses

**200** - 

---

### DELETE /library/sections/{sectionId}/refresh

**Operation ID:** `librarySectionDeleteRefresh`

**Summary:** Cancel section refresh

Cancel the refresh of a section

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  Section identifier

#### Responses

**200** - 

---

### GET /library/sections/{sectionId}/sorts

**Operation ID:** `librarySectionGetSorts`

**Summary:** Get a section sorts

Get the sort mechanisms available in a section

#### Parameters

- **`sectionId`** (path) **(required)** - integer
  Section identifier

#### Responses

**200** - OK

Content-Type: `application/json`

---

### GET /library/streams/{streamId}.{ext}

**Operation ID:** `libraryGetStreamsStream`

**Summary:** Get a stream

Get a stream (such a a sidecar subtitle stream)

#### Parameters

- **`streamId`** (path) **(required)** - integer
  The id of the stream
- **`ext`** (path) **(required)** - string
  The extension of the stream.  Required to fetch the `sub` portion of `idx`/`sub` subtitles
- **`encoding`** (query) - string
  The requested encoding for the subtitle (only used for text subtitles)
- **`format`** (query) - string
  The requested format for the subtitle to convert the subtitles to (only used for text subtitles)
- **`autoAdjustSubtitle`** (query) - integer
  Whether the server should attempt to automatically adjust the subtitle timestamps to match the media

#### Responses

**200** - The stream in the requested format.

**403** - The media is not accessible to the user

Content-Type: `text/html`

**404** - The stream doesn't exist or has no data

Content-Type: `text/html`

**501** - The stream is not a sidecar subtitle

Content-Type: `text/html`

---

### PUT /library/streams/{streamId}.{ext}

**Operation ID:** `libraryPutStreamsStream`

**Summary:** Set a stream offset

Set a stream offset in ms.  This may not be respected by all clients

#### Parameters

- **`streamId`** (path) **(required)** - integer
  The id of the stream
- **`ext`** (path) **(required)** - string
  This is not a part of this endpoint but documented here to satisfy OpenAPI
- **`offset`** (query) - integer
  The offest in ms

#### Responses

**200** - The stream in the requested format.

**400** - The stream doesn't exist

Content-Type: `text/html`

---

### DELETE /library/streams/{streamId}.{ext}

**Operation ID:** `libraryDeleteStreamsStream`

**Summary:** Delete a stream

Delete a stream.  Only applies to downloaded subtitle streams or a sidecar subtitle when media deletion is enabled.

#### Parameters

- **`streamId`** (path) **(required)** - integer
  The id of the stream
- **`ext`** (path) **(required)** - string
  This is not a part of this endpoint but documented here to satisfy OpenAPI

#### Responses

**200** - 

**403** - This user cannot delete this stream

Content-Type: `text/html`

**500** - The stream cannot be deleted

Content-Type: `text/html`

---

### GET /library/streams/{streamId}/loudness

**Operation ID:** `libraryGetStreamsStreamLoudness`

**Summary:** Get loudness about a stream

The the loudness of a stream in db, one number per line, one entry per 100ms

#### Parameters

- **`streamId`** (path) **(required)** - integer
  The id of the stream
- **`subsample`** (query) - integer
  Subsample result down to return only the provided number of samples

#### Responses

**200** - OK

Content-Type: `text/plain`

**403** - The media is not accessible to the user

Content-Type: `text/html`

**404** - The stream doesn't exist, or the loudness feature is not available on this PMS

Content-Type: `text/html`

---

### GET /library/streams/{streamId}/levels

**Operation ID:** `libraryGetStreamsStreamLevels`

**Summary:** Get loudness about a stream in json

The the loudness of a stream in db, one entry per 100ms

#### Parameters

- **`streamId`** (path) **(required)** - integer
  The id of the stream
- **`subsample`** (query) - integer
  Subsample result down to return only the provided number of samples

#### Responses

**200** - OK

Content-Type: `application/json`

**403** - 

**404** - 

---

### GET /library/tags

**Operation ID:** `libraryGetTags`

**Summary:** Get all library tags of a type

Get all library tags of a type

#### Parameters

- **`type`** (query) - integer
  The type of tags to fetch

#### Responses

**200** - OK

Content-Type: `application/json`

---

