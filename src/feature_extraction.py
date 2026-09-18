import cv2
import numpy as np


def calculate_image_statistics(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return {
        "width": image.shape[1],
        "height": image.shape[0],
        "channels": image.shape[2],
        "mean_intensity": round(float(np.mean(gray)), 2),
        "std_intensity": round(float(np.std(gray)), 2),
        "min_intensity": int(np.min(gray)),
        "max_intensity": int(np.max(gray))
    }


def extract_edge_features(gray_image):

    edges = cv2.Canny(gray_image, 50, 150)

    edge_pixels = int(np.sum(edges > 0))
    total_pixels = edges.shape[0] * edges.shape[1]

    edge_density = edge_pixels / total_pixels

    return {
        "edge_pixels": edge_pixels,
        "edge_density": round(edge_density, 4)
    }