# Transcoder



**Category:** General

---

### GET /photo/:/transcode

**Operation ID:** `imageTranscode`

**Summary:** Transcode an image

Transcode an image, possibly changing format or size

#### Parameters

- **`url`** (query) - string
  The source URL for the image to transcode.  Note, if this URL requires a token such as `X-Plex-Token`, it should be given as a query parameter to this url.
- **`format`** (query) - string
  The output format for the image; defaults to jpg
- **`width`** (query) - integer
  The desired width of the output image
- **`height`** (query) - integer
  The desired height of the output image
- **`quality`** (query) - integer
  The desired quality of the output.  -1 means the highest quality.  Defaults to -1
- **`background`** (query) - string
  The background color to apply before painting the image.  Only really applicable if image has transparency.  Defaults to none
- **`upscale`** (query) - integer
  Indicates if image should be upscaled to the desired width/height.  Defaults to false
- **`minSize`** (query) - integer
  Indicates if image should be scaled to fit the smaller dimension.  By default (false) the image is scaled to fit within the width/height specified but if this parameter is true, it will allow overflowing one dimension to fit the other.  Essentially it is making the width/height minimum sizes of the image or sizing the image to fill the entire width/height even if it overflows one dimension.
- **`rotate`** (query) - integer
  Obey the rotation values specified in EXIF data.  Defaults to true.
- **`blur`** (query) - integer
  Apply a blur to the image, Defaults to 0 (none)
- **`saturation`** (query) - integer
  Scale the image saturation by the specified percentage.  Defaults to 100
- **`opacity`** (query) - integer
  Render the image at the specified opacity percentage.  Defaults to 100
- **`chromaSubsampling`** (query) - integer
  Use the specified chroma subsambling.
  - 0: 411
  - 1: 420
  - 2: 422
  - 3: 444
Defaults to 3 (444)
- **`blendColor`** (query) - string
  The color to blend with the image.  Defaults to none

#### Responses

**200** - The resulting image

Content-Type: `image/jpeg`

**400** - 

**403** - 

**404** - 

---

### GET /{transcodeType}/:/transcode/universal/decision

**Operation ID:** `transcodeDecision`

**Summary:** Make a decision on media playback

Make a decision on media playback based on client profile, and requested settings such as bandwidth and resolution.

#### Parameters

- **``** () - string
  
- **``** () - string
  
- **`advancedSubtitles`** (query) - string
  Indicates how  incompatible advanced subtitles (such as ass/ssa) should be included: * 'burn' - Burn incompatible advanced text subtitles into the video stream * 'text' - Transcode incompatible advanced text subtitles to a compatible text format, even if some markup is lost

- **`audioBoost`** (query) - integer
  Percentage of original audio loudness to use when transcoding (100 is equivalent to original volume, 50 is half, 200 is double, etc)
- **`audioChannelCount`** (query) - integer
  Target video number of audio channels.
- **`autoAdjustQuality`** (query) - integer
  Indicates the client supports ABR.
- **`autoAdjustSubtitle`** (query) - integer
  Indicates if the server should adjust subtitles based on Voice Activity Data.
- **`directPlay`** (query) - integer
  Indicates the client supports direct playing the indicated content.
- **`directStream`** (query) - integer
  Indicates the client supports direct streaming the video of the indicated content.
- **`directStreamAudio`** (query) - integer
  Indicates the client supports direct streaming the audio of the indicated content.
- **`disableResolutionRotation`** (query) - integer
  Indicates if resolution should be adjusted for orientation.
- **`hasMDE`** (query) - integer
  Ignore client profiles when determining if direct play is possible. Only has an effect when directPlay=1 and both mediaIndex and partIndex are specified and neither are -1
- **`location`** (query) - string
  Network type of the client, can be used to help determine target bitrate.
- **`mediaBufferSize`** (query) - integer
  Buffer size used in playback (in KB). Clients should specify a lower bound if not known exactly. This value could make the difference between transcoding and direct play on bandwidth constrained networks.
- **`mediaIndex`** (query) - integer
  Index of the media to transcode. -1 or not specified indicates let the server choose.
- **`musicBitrate`** (query) - integer
  Target bitrate for audio only files (in kbps, used to transcode).
