import io
import os

import cv2
import numpy as np
import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="AI Face Privacy System",
    page_icon="🔒",
    layout="wide"
)


# Load the face detection model used by the
# original Face Detection implementation.
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades
    + "haarcascade_frontalface_default.xml"
)


def detect_faces(image_bytes):
    """
    Detect faces in an uploaded image and
    return the image along with face coordinates.
    """

    image = Image.open(
        io.BytesIO(image_bytes)
    ).convert("RGB")

    img = np.array(image)

    img = cv2.cvtColor(
        img,
        cv2.COLOR_RGB2BGR
    )

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    face_list = []

    for (x, y, w, h) in faces:

        face_list.append({
            "x": int(x),
            "y": int(y),
            "width": int(w),
            "height": int(h)
        })

    return image, img, face_list


def anonymize_faces(image, faces):
    """
    Apply Gaussian blur to detected face regions.
    """

    result = image.copy()

    for face in faces:

        x = face["x"]
        y = face["y"]
        w = face["width"]
        h = face["height"]

        x2 = min(
            result.shape[1],
            x + w
        )

        y2 = min(
            result.shape[0],
            y + h
        )

        if x2 > x and y2 > y:

            face_region = result[
                y:y2,
                x:x2
            ]

            blurred_face = cv2.GaussianBlur(
                face_region,
                (51, 51),
                0
            )

            result[
                y:y2,
                x:x2
            ] = blurred_face

    return result


# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("Features")

feature = st.sidebar.selectbox(
    "Choose Feature",
    ["Face Detection & Privacy Protection"]
)


# -----------------------------
# Main interface
# -----------------------------

st.title("🔒 AI Face Privacy System")

st.subheader(
    "📷 Face Detection & Privacy Protection"
)

st.write("Upload an image to detect and anonymize faces.")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file is not None:

    image_bytes = uploaded_file.getvalue()

    original_image, cv_image, faces = detect_faces(
        image_bytes
    )

    st.subheader("Uploaded Image")

    st.image(
        original_image,
        use_container_width=True
    )

    if st.button("Detect Face"):

        if len(faces) > 0:

            st.success("Detection Successful")

        else:

            st.warning(
                "No faces detected in the image."
            )

        st.write("### Faces Detected")

        st.write(len(faces))

        if len(faces) > 0:

            st.write("### Face Coordinates")

            for index, face in enumerate(
                faces,
                start=1
            ):

                st.write(
                    f"**Face {index}**"
                )

                st.write(
                    f"- X: {face['x']}"
                )

                st.write(
                    f"- Y: {face['y']}"
                )

                st.write(
                    f"- Width: {face['width']}"
                )

                st.write(
                    f"- Height: {face['height']}"
                )

            # -----------------------------
            # Privacy protection
            # -----------------------------

            anonymized = anonymize_faces(
                cv_image,
                faces
            )

            anonymized_rgb = cv2.cvtColor(
                anonymized,
                cv2.COLOR_BGR2RGB
            )

            st.write(
                "### Privacy-Protected Image"
            )

            st.image(
                anonymized_rgb,
                use_container_width=True
            )

            success, encoded_image = cv2.imencode(
                ".png",
                anonymized
            )

            if success:

                st.download_button(
                    label="Download Anonymized Image",
                    data=encoded_image.tobytes(),
                    file_name=(
                        "anonymized_"
                        + uploaded_file.name
                    ),
                    mime="image/png"
                )