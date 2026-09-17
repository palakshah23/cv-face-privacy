# AI-Based Face Detection and Privacy Protection Using Computer Vision

## 1. Project Overview

This project implements an AI-based face detection and privacy protection system using computer vision and image processing techniques.

The system accepts an input image, detects human faces using the YuNet face detection model, identifies the detected face regions using bounding boxes, and automatically applies Gaussian blur to anonymize the detected faces.

The resulting image is generated as a privacy-protected output image.

The project provides both:

- A command-line interface (CLI) for image processing.
- A Streamlit-based user interface for interactive image upload, face detection, visualization, and anonymization.

## 2. Problem Statement

Images captured in public places, events, social media, research datasets, and surveillance environments may contain identifiable human faces.

Manually detecting and hiding faces in such images can be time-consuming, particularly when an image contains multiple people.

This project provides an automated computer vision solution that detects faces, identifies their locations, and applies Gaussian blur to the detected face regions to generate a privacy-protected image.

## 3. Objectives

The major objectives of the project are:

- Detect human faces automatically from input images.
- Locate detected faces using bounding boxes.
- Determine the number of detected faces.
- Apply Gaussian blur to detected face regions.
- Generate a privacy-protected output image.
- Provide a command-line execution method.
- Provide an interactive Streamlit interface.
- Validate the implementation using test images and automated testing.

## 4. Functional Modules

The system is divided into the following major functional modules.

### 4.1 Face Detection Module

The face detection module processes the input image and identifies human faces using OpenCV-based computer vision techniques.

The standalone CLI implementation uses the YuNet face detection model.

**Input:** Image  
**Output:** Detected face regions

### 4.2 Face Localization Module

For every detected face, the system identifies its bounding-box coordinates:

- X coordinate
- Y coordinate
- Width
- Height

**Input:** Detected faces  
**Output:** Face bounding-box coordinates

### 4.3 Privacy Anonymization Module

The privacy module applies Gaussian blur to the detected face regions.

This removes recognizable facial details while preserving the surrounding image content.

**Input:** Detected face regions  
**Output:** Anonymized image

### 4.4 Output Generation Module

The system saves the processed image to the output directory.

The Streamlit interface also provides an option to download the anonymized image.

**Input:** Processed image  
**Output:** Privacy-protected image file

## 5. Workflow

The overall workflow of the system is:

Input Image → Face Detection → Face Localization → Gaussian Blur → Privacy-Protected Output

### Processing Steps

1. The user provides an input image.
2. The image is loaded and processed using OpenCV.
3. Human faces are detected.
4. Bounding boxes are generated for detected faces.
5. The detected face regions are extracted.
6. Gaussian blur is applied to the face regions.
7. The anonymized image is generated.
8. The output image is saved or downloaded.

## 6. Technologies Used

### Programming Language

- Python

### Computer Vision

- OpenCV

### Face Detection

- YuNet Face Detection Model
- OpenCV FaceDetectorYN

### Image Processing

- Gaussian Blur
- Bounding-box based face localization
- Image format conversion

### User Interface

- Streamlit

### Model Format

- ONNX

### Testing

- Python unittest

### Version Control

- Git
- GitHub

## 7. Project Structure

    cv-face-privacy/
    │
    ├── Diagrams/
    │   ├── Component Diagram.png
    │   ├── Process Workflow Diagram.png
    │   ├── Sequence Diagram.png
    │   ├── System Architecture Diagram.png
    │   └── Use Case Diagram.png
    │
    ├── Screenshot/
    │   ├── 25_face_detection.png
    │   ├── face_detection.png
    │   ├── output.png
    │   ├── privacy_protected.png
    │   ├── privacy_protected_25.png
    │   └── streamlit.png
    │
    ├── input/
    │   ├── sample.png
    │   └── test_25_faces.png
    │
    ├── models/
    │   └── face_detection_yunet_2023mar.onnx
    │
    ├── output/
    │   ├── sample_anonymized.png
    │   └── test_25_faces_anonymized.png
    │
    ├── tests/
    │   └── test_face_privacy.py
    │
    ├── .gitignore
    ├── app.py
    ├── main.py
    ├── requirements.txt
    ├── README.md
    └── statement.md

## 8. System Architecture

The system follows the workflow:

Input Image → Image Processing → YuNet Face Detection → Face Localization → Gaussian Blur → Privacy-Protected Output

Detailed system architecture and design diagrams are available in the `Diagrams/` directory.

## 9. Setup

### Prerequisites

The project requires:

- Python 3.10 or newer
- pip
- Git

### Clone the Repository

    git clone https://github.com/palakshah23/cv-face-privacy.git

### Navigate to the Project Directory

    cd cv-face-privacy

### Create Virtual Environment

    python -m venv .venv

### Activate Virtual Environment

#### Windows PowerShell

    .venv\Scripts\Activate.ps1

#### Windows Command Prompt

    .venv\Scripts\activate

### Install Dependencies

    pip install -r requirements.txt

## 10. Model Configuration

The standalone image-processing implementation uses the YuNet face detection model.

Model file:

    face_detection_yunet_2023mar.onnx

The model is stored in:

    models/face_detection_yunet_2023mar.onnx

The application automatically loads the model from this location.

If the model file is missing, the application reports an appropriate error instead of continuing with an invalid configuration.

## 11. How to Run

### 11.1 Command-Line Interface

Place an input image inside the `input` directory.

Example:

    input/sample.png

Run:

    python main.py --input input/sample.png

The anonymized image is automatically saved in the `output` directory.

Example:

    output/sample_anonymized.png

