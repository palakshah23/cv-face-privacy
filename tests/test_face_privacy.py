import os
import tempfile
import unittest

from main import anonymize_faces


class TestFacePrivacy(unittest.TestCase):

    def test_25_face_detection_and_anonymization(self):
        input_path = os.path.join(
            "input",
            "test_25_faces.png"
        )

        self.assertTrue(
            os.path.exists(input_path),
            "Test image not found."
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = os.path.join(
                temp_dir,
                "result.png"
            )

            faces = anonymize_faces(
                input_path,
                output_path
            )

            self.assertEqual(faces, 25)
            self.assertTrue(
                os.path.exists(output_path)
            )
            self.assertGreater(
                os.path.getsize(output_path),
                0
            )


if __name__ == "__main__":
    unittest.main()