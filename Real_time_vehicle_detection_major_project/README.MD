Real-Time Vehicle Detection, Counting, and Classification
Award: 3rd Prize at Project Expo 2K23 | Publication: CVR Journal of Science and Technology

Project Overview
This project implements an automated system for real-time traffic monitoring. It uses Computer Vision and Deep Learning to detect vehicles, classify them by type (car, truck, bus, etc.), and maintain a real-time count for traffic flow analysis.

Key Features
Real-Time Detection: Powered by SSD MobileNet v3 and OpenCV for high-speed processing.

High Accuracy: Achieved 88% accuracy in various traffic conditions.

Object Tracking: Implements algorithms to ensure a single vehicle is not counted multiple times as it moves through the frame.

Resource Efficient: Optimized to run on standard hardware without requiring high-end GPUs.

Installation & Setup
1. Clone the Repository
Bash
git clone https://github.com/TammineniTanay/vechiledetection.git
cd vechiledetection/Real_time_vehicle_detection_major_project
2. Install Dependencies
Ensure you have Python 3.8+ installed. Then, install the required libraries:

Bash
pip install opencv-python tensorflow numpy
3. Download Model Weights
The project uses the ssd_mobilenet_v3_large_coco_2020_01_14 model. Ensure the following files are in your project folder:

frozen_inference_graph.pb (The pre-trained model)

ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt (The configuration file)

coco.names (The list of 80 detectable classes)

How to Run
To start the detection on a video file or a live camera feed, run:

Bash
python Real_time_video_based_vehicle_detection.py
Methodology
This system follows a four-stage pipeline:

Preprocessing: Noise filtering and background subtraction to enhance frames.

Detection: SSD MobileNet identifies bounding boxes for objects.

Classification: Filters detections based on coco.names to focus only on vehicles.

Counting: A virtual "counting line" logic tracks when a bounding box center passes a specific coordinate.

Citation
If you use this work in your research, please cite our paper:

T. Tammineni, et al. "Real Time Video Based Vehicle Detection, Counting and Classification," CVR Journal of Science and Technology.