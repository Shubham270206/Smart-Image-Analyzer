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

## 🧪 Testing

The project includes automated unit tests using Pytest.

Test coverage includes:
- Grayscale conversion
- Gaussian blur
- Thresholding
- Canny edge detection
- Image statistics
- Edge feature extraction

All 6 tests passed successfully.

## ⚠️ Error Handling

The application validates the uploaded image before processing.

Supported formats:
- JPG
- JPEG
- PNG

If an invalid or unreadable image is uploaded, the application displays an appropriate error message.

## 📋 Requirements

### Functional Requirements

- FR1: Upload an image
- FR2: Preprocess the image
- FR3: Detect image edges
- FR4: Analyze contours and shapes
- FR5: Extract image features
- FR6: Display analysis results

### Non-Functional Requirements

- Usability
- Performance
- Reliability
- Maintainability
- Portability

## 🚀 Future Scope

- Object detection using deep learning
- Face detection and recognition
- Advanced feature descriptors such as SIFT and HOG
- Image classification
- Batch image processing
- Downloadable analysis reports

## 👨‍💻 Project Information

**Project:** Smart Image Analyzer  
**Domain:** Computer Vision  
**Language:** Python  
**Framework:** Streamlit  
**Libraries:** OpenCV, NumPy, Pillow  
**Testing:** Pytest

## 🔗 GitHub Repository

[Smart Image Analyzer](https://github.com/Shubham270206/Smart-Image-Analyzer)