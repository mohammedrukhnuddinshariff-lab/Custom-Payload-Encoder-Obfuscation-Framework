from encoders.base64_encoder import encode, decode
from encoders.xor_encoder import xor_transform
from encoders.rot13_encoder import transform as rot13_transform

from obfuscators.string_splitter import split_string, join_chunks
from obfuscators.char_insertion import insert_separator, remove_separator
from obfuscators.escape_obfuscator import to_hex_escape, from_hex_escape

from detector.signature_detector import (
    detect_signature,
    detect_normalized,
)

from reporting.report_generator import (
    generate_report,
    save_json_report,
    save_csv_report,
)


SIGNATURES = [
    "TEST_SECURITY_STRING",
    "DEMO_SIGNATURE_PATTERN",
]


def test_base64(text):
    encoded = encode(text)
    decoded = decode(encoded)

    print("\n=== Base64 Test ===")
    print(f"Original : {text}")
    print(f"Encoded  : {encoded}")
    print(f"Decoded  : {decoded}")

    return encoded


def test_xor(text):
    key = 23

    transformed = xor_transform(text, key)
    recovered = xor_transform(transformed, key)

    print("\n=== XOR Test ===")
    print(f"Original : {text}")
    print(f"Key      : {key}")
    print(f"XOR      : {repr(transformed)}")
    print(f"Recovered: {recovered}")

    return transformed


def test_rot13(text):
    transformed = rot13_transform(text)
    recovered = rot13_transform(transformed)

    print("\n=== ROT13 Test ===")
    print(f"Original : {text}")
    print(f"ROT13    : {transformed}")
    print(f"Recovered: {recovered}")

    return transformed


def test_split(text):
    chunks = split_string(text, 3)
    reconstructed = join_chunks(chunks)

    print("\n=== String Splitting Test ===")
    print(f"Original     : {text}")
    print(f"Chunks       : {chunks}")
    print(f"Reconstructed: {reconstructed}")

    return "|".join(chunks)


def test_insertion(text):
    transformed = insert_separator(text, "|")
    restored = remove_separator(transformed, "|")

    print("\n=== Character Insertion Test ===")
    print(f"Original : {text}")
    print(f"Modified : {transformed}")
    print(f"Restored : {restored}")

    return transformed


def test_escape(text):
    transformed = to_hex_escape(text)
    restored = from_hex_escape(transformed)

    print("\n=== Escape Representation Test ===")
    print(f"Original : {text}")
    print(f"Escaped  : {transformed}")
    print(f"Restored : {restored}")

    return transformed


def detect_text(method, text):
    matches = detect_signature(
        text,
        SIGNATURES
    )

    if matches:
        status = "DETECTED"
    else:
        status = "NOT DETECTED"

    print(f"\n=== Detection Result: {method} ===")
    print(f"Status  : {status}")

    if matches:
        print(f"Matches : {matches}")

    return {
        "method": method,
        "status": status,
        "matches": matches,
    }


def run_all_tests(text):

    results = []

    print("\n========================================")
    print(" Running Complete Security Test Suite")
    print("========================================")

    # Original
    results.append(
        detect_text(
            "Original",
            text
        )
    )

    # Base64
    base64_text = test_base64(text)

    results.append(
        detect_text(
            "Base64",
            base64_text
        )
    )

    # XOR
    xor_text = test_xor(text)

    results.append(
        detect_text(
            "XOR",
            xor_text
        )
    )

    # ROT13
    rot13_text = test_rot13(text)

    results.append(
        detect_text(
            "ROT13",
            rot13_text
        )
    )

    # String Split
    split_text = test_split(text)

    results.append(
        detect_text(
            "String Split",
            split_text
        )
    )

    # Character insertion
    insertion_text = test_insertion(text)

    results.append(
        detect_text(
            "Character Insertion",
            insertion_text
        )
    )

    # Escape representation
    escape_text = test_escape(text)

    results.append(
        detect_text(
            "Escape Representation",
            escape_text
        )
    )

    # Multi-layer
    layer1 = rot13_transform(text)
    layer2 = encode(layer1)
    layer3 = encode(layer2)

    print("\n=== Multi-Layer Transformation ===")
    print(f"Original       : {text}")
    print(f"ROT13          : {layer1}")
    print(f"Base64 Layer 1 : {layer2}")
    print(f"Base64 Layer 2 : {layer3}")

    results.append(
        detect_text(
            "ROT13 + Base64 + Base64",
            layer3
        )
    )

    return results