### 11.2 Custom Output Path

A custom output path can also be specified:

    python main.py --input input/sample.png --output output/result.png

### 11.3 Streamlit Application

The project also includes an interactive Streamlit interface.

Run:

    streamlit run app.py

The application provides:

- Image upload
- Image preview
- Face detection
- Face count
- Face coordinates
- Privacy-protected image preview
- Anonymized image download

## 12. Example Output

For an image containing four faces, the system produced:

    AI FACE PRIVACY SYSTEM
    ----------------------
    Input: input/sample.png
    Faces detected: 4
    Faces anonymized: 4
    Output saved to:
    output\sample_anonymized.png

The system was also tested using an image containing 25 faces:

    Input: input/test_25_faces.png
    Faces detected: 25
    Faces anonymized: 25
    Output saved to:
    output\test_25_faces_anonymized.png

The corresponding output images are available in the `output/` directory.

## 13. Testing

Testing was performed using sample images and automated unit testing.

### Test Case 1: Four-Face Image

**Input:**

    input/sample.png

**Observed Result:**

    Faces detected: 4
    Faces anonymized: 4

**Output:**

    output/sample_anonymized.png

### Test Case 2: Twenty-Five-Face Image

**Input:**

    input/test_25_faces.png

**Observed Result:**

    Faces detected: 25
    Faces anonymized: 25

**Output:**

    output/test_25_faces_anonymized.png

### Automated Unit Test

The project includes:

    tests/test_face_privacy.py

The automated test verifies that:

- The test input image exists.
- The expected number of faces is detected.
- The anonymized output file is created.
- The generated output file is not empty.

The 25-face automated test completed successfully:

    Ran 1 test in 0.700s

    OK

## 14. Evaluation and Validation

The project was validated using controlled test images containing multiple faces.

| Test Input | Faces Detected | Faces Anonymized | Output Generated |
|------------|----------------|------------------|------------------|
| 4-face image | 4 | 4 | Yes |
| 25-face image | 25 | 25 | Yes |

The 25-face test is also included in the automated test suite.

The evaluation focuses on functional correctness of face detection, face anonymization, and successful output generation.

## 15. Non-Functional Requirements

### Performance

The system should process an input image without unnecessary processing steps and provide the anonymized output after detection and image processing.

### Usability

The Streamlit interface provides a simple workflow for uploading an image, detecting faces, viewing the results, and downloading the anonymized image.

### Reliability

The system validates important conditions such as the availability of the input image, model file, and successful output generation.

### Maintainability

The implementation separates major processing responsibilities into functions and maintains a structured project directory containing source code, tests, models, diagrams, screenshots, input data, and output data.

### Resource Efficiency

The system applies blur only to detected face regions rather than unnecessarily modifying the entire image.

## 16. Error Handling and Validation

The system includes validation for important runtime conditions.

### Invalid or Missing Input Image

If the input image cannot be read, the application reports an error instead of processing an invalid image.

### Missing YuNet Model

If the YuNet model is not available at the expected path, the application reports that the model is missing.

### Output Generation Failure

The system checks whether the processed image was successfully written to the output path.

### No Face Detected

If no face is detected, the Streamlit interface displays an appropriate warning to the user.

## 17. Design Documentation

The repository contains the following design diagrams:

- System Architecture Diagram
- Process Workflow Diagram
- Use Case Diagram
- Sequence Diagram
- Component Diagram

All diagrams are available in:

    Diagrams/

These diagrams describe the system structure, workflow, user interaction, component relationships, and processing sequence.

## 18. Screenshots

Screenshots demonstrating the project execution and results are available in:

    Screenshot/

The repository includes screenshots showing:

- Face detection
- Face detection with multiple faces
- Generated output
- Privacy-protected image
- Privacy protection for the 25-face test
- Streamlit interface

## 19. Applications

The project can be used as a foundation for privacy-aware image processing in areas such as:

- CCTV and surveillance image processing
- Public event photography
- Social media image processing
- Research datasets
- Computer vision datasets
- Privacy-aware image sharing
- Educational computer vision demonstrations

## 20. Limitations

The current implementation has the following limitations:

- Detection performance may vary depending on image quality.
- Very small or heavily occluded faces may be difficult to detect.
- Extremely dark or blurred images may affect detection performance.
- The current standalone implementation focuses on still-image processing.
- The system does not perform face recognition or identity identification.
- The current anonymization method uses Gaussian blur.

## 21. Future Scope

Possible future enhancements include:

- Real-time webcam face anonymization
- Video face privacy protection
- Batch processing of multiple images
- Pixelation as an alternative anonymization technique
- Additional privacy-preserving methods
- Web-based deployment
- Improved handling of small and partially occluded faces
- Performance optimization for large-scale image processing

## 22. Version Control

The project is maintained using Git and GitHub.

Git is used for:

- Source-code version control
- Tracking project changes
- Maintaining project history
- Organizing project development

The complete source code, documentation, tests, diagrams, screenshots, model configuration, and project statement are maintained in the repository.

Repository:

https://github.com/palakshah23/cv-face-privacy

## 23. Project Statement

A separate project statement is maintained in:

    statement.md

The project statement contains:

- Project title
- Problem statement
- Scope
- Target users
- High-level features

## 24. Development Context

This project was developed as a computer vision and image-processing project focused on automated face detection and privacy protection.

The implementation combines face detection, face localization, image processing, Gaussian blur, automated testing, and a user-facing Streamlit interface into a single workflow.

The project is intended to demonstrate the practical application of computer vision concepts to a real-world privacy-related problem.