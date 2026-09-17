# AI-Based Face Detection and Privacy Protection Using Computer Vision

## 1. Project Overview

This project implements an AI-based face detection and privacy protection system using computer vision.

The system accepts an input image, detects human faces using the YuNet face detection model, and automatically applies Gaussian blur to the detected face regions. The resulting image is saved as a privacy-protected output image.

---

## 2. Problem Statement

Images captured in public places, events, social media, research datasets, and surveillance environments may contain identifiable faces.

Manually hiding faces in such images is time-consuming, especially when an image contains multiple people.

This project provides an automated approach for detecting and anonymizing faces using computer vision and image processing techniques.

---

## 3. Objectives

- Detect human faces automatically in an input image.
- Locate detected faces using bounding boxes.
- Apply Gaussian blur to detected face regions.
- Generate a privacy-protected output image.
- Provide a simple command-line interface for execution.

---

## 4. Workflow

```text
Input Image
     |
     v
YuNet Face Detection
     |
     v
Face Localization
     |
     v
Detected Face Regions
     |
     v
Gaussian Blur
     |
     v
Privacy-Protected Output
```

---

## 5. Technologies Used

- Python
- OpenCV
- YuNet Face Detection
- ONNX
- Gaussian Blur
- Command-Line Interface (CLI)

---

## 6. Project Structure

```text
cv-face-privacy/
|
├── input/
│   ├── sample.png
│   └── test_25_faces.png
|
├── output/
│   ├── sample_anonymized.png
│   └── test_25_faces_anonymized.png
|
├── models/
│   └── face_detection_yunet_2023mar.onnx
|
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

---

## 7. Setup

### Prerequisites

- Python 3.10 or newer
- pip
- Git

### Create Virtual Environment

```powershell
python -m venv .venv
```

### Activate Virtual Environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Install Dependencies

```powershell
pip install -r requirements.txt
```

---

## 8. Model Configuration

The project uses the YuNet face detection model:

```text
face_detection_yunet_2023mar.onnx
```

Place the model inside the `models` directory:

```text
models/face_detection_yunet_2023mar.onnx
```

The application automatically loads the model from this location.

---

## 9. How to Run

Place an input image inside the `input` directory.

Example:

```text
input/sample.png
```

Run the application from the project root:

```powershell
python main.py --input input/sample.png
```

The anonymized image will automatically be saved in the `output` directory.

Example:

```text
output/sample_anonymized.png
```

### Custom Output Path

A custom output path can also be provided:

```powershell
python main.py --input input/sample.png --output output/result.png
```

---

## 10. Example Output

For an image containing four faces:

```text
AI FACE PRIVACY SYSTEM
----------------------
Input: input/sample.png
Faces detected: 4
Faces anonymized: 4
Output saved to:
output\sample_anonymized.png
```

The system was also tested using a 25-face image:

```text
Input: input/test_25_faces.png
Faces detected: 25
Faces anonymized: 25
Output saved to:
output\test_25_faces_anonymized.png
```

---

## 11. Applications

- CCTV and surveillance footage
- Public event photography
- Social media images
- Research datasets
- Privacy-aware image processing
- Computer vision datasets

---

## 12. Limitations

- Detection performance may vary depending on image quality.
- Very small or heavily occluded faces may be difficult to detect.
- Extremely dark or blurred images may affect detection performance.
- The current version processes still images rather than live video.

---

## 13. Future Scope

- Real-time webcam face anonymization
- Video face privacy protection
- Batch processing of multiple images
- Pixelation as an alternative anonymization method
- Web-based privacy protection application