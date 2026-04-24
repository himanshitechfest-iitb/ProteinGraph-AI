# 🧬 ProteinGraph AI

> Converting protein structures into graphs and using AI to understand the language of life.

---

## 🚀 Overview

ProteinGraph AI is a **Graph Neural Network (GNN)-based system** that analyzes protein structures and classifies enzymes using their **3D geometry**.

Instead of treating proteins as sequences, this project models them as **spatial graphs**, enabling deep learning models to capture structural relationships directly.

---

## 🎯 Why This Matters

- 🔬 Drug Discovery → Identify molecular targets for therapeutics  
- 🧬 Disease Analysis → Understand impact of mutations  
- ⚙️ Synthetic Biology → Engineer optimized enzymes  
- 📚 Education → Interactive visualization of protein structures  

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
