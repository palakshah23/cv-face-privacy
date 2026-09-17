import argparse
import os
import cv2


MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "models",
    "face_detection_yunet_2023mar.onnx"
)


def anonymize_faces(input_path, output_path):
    # Read input image
    image = cv2.imread(input_path)

    if image is None:
        raise FileNotFoundError(
            f"Could not read the image: {input_path}"
        )

    # Check whether YuNet model exists
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"YuNet model not found: {MODEL_PATH}"
        )

    # Create YuNet face detector
    detector = cv2.FaceDetectorYN.create(
        MODEL_PATH,
        "",
        (320, 320),
        0.7,
        0.3,
        5000
    )

    # Set image size for detection
    detector.setInputSize(
        (image.shape[1], image.shape[0])
    )

    # Detect faces
    _, faces = detector.detect(image)

    if faces is None:
        faces = []

    # Blur every detected face
    for face in faces:
        x, y, w, h = face[:4].astype(int)

        # Keep coordinates inside the image
        x = max(0, x)
        y = max(0, y)

        x2 = min(image.shape[1], x + w)
        y2 = min(image.shape[0], y + h)

        if x2 > x and y2 > y:
            face_region = image[y:y2, x:x2]

            blurred_face = cv2.GaussianBlur(
                face_region,
                (51, 51),
                0
            )

            image[y:y2, x:x2] = blurred_face

    # Create output directory if needed
    output_directory = os.path.dirname(output_path)

    if output_directory:
        os.makedirs(
            output_directory,
            exist_ok=True
        )

    # Save anonymized image
    success = cv2.imwrite(
        output_path,
        image
    )

    if not success:
        raise RuntimeError(
            "Could not save the output image."
        )

    return len(faces)


def main():
    parser = argparse.ArgumentParser(
        description="AI Face Detection and Privacy Protection"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to the input image"
    )

    parser.add_argument(
        "--output",
        default=None,
        help="Path for the anonymized output image"
    )

    args = parser.parse_args()

    # Automatically create output filename
    if args.output is None:
        filename = os.path.basename(args.input)

        name, extension = os.path.splitext(filename)

        args.output = os.path.join(
            "output",
            f"{name}_anonymized{extension}"
        )

    # Detect and anonymize faces
    faces_detected = anonymize_faces(
        args.input,
        args.output
    )

    # Display result
    print()
    print("AI FACE PRIVACY SYSTEM")
    print("----------------------")
    print(f"Input: {args.input}")
    print(f"Faces detected: {faces_detected}")
    print(f"Faces anonymized: {faces_detected}")
    print("Output saved to:")
    print(args.output)


if __name__ == "__main__":
    main()