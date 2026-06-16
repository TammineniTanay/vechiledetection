# Real-Time Vehicle Detection, Counting & Classification

> Published in CVR Journal of Science & Technology, Vol. 24, June 2023 | 🏆 3rd Prize, Project Expo 2K23

[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://python.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green)](https://opencv.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)](https://tensorflow.org)

## Overview

A real-time computer vision system that detects, counts, and classifies vehicles from video footage with 88% accuracy across 5,000+ processed frames. Built for intelligent transportation and traffic monitoring applications.

## Results

- **88% detection accuracy** across 5,000+ video frames
- **25% inference optimization** via TensorFlow model quantization
- **Real-time processing** on standard hardware without high-end GPUs
- **Published** in CVR Journal of Science & Technology (Vol. 24, June 2023)
- **Award:** 3rd Prize at Project Expo 2K23

## How It Works
Video Input

↓

[Preprocessing] — noise filtering, background subtraction

↓

[Detection] — SSD MobileNet v3 identifies bounding boxes

↓

[Classification] — filters detections to vehicle classes only

↓

[Counting] — virtual counting line tracks unique vehicles

↓

Real-time count output

## Tech Stack

- **Python** — core pipeline
- **OpenCV** — video capture and frame processing
- **TensorFlow** — SSD MobileNet v3 inference
- **YOLOv8** — improved detection model
- **NumPy** — numerical operations

## Quick Start

```bash
git clone https://github.com/TammineniTanay/vechiledetection.git
cd vechiledetection/Real_time_vehicle_detection_major_project
pip install opencv-python tensorflow numpy
python Main1.py
```

## Project Structure
vechiledetection/

├── Real_time_vehicle_detection_major_project/

│   ├── Main1.py          — main detection pipeline

│   ├── Gui.py            — GUI interface

│   ├── input_retrieval.py — video input handling

│   └── README.MD         — detailed setup guide

├── tests/

│   └── test_pipeline.py  — unit tests

└── README.md             — this file

## Publication

T. Tammineni, et al. "Real Time Video Based Vehicle Detection, Counting and Classification," CVR Journal of Science & Technology, Vol. 24, June 2023.

## Author

Tanay Tammineni — [GitHub](https://github.com/TammineniTanay) | [LinkedIn](https://linkedin.com/in/tanay-tammineni)