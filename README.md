# 🧬 ProteinGraph AI

> Converting protein structures into graphs and using AI to understand the language of life.

---

## 🚀 Overview

ProteinGraph AI is a Graph Neural Network (GNN)-based system that analyzes protein structures and classifies enzymes using their 3D geometry.

Instead of treating proteins as sequences, this project models them as spatial graphs, enabling deep learning models to capture structural relationships directly.

---

## 🎯 Why This Matters

* Drug Discovery → Identify molecular targets for therapeutics
* Disease Analysis → Understand impact of mutations
* Synthetic Biology → Engineer optimized enzymes
* Education → Interactive visualization of protein structures

---

## 🏗️ System Architecture

```mermaid
flowchart LR
    A[Frontend (Three.js)] --> B[Flask Backend]

    B --> C[PDB Loader]
    C --> D[Biopython Parser]
    D --> E[C-alpha Extraction]

    E --> F[Graph Construction]
    F --> G[Distance Matrix (< 8 Å)]
    G --> H[Graph (Nodes + Edges)]

    H --> I[Graph Neural Network]
    I --> J[Conv Layer 1]
    J --> K[Conv Layer 2]
    K --> L[Conv Layer 3]

    L --> M[Global Mean Pooling]
    M --> N[Fully Connected Layer]
    N --> O[Softmax Output]

    O --> P[Prediction + Confidence]
    P --> A
```

---

## 🧠 Core Idea

We convert proteins into graphs:

* Nodes → C-alpha atoms
* Edges → Spatial proximity (< 8 Å)
* Graph → Encodes 3D structure

Then apply a Graph Convolutional Network (GCN) to classify enzymes.

---

## ⚙️ Tech Stack

### Backend

* Python
* PyTorch
* PyTorch Geometric
* Flask
* Biopython

### Frontend

* HTML / CSS
* JavaScript
* Three.js (3D visualization)

---

## 🧪 Model Details

* Architecture: 3-layer GCN
* Input: 3D coordinates (x, y, z)
* Pooling: Global Mean Pooling
* Output: 6 Enzyme Classes

---

## 🎮 Features

### Graph-Based Protein Representation

* Converts atoms to nodes
* Uses spatial proximity to define edges

### Real-Time AI Pipeline

* Visual step-by-step inference
* Graph construction to prediction

### Mutation Simulation

* Simulates structural disruption
* Detects steric clashes
* Shows loss of function

### Interactive 3D Visualization

* Rotate, zoom, explore proteins
* Color-coded folding patterns

### Insight Panel

* Enzyme function
* Organism details
* Structural insights

---

## ▶️ How to Run

### 1. Clone Repo

```bash
git clone https://github.com/your-username/protein-graph-ai.git
cd protein-graph-ai/backend
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Start Backend

```bash
python app.py
```

Backend runs on:

```
http://127.0.0.1:5000
```

### 4. Run Frontend

```bash
cd ../frontend
python -m http.server 5500
```

Open:

```
http://localhost:5500
```

---

## 🔄 Workflow

1. Select enzyme (PDB ID)
2. Backend parses structure and builds graph
3. GNN performs classification
4. Frontend visualizes results and interactions

---

## 📈 Results

* Real-time enzyme classification
* Graph-based structural learning
* Scalable to thousands of proteins

---

## 🔮 Future Improvements

* AlphaFold integration
* Drug-binding prediction
* Cloud deployment
* Attention-based GNN (GAT)

---

## 📸 Demo

(Add demo GIF in /assets/demo.gif)

---

## 👨‍💻 Authors

* Arjun Singh
* Himanshi Garg
* Ayushi Naharwal

---

## ⭐ If you like this project

Give it a star ⭐
