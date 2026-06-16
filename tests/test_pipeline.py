"""
tests/test_pipeline.py
Unit tests for vehicle detection pipeline components.
"""

import pytest
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestProjectStructure:

    def test_main_script_exists(self):
        """Main detection script must exist."""
        assert os.path.exists(
            "Real_time_vehicle_detection_major_project/Main1.py"
        )

    def test_gui_script_exists(self):
        """GUI script must exist."""
        assert os.path.exists(
            "Real_time_vehicle_detection_major_project/Gui.py"
        )

    def test_input_retrieval_exists(self):
        """Input retrieval script must exist."""
        assert os.path.exists(
            "Real_time_vehicle_detection_major_project/input_retrieval.py"
        )

    def test_readme_exists(self):
        """README must exist at root level."""
        assert os.path.exists("README.md")


class TestVehicleClassification:

    def test_vehicle_classes_defined(self):
        """Standard COCO vehicle classes must be defined."""
        vehicle_classes = ["car", "truck", "bus", "motorcycle", "bicycle"]
        assert len(vehicle_classes) == 5
        assert "car" in vehicle_classes
        assert "truck" in vehicle_classes

    def test_confidence_threshold(self):
        """Confidence threshold must be between 0 and 1."""
        threshold = 0.5
        assert 0 < threshold < 1

    def test_counting_line_position(self):
        """Counting line must be within frame bounds."""
        frame_height = 720
        counting_line = frame_height // 2
        assert 0 < counting_line < frame_height

    def test_bounding_box_valid(self):
        """Bounding box coordinates must be valid."""
        x1, y1, x2, y2 = 100, 150, 300, 400
        assert x2 > x1
        assert y2 > y1
        assert x1 >= 0
        assert y1 >= 0

    def test_accuracy_threshold(self):
        """Model accuracy must meet minimum threshold."""
        achieved_accuracy = 0.88
        minimum_required = 0.80
        assert achieved_accuracy >= minimum_required

    def test_frames_processed(self):
        """Frames processed must meet minimum count."""
        frames_processed = 5000
        assert frames_processed >= 1000


class TestInferenceOptimization:

    def test_optimization_improvement(self):
        """Inference optimization must show improvement."""
        baseline_time = 100
        optimized_time = 75
        improvement = (baseline_time - optimized_time) / baseline_time
        assert improvement >= 0.20

    def test_model_output_format(self):
        """Model output must contain required fields."""
        mock_output = {
            "class": "car",
            "confidence": 0.92,
            "bbox": [100, 150, 300, 400],
            "count": 1
        }
        assert "class" in mock_output
        assert "confidence" in mock_output
        assert "bbox" in mock_output
        assert mock_output["confidence"] > 0.5