- **`offset`** (query) - number
  Offset from the start of the media (in seconds).
- **`partIndex`** (query) - integer
  Index of the part to transcode. -1 or not specified indicates the server should join parts together in a transcode
- **`path`** (query) - string
  Internal PMS path of the media to transcode.
- **`peakBitrate`** (query) - integer
  Maximum bitrate (in kbps) to use in ABR.
- **`photoResolution`** (query) - string
  Target photo resolution.
- **`protocol`** (query) - string
  Indicates the network streaming protocol to be used for the transcode session: * 'http' - include the file in the http response such as MKV streaming * 'hls' - hls stream (RFC 8216) * 'dash' - dash stream (ISO/IEC 23009-1:2022)

- **`secondsPerSegment`** (query) - integer
  Number of seconds to include in each transcoded segment
- **`subtitleSize`** (query) - integer
  Percentage of original subtitle size to use when burning subtitles (100 is equivalent to original size, 50 is half, ect)
- **`subtitles`** (query) - string
  Indicates how subtitles should be included: * 'auto' - Compute the appropriate subtitle setting automatically * 'burn' - Burn the selected subtitle; auto if no selected subtitle * 'none' - Ignore all subtitle streams * 'sidecar' - The selected subtitle should be provided as a sidecar * 'embedded' - The selected subtitle should be provided as an embedded stream * 'segmented' - The selected subtitle should be provided as a segmented stream

- **`videoBitrate`** (query) - integer
  Target video bitrate (in kbps).
- **`videoQuality`** (query) - integer
  Target photo quality.
- **`videoResolution`** (query) - string
  Target maximum video resolution.
- **`X-Plex-Client-Identifier`** (header) **(required)** - string
  Unique per client.
