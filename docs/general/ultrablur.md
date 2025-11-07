# UltraBlur

Service provided to compute UltraBlur colors and images.

**Category:** General

---

### GET /services/ultrablur/colors

**Operation ID:** `ultraBlurGetColors`

**Summary:** Get UltraBlur Colors

Retrieves the four colors extracted from an image for clients to use to generate an ultrablur image.

#### Parameters

- **`url`** (query) - string
  Url for image which requires color extraction. Can be relative PMS library path or absolute url.

#### Responses

**200** - OK

Content-Type: `application/json`

**404** - The image url could not be found.

Content-Type: `text/html`

**500** - The server was unable to successfully extract the UltraBlur colors.

Content-Type: `text/html`

---

### GET /services/ultrablur/image

**Operation ID:** `ultraBlurGetImage`

**Summary:** Get UltraBlur Image

Retrieves a server-side generated UltraBlur image based on the provided color inputs. Clients should always call this via the photo transcoder endpoint.

#### Parameters

- **`topLeft`** (query) - string
  The base color (hex) for the top left quadrant.
- **`topRight`** (query) - string
  The base color (hex) for the top right quadrant.
- **`bottomRight`** (query) - string
  The base color (hex) for the bottom right quadrant.
- **`bottomLeft`** (query) - string
  The base color (hex) for the bottom left quadrant.
- **`width`** (query) - integer
  Width in pixels for the image.
- **`height`** (query) - integer
  Height in pixels for the image.
- **`noise`** (query) - integer
  Whether to add noise to the ouput image. Noise can reduce color banding with the gradients. Image sizes with noise will be larger.

#### Responses

**200** - OK

Content-Type: `image/png`

**400** - Requested width and height parameters are out of bounds (maximum 3840 x 2160)

Content-Type: `text/html`

---

