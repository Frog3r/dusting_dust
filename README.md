# 🌌 NASA Image Archive Viewer

An interactive web application that allows users to **explore NASA’s image database** or browse **local mission archives** with zoomable deep-space visuals powered by **OpenSeadragon**.  

This project lets you switch between **Local Archive Mode** (using provided images) and **NASA Database Mode** (using NASA’s public Images API).  

You can see a live demo in: dusting-dust-nasa.github.io

---

## 🚀 Features

- **Two modes:**
  - 🛰️ *Local Archive Mode* – Explore included mission images.
  - 🌍 *NASA Database Mode* – Search NASA’s vast online image library.
- **Interactive Deep Zoom** – Zoom and pan on astronomical images using OpenSeadragon.
- **Live Coordinates Display** – Shows X/Y coordinates and zoom level dynamically.
- **Responsive Gallery Interface** – Clean design with easy image browsing.
- **Keyboard Shortcuts**
  - `Esc` → Exit viewer  
  - `+ / -` → Zoom in/out  
  - `H` → Reset view  
  - `F` → Toggle fullscreen  

---


---

## ⚙️ Local Setup (Using Python 3)

You can easily preview and interact with the project locally by serving it with **Python’s built-in web server**.

### 🪄 Steps

1. **Clone or download** this repository to your computer:
   ```bash
   git clone https://github.com/your-username/nasa-image-viewer.git
   cd nasa-image-viewer
Start a local server using Python 3:

python3 -m http.server


Open your browser and visit:

http://localhost:8000


The demo will now run locally, showing the Local Archive by default.
You can switch to NASA Database Mode to search live data from NASA’s API.


## 🖼️ Adding Your Own Local Images

To add your own Deep Zoom (DZI) images:

Place your .dzi files inside the /img/ folder.

Add preview thumbnails inside /img/previews/.

Update the imageCatalog array inside index.html:
```js
{
    id: 'newimage',
    title: 'My Custom Galaxy',
    description: 'A beautiful galaxy captured during the 2025 observation mission.',
    dzi: 'img/mycustomgalaxy.dzi',
    preview: 'img/previews/mycustomgalaxy.png',
    type: 'local'
}
```

Refresh your browser — your new image will appear in Local Archive Mode.

## 🌠 Notes

Ensure your internet connection is active for NASA API searches.

Local DZI (Deep Zoom Image) files must be correctly linked in the /img/ folder.

Tested on Python 3.8+ and modern browsers (Chrome, Edge, Firefox).

## 🛰️ Technologies Used

HTML5 / CSS3 / JavaScript (Vanilla)

OpenSeadragon
 for deep-zoom functionality

NASA Image API
 for dynamic searches