- **`X-Plex-Client-Profile-Extra`** (header) - string
  See [Profile Augmentations](#section/API-Info/Profile-Augmentations) .
- **`X-Plex-Client-Profile-Name`** (header) - string
  Which built in Client Profile to use in the decision. Generally should only be used to specify the Generic profile.
- **`X-Plex-Device`** (header) - string
  Device the client is running on
- **`X-Plex-Model`** (header) - string
  Model of the device the client is running on
- **`X-Plex-Platform`** (header) - string
  Client Platform
- **`X-Plex-Platform-Version`** (header) - string
  Client Platform Version
- **`X-Plex-Session-Identifier`** (header) - string
  Unique per client playback session.  Used if a client can playback multiple items at a time (such as a browser with multiple tabs)

#### Responses

**200** - OK

Content-Type: `application/json`

---

### POST /{transcodeType}/:/transcode/universal/fallback

**Operation ID:** `transcodeFallback`

**Summary:** Manually trigger a transcoder fallback

Manually trigger a transcoder fallback ex: HEVC to h.264 or hw to sw

#### Parameters

- **``** () - string
  
- **``** () - string
  

#### Responses

**200** - 

**404** - Session ID does not exist

Content-Type: `text/html`

**412** - Transcode could not fallback

Content-Type: `text/html`

**500** - Transcode failed to fallback

Content-Type: `text/html`

---

### GET /{transcodeType}/:/transcode/universal/start.*

**Operation ID:** `transcodeStart`

**Summary:** Start A Transcoding Session

Starts the transcoder and returns the corresponding streaming resource document.

#### Parameters

- **``** () - string
  
- **``** () - string
  
- **`advancedSubtitles`** (query) - string
  Indicates how  incompatible advanced subtitles (such as ass/ssa) should be included: * 'burn' - Burn incompatible advanced text subtitles into the video stream * 'text' - Transcode incompatible advanced text subtitles to a compatible text format, even if some markup is lost

- **`audioBoost`** (query) - integer
  Percentage of original audio loudness to use when transcoding (100 is equivalent to original volume, 50 is half, 200 is double, etc)
- **`audioChannelCount`** (query) - integer
  Target video number of audio channels.
- **`autoAdjustQuality`** (query) - integer
  Indicates the client supports ABR.
- **`autoAdjustSubtitle`** (query) - integer
  Indicates if the server should adjust subtitles based on Voice Activity Data.
- **`directPlay`** (query) - integer
  Indicates the client supports direct playing the indicated content.
- **`directStream`** (query) - integer
  Indicates the client supports direct streaming the video of the indicated content.
- **`directStreamAudio`** (query) - integer
  Indicates the client supports direct streaming the audio of the indicated content.
- **`disableResolutionRotation`** (query) - integer
  Indicates if resolution should be adjusted for orientation.
- **`hasMDE`** (query) - integer
  Ignore client profiles when determining if direct play is possible. Only has an effect when directPlay=1 and both mediaIndex and partIndex are specified and neither are -1
- **`location`** (query) - string
  Network type of the client, can be used to help determine target bitrate.
- **`mediaBufferSize`** (query) - integer
  Buffer size used in playback (in KB). Clients should specify a lower bound if not known exactly. This value could make the difference between transcoding and direct play on bandwidth constrained networks.
- **`mediaIndex`** (query) - integer
  Index of the media to transcode. -1 or not specified indicates let the server choose.
- **`musicBitrate`** (query) - integer
  Target bitrate for audio only files (in kbps, used to transcode).
- **`offset`** (query) - number
  Offset from the start of the media (in seconds).
- **`partIndex`** (query) - integer
  Index of the part to transcode. -1 or not specified indicates the server should join parts together in a transcode
- **`path`** (query) - string
  Internal PMS path of the media to transcode.
- **`peakBitrate`** (query) - integer
  Maximum bitrate (in kbps) to use in ABR.
- **`photoResolution`** (query) - string
  Target photo resolution.
- **`protocol`** (query) - string
  Indicates the network streaming protocol to be used for the transcode session: * 'http' - include the file in the http response such as MKV streaming * 'hls' - hls stream (RFC 8216) * 'dash' - dash stream (ISO/IEC 23009-1:2022)

- **`secondsPerSegment`** (query) - integer
  Number of seconds to include in each transcoded segment
- **`subtitleSize`** (query) - integer
  Percentage of original subtitle size to use when burning subtitles (100 is equivalent to original size, 50 is half, ect)
- **`subtitles`** (query) - string
  Indicates how subtitles should be included: * 'auto' - Compute the appropriate subtitle setting automatically * 'burn' - Burn the selected subtitle; auto if no selected subtitle * 'none' - Ignore all subtitle streams * 'sidecar' - The selected subtitle should be provided as a sidecar * 'embedded' - The selected subtitle should be provided as an embedded stream * 'segmented' - The selected subtitle should be provided as a segmented stream

- **`videoBitrate`** (query) - integer
  Target video bitrate (in kbps).
- **`videoQuality`** (query) - integer
  Target photo quality.
- **`videoResolution`** (query) - string
  Target maximum video resolution.
- **`X-Plex-Client-Identifier`** (header) **(required)** - string
  Unique per client.
- **`X-Plex-Client-Profile-Extra`** (header) - string
  See [Profile Augmentations](#section/API-Info/Profile-Augmentations) .
- **`X-Plex-Client-Profile-Name`** (header) - string
  Which built in Client Profile to use in the decision. Generally should only be used to specify the Generic profile.
- **`X-Plex-Device`** (header) - string
  Device the client is running on
- **`X-Plex-Model`** (header) - string
  Model of the device the client is running on
- **`X-Plex-Platform`** (header) - string
  Client Platform
- **`X-Plex-Platform-Version`** (header) - string
  Client Platform Version
- **`X-Plex-Session-Identifier`** (header) - string
  Unique per client playback session.  Used if a client can playback multiple items at a time (such as a browser with multiple tabs)

#### Responses

**200** - MPD file (see ISO/IEC 23009-1:2022), m3u8 file (see RFC 8216), or binary http stream

Content-Type: `text/html`

**400** - 

**403** - 

**404** - 

---

### GET /{transcodeType}/:/transcode/universal/subtitles

**Operation ID:** `transcodeSubtitles`

**Summary:** Transcode subtitles

Only transcode subtitle streams.

#### Parameters

- **``** () - string
  
- **``** () - string
  
- **`advancedSubtitles`** (query) - string
  Indicates how  incompatible advanced subtitles (such as ass/ssa) should be included: * 'burn' - Burn incompatible advanced text subtitles into the video stream * 'text' - Transcode incompatible advanced text subtitles to a compatible text format, even if some markup is lost

- **`audioBoost`** (query) - integer
  Percentage of original audio loudness to use when transcoding (100 is equivalent to original volume, 50 is half, 200 is double, etc)
- **`audioChannelCount`** (query) - integer
  Target video number of audio channels.
- **`autoAdjustQuality`** (query) - integer
  Indicates the client supports ABR.
- **`autoAdjustSubtitle`** (query) - integer
  Indicates if the server should adjust subtitles based on Voice Activity Data.
- **`directPlay`** (query) - integer
  Indicates the client supports direct playing the indicated content.
- **`directStream`** (query) - integer
  Indicates the client supports direct streaming the video of the indicated content.
- **`directStreamAudio`** (query) - integer
  Indicates the client supports direct streaming the audio of the indicated content.
- **`disableResolutionRotation`** (query) - integer
  Indicates if resolution should be adjusted for orientation.
- **`hasMDE`** (query) - integer
  Ignore client profiles when determining if direct play is possible. Only has an effect when directPlay=1 and both mediaIndex and partIndex are specified and neither are -1
- **`location`** (query) - string
  Network type of the client, can be used to help determine target bitrate.
- **`mediaBufferSize`** (query) - integer
  Buffer size used in playback (in KB). Clients should specify a lower bound if not known exactly. This value could make the difference between transcoding and direct play on bandwidth constrained networks.
- **`mediaIndex`** (query) - integer
  Index of the media to transcode. -1 or not specified indicates let the server choose.
- **`musicBitrate`** (query) - integer
  Target bitrate for audio only files (in kbps, used to transcode).
- **`offset`** (query) - number
  Offset from the start of the media (in seconds).
- **`partIndex`** (query) - integer
  Index of the part to transcode. -1 or not specified indicates the server should join parts together in a transcode
- **`path`** (query) - string
  Internal PMS path of the media to transcode.
- **`peakBitrate`** (query) - integer
  Maximum bitrate (in kbps) to use in ABR.
- **`photoResolution`** (query) - string
  Target photo resolution.
- **`protocol`** (query) - string
  Indicates the network streaming protocol to be used for the transcode session: * 'http' - include the file in the http response such as MKV streaming * 'hls' - hls stream (RFC 8216) * 'dash' - dash stream (ISO/IEC 23009-1:2022)

- **`secondsPerSegment`** (query) - integer
  Number of seconds to include in each transcoded segment
- **`subtitleSize`** (query) - integer
  Percentage of original subtitle size to use when burning subtitles (100 is equivalent to original size, 50 is half, ect)
- **`subtitles`** (query) - string
  Indicates how subtitles should be included: * 'auto' - Compute the appropriate subtitle setting automatically * 'burn' - Burn the selected subtitle; auto if no selected subtitle * 'none' - Ignore all subtitle streams * 'sidecar' - The selected subtitle should be provided as a sidecar * 'embedded' - The selected subtitle should be provided as an embedded stream * 'segmented' - The selected subtitle should be provided as a segmented stream

- **`videoBitrate`** (query) - integer
  Target video bitrate (in kbps).
- **`videoQuality`** (query) - integer
  Target photo quality.
- **`videoResolution`** (query) - string
  Target maximum video resolution.
- **`X-Plex-Client-Identifier`** (header) **(required)** - string
  Unique per client.
- **`X-Plex-Client-Profile-Extra`** (header) - string
  See [Profile Augmentations](#section/API-Info/Profile-Augmentations) .
- **`X-Plex-Client-Profile-Name`** (header) - string
  Which built in Client Profile to use in the decision. Generally should only be used to specify the Generic profile.
- **`X-Plex-Device`** (header) - string
  Device the client is running on
- **`X-Plex-Model`** (header) - string
  Model of the device the client is running on
- **`X-Plex-Platform`** (header) - string
  Client Platform
- **`X-Plex-Platform-Version`** (header) - string
  Client Platform Version
- **`X-Plex-Session-Identifier`** (header) - string
  Unique per client playback session.  Used if a client can playback multiple items at a time (such as a browser with multiple tabs)

#### Responses

**200** - Transcoded subtitle file

Content-Type: `text/srt`

**400** - 

**403** - 

**404** - 

---

