# 🔍 Smart Image Analyzer

A Computer Vision Based Image Processing and Feature Analysis System built using Python, OpenCV, NumPy, and Streamlit.

---

## 📌 Project Overview

Smart Image Analyzer is an interactive Computer Vision application that analyzes an uploaded image through multiple image-processing stages.

The system performs image preprocessing, edge detection, contour and shape analysis, and feature extraction. The results are displayed through a simple Streamlit web interface.

The project follows a modular architecture where different Computer Vision operations are implemented in separate Python modules.

---

## 🎯 Objectives

- Process and analyze digital images using Computer Vision techniques.
- Convert images into useful representations such as grayscale and binary images.
- Detect important image edges using the Canny edge detection algorithm.
- Detect and analyze object contours.
- Extract statistical and edge-based image features.
- Provide an interactive interface for viewing image-processing results.
- Maintain a modular and testable codebase.

---

## ✨ Features

### 1. Image Preprocessing

The application performs:

- Color-to-grayscale conversion
- Gaussian blur for noise reduction
- Binary thresholding

### 2. Edge Detection

The system uses the Canny edge detection algorithm to identify important edges and structural information in the image.

### 3. Contour & Shape Analysis

The application:

- Detects external contours
- Counts detected contours
- Calculates contour area
- Calculates contour perimeter
- Calculates bounding-box width and height
- Draws detected contours on the original image

### 4. Feature Extraction

The application extracts:

#### Image Statistics

- Image width
- Image height
- Number of channels
- Mean intensity
- Standard deviation of intensity
- Minimum intensity
- Maximum intensity

#### Edge Features

- Number of edge pixels
- Edge density

### 5. Interactive Visualization

All results are presented using an interactive Streamlit interface.

---

## 🏗️ System Architecture

The application follows the workflow:

```text
                    USER
                     │
                     ▼
                Upload Image
                     │
                     ▼
            Image Preprocessing
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
      Grayscale   Gaussian   Threshold
                   Blur
                     │
                     ▼
              Edge Detection
                     │
                     ▼
            Contour Detection
                     │
                     ▼
            Contour Analysis
                     │
                     ▼
             Feature Extraction
                ┌────┴────┐
                ▼         ▼
        Image Statistics  Edge Features
                │         │
                └────┬────┘
                     ▼
                Visualization
                     │
                     ▼
                  Results