def show_improved_detection(text):

    print("\n========================================")
    print(" Improved Defensive Detection")
    print("========================================")

    results = {
        "Original": text,
        "Character Insertion": insert_separator(
            text,
            "|"
        ),
        "String Split": "|".join(
            split_string(text, 3)
        ),
    }

    for method, transformed in results.items():

        basic = detect_signature(
            transformed,
            SIGNATURES
        )

        improved = detect_normalized(
            transformed,
            SIGNATURES
        )

        basic_result = (
            "DETECTED"
            if basic
            else "NOT DETECTED"
        )

        improved_result = (
            "DETECTED"
            if improved
            else "NOT DETECTED"
        )

        print(f"\nMethod: {method}")
        print(f"Basic detector    : {basic_result}")
        print(f"Improved detector : {improved_result}")


def generate_reports(results):

    report = generate_report(results)

    print("\n========================================")
    print(" Analysis Summary")
    print("========================================")

    print(
        f"Total tests     : "
        f"{report['total_tests']}"
    )

    print(
        f"Detected        : "
        f"{report['detected']}"
    )

    print(
        f"Not detected    : "
        f"{report['not_detected']}"
    )

    print(
        f"Detection rate  : "
        f"{report['detection_rate_percent']}%"
    )

    json_path = save_json_report(
        report
    )

    csv_path = save_csv_report(
        results
    )

    print(
        f"\nJSON report : {json_path}"
    )

    print(
        f"CSV report  : {csv_path}"
    )


def show_menu():

    print("\n")
    print("========================================")
    print(" Custom Payload Encoder Framework")
    print("========================================")

    print("1. Base64")
    print("2. XOR")
    print("3. ROT13")
    print("4. String Split")
    print("5. Character Insertion")
    print("6. Escape Representation")
    print("7. Run Complete Test Suite")
    print("8. Improved Detection Test")
    print("9. Exit")

    print("========================================")


def main():

    print("\nCustom Payload Encoder &")
    print("Obfuscation Framework")

    while True:

        show_menu()

        choice = input(
            "\nSelect an option: "
        ).strip()

        if choice == "9":

            print(
                "\nExiting framework..."
            )

            break

        if choice in {
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
        }:

            text = input(
                "\nEnter a benign test string: "
            ).strip()

            if not text:

                print(
                    "\nInput cannot be empty."
                )

                continue

        if choice == "1":

            transformed = test_base64(
                text
            )

            detect_text(
                "Base64",
                transformed
            )

        elif choice == "2":

            transformed = test_xor(
                text
            )

            detect_text(
                "XOR",
                transformed
            )

        elif choice == "3":

            transformed = test_rot13(
                text
            )

            detect_text(
                "ROT13",
                transformed
            )

        elif choice == "4":

            transformed = test_split(
                text
            )

            detect_text(
                "String Split",
                transformed
            )

        elif choice == "5":

            transformed = test_insertion(
                text
            )

            detect_text(
                "Character Insertion",
                transformed
            )

        elif choice == "6":

            transformed = test_escape(
                text
            )

            detect_text(
                "Escape Representation",
                transformed
            )

        elif choice == "7":

            results = run_all_tests(
                text
            )

            show_improved_detection(
                text
            )

            generate_reports(
                results
            )

        elif choice == "8":

            show_improved_detection(
                text
            )

        else:

            print(
                "\nInvalid option. "
                "Please select 1-9."
            )


if __name__ == "__main__":
    main()