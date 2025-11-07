# API Schemas

This document contains the data model schemas used throughout the Plex API.

---

## MediaContainer

**Type:** `object`

### Properties

- **`identifier`** - `string`

- **`size`** - `integer`

- **`totalSize`** - `integer`
  The total size of objects available.  Also provided in the X-Plex-Container-Total-Size header

- **`offset`** - `integer`
  The offset of where this container page starts among the total objects available.  Also provided in the X-Plex-Container-Start header

---

## serverConfiguration

**Type:** `object`

### Composed of (allOf)

- [MediaContainer](#mediacontainer)
---

## mediaContainerWithSettings

**Type:** `object`

### Properties

- **`MediaContainer`** - `any`

---

## stream

`Stream` represents a particular stream from a media item, such as the video stream, audio stream, or subtitle stream. The stream may either be part of the file represented by the parent `Part` or, especially for subtitles, an external file. The stream contains more detailed information about the specific stream. For example, a video may include the `aspectRatio` at the `Media` level, but detailed information about the video stream like the color space will be included on the `Stream` for the video stream.  Note that photos do not have streams (mostly as an optimization).


**Type:** `object`

### Properties

- **`audioChannelLayout`** - `any`

- **`bitDepth`** - `integer`

- **`bitrate`** - `integer`

- **`canAutoSync`** - `boolean`
  For subtitle streams only. If `true` then the server can attempt to automatically sync the subtitle timestamps with the video.

- **`chromaLocation`** - `any`

- **`chromaSubsampling`** - `any`

- **`codec`** - `any`
  The codec of the stream, such as `h264` or `aac`

- **`colorPrimaries`** - `any`

- **`colorRange`** - `any`

- **`colorSpace`** - `any`

- **`colorTrc`** - `any`

- **`default`** - `boolean`

- **`displayTitle`** - `any`
  A friendly name for the stream, often comprised of the language and codec information

- **`frameRate`** - `number`

- **`hasScalingMatrix`** - `any`

- **`height`** - `integer`

- **`id`** - `integer`

- **`index`** - `integer`
  If the stream is part of the `Part` and not an external resource, the index of the stream within that part

- **`key`** - `any`
  If the stream is independently streamable, the key from which it can be streamed

- **`language`** - `any`

- **`languageCode`** - `any`
  The three character language code for the stream contents

- **`level`** - `integer`

- **`profile`** - `any`

- **`refFrames`** - `integer`

- **`samplingRate`** - `integer`

- **`selected`** - `boolean`

- **`streamIdentifier`** - `integer`

- **`streamType`** - `integer`
  A number indicating the type of the stream. `1` for video, `2` for audio, `3` for subtitles, `4` for lyrics

- **`width`** - `integer`

---

## part

`Part` represents a particular file or "part" of a media item. The part is the playable unit of the media hierarchy. Suppose that a movie library contains a movie that is broken up into files, reminiscent of a movie split across two BDs. The metadata item represents information about the movie, the media item represents this instance of the movie at this resolution and quality, and the part items represent the two playable files.  If another media were added which contained the joining of these two parts transcoded down to a lower resolution, then this metadata would contain 2 medias, one with 2 parts and one with 1 part.


**Type:** `object`

### Properties

- **`audioProfile`** - `any`

- **`container`** - `any`
  The container of the media file, such as `mp4` or `mkv`

- **`duration`** - `integer`
  The duration of the media item, in milliseconds

- **`file`** - `any`
  The local file path at which the part is stored on the server

- **`has64bitOffsets`** - `boolean`

- **`id`** - `integer`

- **`key`** - `any`
  The key from which the media can be streamed

- **`optimizedForStreaming`** - `boolean`

- **`size`** - `integer`
  The size of the media, in bytes

- **`videoProfile`** - `any`

- **`Stream`** - `array`

---

## media

`Media` represents an one or more media files (parts) and is a child of a metadata item. There aren't necessarily any guaranteed attributes on media elements since the attributes will vary based on the type. The possible attributes are not documented here, but they typically have self-evident names. High-level media information that can be used for badging and flagging, such as `videoResolution` and codecs, is included on the media element.


**Type:** `object`

### Properties

- **`aspectRatio`** - `number`

- **`audioChannels`** - `integer`

- **`audioCodec`** - `any`

- **`audioProfile`** - `any`

- **`bitrate`** - `integer`

- **`container`** - `any`

- **`duration`** - `integer`

- **`has64bitOffsets`** - `boolean`

- **`hasVoiceActivity`** - `boolean`

- **`height`** - `integer`

- **`id`** - `integer`

- **`optimizedForStreaming`** - `boolean`

- **`videoCodec`** - `any`

- **`videoFrameRate`** - `any`

- **`videoProfile`** - `any`

- **`videoResolution`** - `any`

- **`width`** - `integer`

- **`Part`** - `array`

---

## image

Images such as movie posters and background artwork are represented by Image elements.


**Type:** `object`

### Properties

- **`type`** - `string`
  Describes both the purpose and intended presentation of the image.

- **`url`** - `string`
  The relative path or absolute url for the image.

- **`alt`** - `string`
  Title to use for accessibility.

---

## tag

A variety of extra information about a metadata item is included as tags. These tags use their own element names such as `Genre`, `Writer`, `Directory`, and `Role`. Individual tag types may introduce their own extra attributes.


**Type:** `object`

### Properties

- **`id`** - `integer`

- **`tag`** - `any`
  The value of the tag (the name)

- **`tagKey`** - `any`
  Plex identifier for this tag which can be used to fetch additional information from plex.tv

- **`tagType`** - `integer`

- **`filter`** - `any`
  A filter parameter that can be used to query for more content that matches this tag value.

- **`role`** - `any`
  The role this actor played

- **`thumb`** - `any`

- **`context`** - `string`

- **`ratingKey`** - `string`

- **`confidence`** - `number`
  Measure of the confidence of an automatic tag

---

## directory

**Type:** `object`

### Properties

- **`hubKey`** - `string`

- **`key`** - `string`

- **`title`** - `string`

- **`thumb`** - `string`

- **`art`** - `string`

- **`share`** - `integer`

- **`hasStoreServices`** - `boolean`

- **`hasPrefs`** - `boolean`

- **`identifier`** - `string`

- **`titleBar`** - `string`

- **`lastAccessedAt`** - `integer`

- **`type`** - `string`

- **`content`** - `boolean`

- **`filter`** - `string`

- **`Pivot`** - `array`

---

## filter

**Type:** `object`

### Composed of (allOf)

- [directory](#directory)
---

## sort

**Type:** `object`

### Composed of (allOf)

- [directory](#directory)
---

## metadata

Items in a library are referred to as "metadata items." These metadata items are distinct from "media items" which represent actual instances of media that can be consumed. Consider a TV library that has a single video file in it for a particular episode of a show. The library has a single media item, but it has three metadata items: one for the show, one for the season, and one for the episode. Consider a movie library that has two video files in it: the same movie, but two different resolutions. The library has a single metadata item for the movie, but that metadata item has two media items, one for each resolution. Additionally a "media item" will have one or more "media parts" where the the parts are intended to be watched together, such as a CD1 and CD2 parts of the same movie.

Note that when a metadata item has multiple media items, those media items should be isomorphic. That is, a 4K version and 1080p version of a movie are different versions of the same movie. They have the same duration, same summary, same rating, etc. and they can generally be considered interchangeable. A theatrical release vs. director's cut vs. unrated version on the other hand would be separate metadata items.

Metadata items can often live in a hierarchy with relationships between them.  For example, the metadata item for an episodes is associated with a season metadata item which is associated with a show metadata item.  A similar hierarchy exists with track, album, and artist and photos and photo album.  The relationships may be expressed via relative terms and absolute terms.  For example, "leaves" refer to metadata items which has associated media (there is no media for a season nor show).  A show will have "children" in the form of seasons and a season will have "children" in the form of episodes and episodes have "parent" in the form of a season which has a "parent" in the form of a show.  Similarly, a show has "grandchildren" in the form of episodse and an episode has a "grandparent" in the form of a show.


**Type:** `object`

### Properties

- **`type`** - `any`
  The type of the video item, such as `movie`, `episode`, or `clip`.

- **`subtype`** - `any`
  The subtype of the video item, such as `photo` when the video item is in a photo library

- **`key`** - `any`
  The key at which the item's details can be fetched.  In many cases a metadata item may be passed without all the details (such as in a hub) and this key corresponds to the endpoint to fetch additional details.

- **`ratingKey`** - `any`
  This is the opaque string to be passed into timeline, scrobble, and rating endpoints to identify them.  While it often appears to be numeric, this is not guaranteed.

- **`title`** - `any`
  The title of the item (e.g. “300” or “The Simpsons”)

- **`titleSort`** - `any`
  Whene present, this is the string used for sorting the item. It's usually the title with any leading articles removed (e.g. “Simpsons”).

- **`originalTitle`** - `any`
  When present, used to indicate an item's original title, e.g. a movie's foreign title.

- **`year`** - `integer`
  When present, the year associated with the item's release (e.g. release year for a movie).

- **`index`** - `integer`
  When present, this represents the episode number for episodes, season number for seasons, or track number for audio tracks.

- **`absoluteIndex`** - `integer`
  When present, contains the disc number for a track on multi-disc albums.

- **`originallyAvailableAt`** - `any`
  When present, in the format YYYY-MM-DD [HH:MM:SS] (the hours/minutes/seconds part is not always present). The air date, or a higher resolution release date for an item, depending on type. For example, episodes usually have air date like 1979-08-10 (we don't use epoch seconds because media existed prior to 1970). In some cases, recorded over-the-air content has higher resolution air date which includes a time component. Albums and movies may have day-resolution release dates as well.

- **`duration`** - `integer`
  When present, the duration for the item, in units of milliseconds.

- **`summary`** - `any`
  When present, the extended textual information about the item (e.g. movie plot, artist biography, album review).

- **`tagline`** - `any`
  When present, a pithy one-liner about the item (usually only seen for movies).

- **`thumb`** - `any`
  When present, the URL for the poster or thumbnail for the item. When available for types like movie, it will be the poster graphic, but fall-back to the extracted media thumbnail.

- **`art`** - `any`
  When present, the URL for the background artwork for the item.

- **`banner`** - `any`
  When present, the URL for a banner graphic for the item.

- **`hero`** - `any`
  When present, the URL for a hero image for the item.

- **`theme`** - `any`
  When present, the URL for theme music for the item (usually only for TV shows).

- **`composite`** - `any`
  When present, the URL for a composite image for descendent items (e.g. photo albums or playlists).

- **`studio`** - `any`
  When present, the studio or label which produced an item (e.g. movie studio for movies, record label for albums).

- **`contentRating`** - `any`
  If known, the content rating (e.g. MPAA) for an item.

- **`rating`** - `number`
  When present, the rating for the item. The exact meaning and representation depends on where the rating was sourced from.

- **`ratingImage`** - `any`
  When present, indicates an image to be shown with the rating. This is passed back as a small set of defined URI values, e.g. rottentomatoes://image.rating.rotten.

- **`audienceRating`** - `number`
  Some rating systems separate reviewer ratings from audience ratings

- **`audienceRatingImage`** - `any`
  A URI representing the image to be shown with the audience rating (e.g. rottentomatoes://image.rating.spilled).

- **`userRating`** - `number`
  When the user has rated an item, this contains the user rating

- **`viewOffset`** - `integer`
  When a user is in the process of viewing or listening to this item, this attribute contains the current offset, in units of milliseconds.

- **`viewCount`** - `integer`
  When a users has completed watched or listened to an item, this attribute contains the number of consumptions.

- **`lastViewedAt`** - `integer`
  When a user has watched or listened to an item, this contains a timestamp (epoch seconds) for that last consumption time.

- **`addedAt`** - `integer`
  In units of seconds since the epoch, returns the time at which the item was added to the library.

- **`updatedAt`** - `integer`
  In units of seconds since the epoch, returns the time at which the item was last changed (e.g. had its metadata updated).

- **`chapterSource`** - `any`
  When present, indicates the source for the chapters in the media file. Can be media (the chapters were embedded in the media itself), agent (a metadata agent computed them), or mixed (a combination of the two).

- **`primaryExtraKey`** - `any`
  Indicates that the item has a primary extra; for a movie, this is a trailer, and for a music track it is a music video. The URL points to the metadata details endpoint for the item.

- **`skipChildren`** - `boolean`
  When found on a show item, indicates that the children (seasons) should be skipped in favor of the grandchildren (episodes). Useful for mini-series, etc.

- **`skipParent`** - `boolean`
  When present on an episode or track item, indicates parent should be skipped in favor of grandparent (show).

- **`leafCount`** - `integer`
  For shows and seasons, contains the number of total episodes.

- **`viewedLeafCount`** - `integer`
  For shows and seasons, contains the number of viewed episodes.

- **`parentKey`** - `string`
  The `key` of the parent

- **`grandparentKey`** - `string`
  The `key` of the grandparent

- **`parentRatingKey`** - `string`
  The `ratingKey` of the parent

- **`grandparentRatingKey`** - `string`
  The `ratingKey` of the grandparent

- **`parentThumb`** - `string`
  The `thumb` of the parent

- **`grandparentThumb`** - `string`
  The `thumb` of the grandparent

- **`grandparentArt`** - `string`
  The `art` of the grandparent

- **`parentHero`** - `string`
  The `hero` of the parent

- **`grandparentHero`** - `string`
  The `hero` of the grandparent

- **`grandparentTheme`** - `string`
  The `theme` of the grandparent

- **`parentTitle`** - `string`
  The `title` of the parent

- **`grandparentTitle`** - `string`
  The `title` of the grandparent

- **`parentIndex`** - `integer`
  The `index` of the parent

- **`secondary`** - `boolean`
  Used by old clients to provide nested menus allowing for primative (but structured) navigation.

- **`prompt`** - `string`
  Prompt to give the user for this directory (such as `Search Movies`)

- **`search`** - `boolean`
  Indicates this is a search directory

- **`ratingCount`** - `integer`
  Number of ratings under this metadata

- **`Media`** - `array`

- **`Image`** - `array`

- **`Genre`** - `array`

- **`Country`** - `array`

- **`Guid`** - `array`

- **`Rating`** - `array`

- **`Director`** - `array`

- **`Writer`** - `array`

- **`Role`** - `array`

- **`Autotag`** - `array`

- **`Filter`** - `array`
  Typically only seen in metadata at a library's top level

- **`Sort`** - `array`
  Typically only seen in metadata at a library's top level

---

## properties-MediaContainer

**Type:** `object`

### Properties

- **`identifier`** - `string`

- **`size`** - `integer`

- **`totalSize`** - `integer`
  The total size of objects available.  Also provided in the X-Plex-Container-Total-Size header

- **`offset`** - `integer`
  The offset of where this container page starts among the total objects available.  Also provided in the X-Plex-Container-Start header

- **`Metadata`** - `array`

---

## mediaContainerWithDecision

`MediaContainer` is commonly found as the root of a response and is a pretty generic container. Common attributes include `identifier` and things related to paging (`offset`, `size`, `totalSize`).

It is also common for a `MediaContainer` to contain attributes "hoisted" from its children. If every element in the container would have had the same attribute, then that attribute can be present on the container instead of being repeated on every element. For example, an album's list of tracks might include `parentTitle` on the container since all of the tracks have the same album title. A container may have a `source` attribute when all of the items came from the same source. Generally speaking, when looking for an attribute on an item, if the attribute wasn't found then the container should be checked for that attribute as well.


**Type:** `object`

### Properties

- **`MediaContainer`** - `any`

---

## hub

**Type:** `object`

### Properties

- **`context`** - `string`

- **`hubIdentifier`** - `string`
  A unique identifier for the hub

- **`hubKey`** - `string`
  A key at which the exact content currently displayed can be fetched again. This is particularly important when a hub is marked as random and requesting the `key` may get different results. It's otherwise optional.


- **`key`** - `string`
  The key at which all of the content for this hub can be retrieved

- **`more`** - `boolean`
  "A boolean indicating that the hub contains more than what's included in the current response."


- **`size`** - `integer`

- **`totalSize`** - `integer`

- **`type`** - `string`
  The type of the items contained in this hub, or possibly `mixed` if there are multiple types

- **`subtype`** - `string`
  The subtype of the items contained in this hub, or possibly `mixed` if there are multiple types

- **`promoted`** - `boolean`
  Indicating if the hub should be promoted to the user's homescreen

- **`random`** - `boolean`
  Indicating that the contents of the hub may change on each request

- **`style`** - `string`
  A suggestion on how this hub's contents might be displayed by a client. Some examples include `hero`, `list`, `spotlight`, and `upsell`

- **`title`** - `string`
  A title for this grouping of content

- **`Metadata`** - `array`

---

## mediaContainerWithMetadata

`MediaContainer` is commonly found as the root of a response and is a pretty generic container. Common attributes include `identifier` and things related to paging (`offset`, `size`, `totalSize`).

It is also common for a `MediaContainer` to contain attributes "hoisted" from its children. If every element in the container would have had the same attribute, then that attribute can be present on the container instead of being repeated on every element. For example, an album's list of tracks might include `parentTitle` on the container since all of the tracks have the same album title. A container may have a `source` attribute when all of the items came from the same source. Generally speaking, when looking for an attribute on an item, if the attribute wasn't found then the container should be checked for that attribute as well.


**Type:** `object`

### Properties

- **`MediaContainer`** - `object`

---

## items

**Type:** `object`

### Composed of (allOf)

- [metadata](#metadata)
---

## mediaContainerWithNestedMetadata

**Type:** `object`

### Properties

- **`MediaContainer`** - `any`

---

## mediaContainerWithArtwork

**Type:** `object`

### Properties

- **`MediaContainer`** - `any`

---

## mediaContainer

`MediaContainer` is commonly found as the root of a response and is a pretty generic container. Common attributes include `identifier` and things related to paging (`offset`, `size`, `totalSize`).

It is also common for a `MediaContainer` to contain attributes "hoisted" from its children. If every element in the container would have had the same attribute, then that attribute can be present on the container instead of being repeated on every element. For example, an album's list of tracks might include `parentTitle` on the container since all of the tracks have the same album title. A container may have a `source` attribute when all of the items came from the same source. Generally speaking, when looking for an attribute on an item, if the attribute wasn't found then the container should be checked for that attribute as well.


**Type:** `object`

### Properties

- **`MediaContainer`** - `object`

---

## allowSync

**Type:** `boolean`

---

## art

**Type:** `string`

---

## thumb

**Type:** `string`

---

## key

**Type:** `string`

---

## type

**Type:** `string`

---

## title

**Type:** `string`

---

## content

**Type:** `boolean`

---

## librarySection

**Type:** `object`

### Properties

- **`allowSync`** - `boolean`

- **`art`** - `any`

- **`composite`** - `string`

- **`filters`** - `boolean`
  Indicates whether this section has filtering capabilities

- **`refreshing`** - `boolean`
  Indicates whether this library section is currently scanning

- **`thumb`** - `any`

- **`key`** - `any`

- **`type`** - `any`

- **`title`** - `any`

- **`agent`** - `string`

- **`scanner`** - `string`

- **`language`** - `string`

- **`updatedAt`** - `integer`

- **`createdAt`** - `integer`

- **`scannedAt`** - `integer`

- **`content`** - `any`

- **`directory`** - `boolean`

- **`contentChangedAt`** - `integer`

- **`hidden`** - `boolean`

- **`Location`** - `array`

---

## mediaContainerWithStatus_properties-MediaContainer

**Type:** `object`

### Composed of (allOf)

- [MediaContainer](#mediacontainer)
---

## Device-items

**Type:** `object`

### Properties

- **`key`** - `string`

- **`lastSeenAt`** - `integer`

- **`make`** - `string`

- **`model`** - `string`

- **`modelNumber`** - `string`

- **`protocol`** - `string`

- **`sources`** - `string`

- **`state`** - `string`

- **`status`** - `string`

- **`tuners`** - `string`

- **`uri`** - `string`

- **`uuid`** - `string`

- **`ChannelMapping`** - `array`

---

## channel

**Type:** `object`

### Properties

- **`identifier`** - `string`

- **`key`** - `string`

- **`channelVcn`** - `string`

- **`hd`** - `boolean`

- **`thumb`** - `string`

- **`title`** - `string`

- **`callSign`** - `string`

- **`language`** - `string`

---

## mediaContainerWithLineup

**Type:** `object`

### Properties

- **`MediaContainer`** - `any`

---

## Lineup-items

**Type:** `object`

### Properties

- **`uuid`** - `string`
  The uuid of this lineup

- **`type`** - `string`
  The type of this object (`lineup` in this case)

- **`title`** - `string`

- **`lineupType`** - `integer`
  - `-1`: N/A
- `0`: Over the air
- `1`: Cable
- `2`: Satellite
- `3`: IPTV
- `4`: Virtual


- **`location`** - `string`

---

## mediaContainerWithDevice

**Type:** `object`

### Properties

- **`MediaContainer`** - `any`

---

## mediaGrabOperation

A media grab opration represents a scheduled or active recording of media


**Type:** `object`

### Properties

- **`mediaSubscriptionID`** - `integer`

- **`mediaIndex`** - `integer`

- **`id`** - `string`

- **`key`** - `string`

- **`grabberIdentifier`** - `string`

- **`grabberProtocol`** - `string`

- **`percent`** - `number`

- **`currentSize`** - `integer`

- **`status`** - `string`

- **`provider`** - `string`

- **`Metadata`** - `any`

---

## mediaSubscription

A media subscription contains a representation of metadata desired to be recorded


**Type:** `object`

### Properties

- **`key`** - `string`

- **`type`** - `integer`
  The metadata type of the root item of the subscription

- **`targetLibrarySectionID`** - `integer`
  The library section id for where the item is to be recorded

- **`targetSectionLocationID`** - `integer`
  The library section location id for where the item is to be recorded

- **`createdAt`** - `integer`

- **`title`** - `string`

- **`storageTotal`** - `integer`
  Only included if `includeStorage` is specified

- **`durationTotal`** - `integer`
  Only included if `includeStorage` is specified

- **`airingsType`** - `string`

- **`librarySectionTitle`** - `string`

- **`locationPath`** - `string`

- **`Video`** - `any`
  Media Matching Hints

- **`Directory`** - `any`
  Media Matching Hints

- **`Playlist`** - `any`
  Media Matching Hints

- **`Setting`** - `array`

- **`MediaGrabOperation`** - `array`

---

## mediaContainerWithSubscription

**Type:** `object`

### Properties

- **`MediaContainer`** - `any`

---

## mediaContainerWithPlaylistMetadata

**Type:** `object`

### Properties

- **`MediaContainer`** - `any`

---

## directoryType

These represent the types of things found in this library, and for each one, a list of `Filter` and `Sort` objects. These can be used to build rich controls around a grid of media to allow filtering and organizing. Note that these filters and sorts are optional, and without them, the client won't render any filtering controls.


**Type:** `object`

### Properties

- **`key`** - `string`
  This provides the root endpoint returning the actual media list for the type.

- **`type`** - `string`
  This is the metadata type for the type (if a standard Plex type).

- **`title`** - `string`
  The title for for the content of this type (e.g. "Movies").

---

## Hub

**Type:** `object`

---

## Metadata

**Type:** `object`

---

## MediaContainerWithMetadata

**Type:** `object`

---

## Media

**Type:** `object`

---

## Part

**Type:** `object`

---

## Stream

**Type:** `object`

---

## Tag

**Type:** `object`

---

## ServerConfiguration

**Type:** `object`

---

## Directory

**Type:** `object`

---

## LibrarySection

**Type:** `object`

---

## DirectoryType

**Type:** `object`

---

## Filter

**Type:** `object`

---

## Sort

**Type:** `object`

---

## MediaSubscription

**Type:** `object`

---

## MediaGrabOperation

**Type:** `object`

---

## MediaContainerWithSubscription

**Type:** `object`

---

## MediaContainerWithDevice

**Type:** `object`

---

## MediaContainerWithLineup

**Type:** `object`

---

## MediaContainerWithPlaylistMetadata

**Type:** `object`

---

## MediaContainerWithArtwork

**Type:** `object`

---

## MediaContainerWithNestedMetadata

**Type:** `object`

---

## MediaContainerWithSettings

**Type:** `object`

---

