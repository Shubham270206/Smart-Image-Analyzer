import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


import numpy as np

from src.preprocessing import (
    convert_to_grayscale,
    apply_gaussian_blur,
    apply_threshold
)

from src.edge_detection import detect_edges

from src.feature_extraction import (
    calculate_image_statistics,
    extract_edge_features
)


def create_test_image():
    """Create a simple synthetic test image."""
    image = np.zeros((100, 100, 3), dtype=np.uint8)

    image[25:75, 25:75] = 255

    return image


def test_grayscale_conversion():

    image = create_test_image()

    gray = convert_to_grayscale(image)

    assert gray.shape == (100, 100)


def test_gaussian_blur():

    image = create_test_image()

    gray = convert_to_grayscale(image)

    blurred = apply_gaussian_blur(gray)

    assert blurred.shape == gray.shape


def test_threshold():

    image = create_test_image()

    gray = convert_to_grayscale(image)

    thresholded = apply_threshold(gray)

    assert thresholded.shape == gray.shape


def test_edge_detection():

    image = create_test_image()

    gray = convert_to_grayscale(image)

    edges = detect_edges(gray)

    assert edges.shape == gray.shape


def test_image_statistics():

    image = create_test_image()

    statistics = calculate_image_statistics(image)

    assert statistics["width"] == 100
    assert statistics["height"] == 100
    assert statistics["channels"] == 3


def test_edge_features():

    image = create_test_image()

    gray = convert_to_grayscale(image)

    features = extract_edge_features(gray)

    assert "edge_pixels" in features
    assert "edge_density" in features
