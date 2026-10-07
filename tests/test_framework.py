import unittest

from encoders.base64_encoder import encode, decode
from encoders.xor_encoder import xor_transform
from encoders.rot13_encoder import transform as rot13_transform

from obfuscators.string_splitter import split_string, join_chunks
from obfuscators.char_insertion import (
    insert_separator,
    remove_separator,
)
from obfuscators.escape_obfuscator import (
    to_hex_escape,
    from_hex_escape,
)

from detector.signature_detector import (
    detect_signature,
    detect_normalized,
)


class TestEncoders(unittest.TestCase):

    def setUp(self):
        self.test_text = "TEST_SECURITY_STRING"

    def test_base64(self):
        encoded = encode(self.test_text)
        decoded = decode(encoded)

        self.assertEqual(
            decoded,
            self.test_text
        )

    def test_xor(self):
        key = 23

        transformed = xor_transform(
            self.test_text,
            key
        )

        recovered = xor_transform(
            transformed,
            key
        )

        self.assertEqual(
            recovered,
            self.test_text
        )

    def test_rot13(self):
        transformed = rot13_transform(
            self.test_text
        )

        recovered = rot13_transform(
            transformed
        )

        self.assertEqual(
            recovered,
            self.test_text
        )


class TestObfuscators(unittest.TestCase):

    def setUp(self):
        self.test_text = "TEST_SECURITY_STRING"

    def test_string_split(self):
        chunks = split_string(
            self.test_text,
            3
        )

        reconstructed = join_chunks(
            chunks
        )

        self.assertEqual(
            reconstructed,
            self.test_text
        )

    def test_character_insertion(self):
        transformed = insert_separator(
            self.test_text,
            "|"
        )

        restored = remove_separator(
            transformed,
            "|"
        )

        self.assertEqual(
            restored,
            self.test_text
        )

    def test_escape_representation(self):
        transformed = to_hex_escape(
            self.test_text
        )

        restored = from_hex_escape(
            transformed
        )

        self.assertEqual(
            restored,
            self.test_text
        )


class TestDetector(unittest.TestCase):

    def setUp(self):
        self.signature = [
            "TEST_SECURITY_STRING"
        ]

    def test_exact_detection(self):

        result = detect_signature(
            "TEST_SECURITY_STRING",
            self.signature
        )

        self.assertIn(
            "TEST_SECURITY_STRING",
            result
        )

    def test_no_detection(self):

        result = detect_signature(
            "COMPLETELY_SAFE_TEXT",
            self.signature
        )

        self.assertEqual(
            result,
            []
        )

    def test_normalized_detection(self):

        transformed = (
            "T|E|S|T|_|S|E|C|U|R|I|T|Y|_|S|T|R|I|N|G"
        )

        result = detect_normalized(
            transformed,
            self.signature
        )

        self.assertIn(
            "TEST_SECURITY_STRING",
            result
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)