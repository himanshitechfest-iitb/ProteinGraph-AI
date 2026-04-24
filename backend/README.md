# ⚙️ Backend (app.py) — ProteinGraph-AI

This backend powers the **AI inference pipeline** for ProteinGraph-AI. It parses protein structures, converts them into graphs, and runs a **Graph Neural Network (GNN)** to classify enzymes.

---

## 🚀 Overview

Built using **Flask + PyTorch + PyTorch Geometric**, the backend:

* Loads protein structures from PDB
* Converts them into graph representations
* Runs a trained **Graph Convolutional Network (GCN)**
* Returns predictions and structural insights via API

---

## 🧠 Core Pipeline

### 1. 📥 Data Loading

* Fetches `.pdb` files from **RCSB Protein Data Bank**
* Stores locally in `dataset/`

### 2. 🧬 Structure Parsing

* Uses **Biopython (PDBParser)**
* Extracts only **C-alpha atoms**

### 3. 🔗 Graph Construction

* Nodes → C-alpha coordinates
* Edges → created using distance threshold (< 8 Å)
* Distance matrix computed using **SciPy**

### 4. 🧠 GNN Model

* 3-layer **Graph Convolutional Network (GCN)**
* Feature aggregation from neighbors
* Global mean pooling
* Fully connected layer + softmax

### Core Equation

[
H^{(l+1)} = \sigma(D^{-1/2} A D^{-1/2} H^{(l)} W^{(l)})
]

---

## 🧩 Model Architecture

* Input: 3D coordinates (x, y, z)
* Conv1 → 64 features
* Conv2 → 128 features
* Conv3 → 64 features
* Global Pooling
* Linear Layer → 6 classes

---

## 🌐 API Endpoints

### `/api/predict`

**Method:** GET
**Params:** `pdb_id`

Example:

```
/api/predict?pdb_id=1a3d
```

### Response

```json
{
  "prediction": "EC class",
  "confidence": 97.2,
  "nodes": [...],
  "edges": [...],
  "stats": {
    "total_raw_atoms": 12345,
    "ai_nodes_extracted": 300,
    "spatial_edges_formed": 1200
  }
}
```

---

## ▶️ How to Run Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```

Runs on:

```
http://127.0.0.1:5000
```

---

## 📦 Dependencies

* torch
* torch-geometric
* numpy
* scipy
* flask
* biopython

---

## ⚠️ Notes

* Dataset auto-downloads on first run
* Requires internet for initial PDB fetch
* Uses CPU by default

---

## 🔥 Future Improvements

* GPU acceleration
* Better trained GNN model
* Support for custom protein upload
* Integration with AlphaFold

---

## 👨‍💻 Part of

ProteinGraph-AI p
