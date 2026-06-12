# Autonomous UGV Navigation via Enhanced RGB-D Semantic Segmentation
Undergraduate Research Project  | Indian Institute of Technology, Kanpur  | **Mentor:** Prof. Tushar Sandhan | **Author:** Utkarsh Sawarn  

---

## 📌 Project Architecture & Objective
The goal of this project is to implement robust autonomous navigation on an all-terrain Unmanned Ground Vehicle (UGV) via model-based path planning. The primary bottleneck is translating multimodal environmental inputs (RGB + Depth) into high-fidelity binary semantic masks (Traversable vs. Non-Traversable space) to feed downstream trajectory generation stacks.
---

## 🚀 Core Technical Contributions

### 1. Architectural Optimization: Residual Cross-Modal Attention ($KVQ$)
To resolve spatial boundaries more cleanly than native multi-stream architectures, I engineered a mathematical modification to the **Multimodal Interaction Module (MIM)** inside **MIPANet**:
* **The Realignment:** I refactored the attention projection pipeline by altering the Query ($Q$), Key ($K$), and Value ($V$) mappings. RGB spatial context acts as the Query ($Q_{rgb}$), while structural depth maps dictate the Keys ($K_{dep}$) and Values ($V_{rgb}$). The inverse mapping is processed in parallel for the depth stream.
* **Residual Fusion:** Integrated a direct skip connection to add the original raw feature streams back into the attention outputs:
  $$\text{Output} = Q_{rgb}K_{dep}^{T}V_{rgb} + Q_{dep}K_{rgb}^{T}V_{dep} + V_{rgb} + V_{dep}$$
* **Quantifiable Impact:** Trained and benchmarked the architecture on a binary outdoor traversability dataset, achieving a **92.6% Mean Intersection Over Union (mIoU)**, directly outperforming the baseline MIPANet paper model (91.0%).

### 2. Dataset Engineering & Sensor Validation Traps
* **Target Dataset Generation:** Curated, synchronized, and manually pixel-labeled **800+ RGB-D outdoor field scenes** using `LabelMe`, parsing raw JSON annotations into structured RGB, depth, and target label arrays via Python automation.
* **Active IR Stereo Failure Analysis:** Identified a critical edge-case failure mode where bright ambient solar radiation saturated the Intel RealSense D455's active IR sensors, causing severe depth map holes and stereo-matching fragmentation in outdoor environments. Navigated this constraint by shifting validation weights to the RGB stream under solar interference.

### 3. Industrial Peer Review & Academic Verification
* Selected by the project advisor to map and resolve detailed criticism raised by **IEEE Peer Reviewers** for the learning-based diffusion path-planning paper *'Neural PathLite'*. 
* Co-authored literature revisions by adding comprehensive ablation studies isolating lightweight compute efficiencies, extending comparative state-of-the-art citations in the Related Work sections, and documenting systemic model failure case analyses.

---

## 🛠️ Compute & Hardware Field Infrastructure

* **Mobility Base Platform:** Clearpath Husky A200 (Rugged, heavy-duty differential-drive all-terrain research UGV).
* **Onboard Edge Compute:** NVIDIA Jetson AGX (ARMv8 8-Core CPU + Volta GPU Architecture) running real-time multimodal perception layers.
* **Sensor Suite Payload:** Intel RealSense D455 RGB-D long-range stereo depth camera + high-frequency internal 6-DoF IMU.

---

## 🔧 Applied Mechanical & Power Systems Engineering

* **Power Delivery Retrofit:** Diagnosed battery degradation and short operating cycles on the experimental chassis. Re-engineered the core power distribution bus by combining **two 12V Sealed Lead-Acid (SLA) batteries in a series configuration** to fulfill the high-current 24V/12Ahr demand profile under maximum stall torque load conditions.
* **CAD & Additive Manufacturing:** Addressed a severe physical packaging conflict when the custom dual-battery assembly exceeded the internal compartment height by 1mm. Form-modeled a structural retention casing in **Autodesk Fusion 360** and fabricated a physical prototype on an **Ender 3D printer** to securely mount and stabilize the secondary battery block on the exterior upper frame plate under active driving vibrations.

---

## 💻 Algorithmic Implementations Analysed

* **Global Path Planners Studied:** Dijkstra's Algorithm (uniform graph exploration), A* (admissible heuristic cost optimization), RRT, and Asymptotically Optimal RRT* (tree-rewiring path refinement).
* **Local Reactive Planners Studied:** Artificial Potential Fields (Attractive/Repulsive vector summation), Dynamic Window Approach (DWA velocity-space search constraints), and Timed Elastic Band (TEB non-linear multi-objective optimization).
