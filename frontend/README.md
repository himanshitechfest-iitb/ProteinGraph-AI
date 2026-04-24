# 🌐 Frontend (index.html) — ProteinGraph-AI

This frontend provides an **interactive 3D visualization** and control panel for exploring protein structures and running AI inference in real time.

---

## 🚀 Overview

The UI is built using **HTML, CSS, and JavaScript** with **Three.js** for rendering 3D protein graphs. It communicates with the Flask backend to fetch predictions and structural data.

---

## 🧠 What the Frontend Does

* Visualizes proteins as **graphs (nodes + edges)**
* Sends requests to backend API (`/api/predict`)
* Displays **model predictions + confidence**
* Simulates **mutations and structural instability**
* Provides an **interactive educational panel**

---

## 🏗️ Core Components

### 1. 🎮 Control Panel

* Select enzyme (PDB ID)
* Run inference pipeline
* Toggle visualization modes
* Simulate mutation

### 2. 🧬 3D Visualization (Three.js)

* Nodes → C-alpha atoms
* Edges → spatial proximity
* OrbitControls → rotate, zoom, pan
* Dynamic color gradient → sequence mapping

### 3. 📊 Information Panel

* Enzyme name, function, organism
* Structural insights
* Biological significance
* Graph statistics (nodes, edges, atoms)

### 4. ⚙️ Pipeline Animation

* Step-by-step visualization:

  1. Backbone extraction
  2. Graph construction
  3. Feature aggregation

---

## 🔌 API Integration

The frontend calls:

```
GET /api/predict?pdb_id=<ID>
```

### Response includes:

* `nodes` → 3D coordinates
* `edges` → connectivity
* `prediction` → enzyme class
* `confidence` → model confidence
* `stats` → atoms, nodes, edges

---

## 🎨 Visualization Logic

* Nodes rendered as **spheres**
* Edges rendered as **lines**
* Colors assigned using **HSL gradient** across sequence
* Mutation simulation:

  * Enlarges selected node
  * Displaces neighboring nodes
  * Highlights steric clash

---

## ▶️ How to Run Frontend

```bash
cd frontend
python -m http.server 5500
```

Open in browser:

```
http://localhost:5500
```

Make sure backend is running at:

```
http://127.0.0.1:5000
```

---

## ⚠️ Notes

* Backend must be running before using UI
* Uses CDN for Three.js and dependencies
* Designed for modern browsers (Chrome recommended)

---

## 🔥 Future Improvements

* Drag-and-drop PDB upload
* Toggle different graph views
* Heatmap visualization for active sites
* Better mutation physics simulation

---

## 👨‍💻 Part of

ProteinGraph-AI project
