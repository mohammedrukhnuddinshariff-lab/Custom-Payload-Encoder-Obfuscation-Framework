from flask import Flask, render_template, request

from encoders.base64_encoder import encode
from encoders.xor_encoder import xor_transform
from encoders.rot13_encoder import transform as rot13_transform
from obfuscators.string_splitter import split_string
from obfuscators.char_insertion import insert_separator
from obfuscators.escape_obfuscator import to_hex_escape
from detector.signature_detector import detect_signature, detect_normalized


app = Flask(__name__)

SIGNATURES = [
    "TEST_SECURITY_STRING",
    "DEMO_SIGNATURE_PATTERN",
]


@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    text = ""

    if request.method == "POST":
        text = request.form.get("text", "").strip()

        if text:
            results = {
                "base64": encode(text),
                "xor": xor_transform(text, 23),
                "rot13": rot13_transform(text),
                "split": " | ".join(split_string(text, 3)),
                "character_insertion": insert_separator(text),
                "hex_escape": to_hex_escape(text),
                "direct_detection": detect_signature(text, SIGNATURES),
                "normalized_detection": detect_normalized(text, SIGNATURES),
            }

    return render_template(
        "index.html",
        results=results,
        text=text
    )


if __name__ == "__main__":
 app.run()