# Autonomous-Navigation-Of-UGV
Under Graduate Project under Prof. Tushar Sandhan

📌 Project Overview

The project aims to achieve safe and efficient autonomous navigation by integrating advanced perception and planning techniques. Key activities include the manual generation of a custom RGB-D dataset, the development of architectural refinements for multimodal semantic segmentation, and the hardware maintenance of a rugged all-terrain UGV.

🛠 Hardware Stack

Platform: Clearpath Husky A200 (Rugged differential-drive UGV).

Computer: NVIDIA Jetson AGX (ARMv8 8-core processor) for real-time processing.

Perception: Intel RealSense D455 RGB-D camera.

Sensors: Integrated IMU for high-frequency motion information.

🚀 Key Features & Research

 1.Multimodal Semantic Segmentation

  We utilize RGB-D fusion architectures like ESANet and MIPANet to classify every pixel into meaningful categories (traversable vs. non-traversable).

  Proposed Refinement: Modified the Multimodal Interaction Module (MIM) in MIPANet to use cross-modal attention with residual fusion.

  Results: Achieved a Mean Intersection Over Union (mIoU) of 92.6% on a binary dataset, outperforming the original MIPANet.

 2.Path Planning Algorithms
 
  Explored both global and local planning approaches to generate collision-free trajectories:

  Global Planners: Dijkstra's, A*, RRT, and RRT* for optimal full-path computation.

  Local Planners: Potential Field Method, Dynamic Window Approach (DWA), and Timed Elastic Band (TEB) for reactive obstacle avoidance.

 3.Dataset Generation

  Manually labeled over 800 images using LabelMe.

  Captured and processed synchronized RGB and depth information specifically for robotics environments.

🔧 Hardware Maintenance & Engineering

  Battery Replacement: Upgraded the Husky A200 power system by placing two 12V SLA batteries in series to meet the 24V requirement.

  3D Modeling: Designed a custom battery mount using Fusion 360 and an Ender 3D printer to secure hardware despite internal space constraints.

