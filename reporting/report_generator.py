import csv
import json
from datetime import datetime
from pathlib import Path


def calculate_detection_rate(results: list[dict]) -> float:
    """Calculate the percentage of tested representations detected."""

    if not results:
        return 0.0

    detected_count = sum(
        1
        for result in results
        if result["status"] == "DETECTED"
    )

    return (detected_count / len(results)) * 100


def generate_report(results: list[dict]) -> dict:
    """Generate a structured analysis report."""

    detected_count = sum(
        1
        for result in results
        if result["status"] == "DETECTED"
    )

    not_detected_count = sum(
        1
        for result in results
        if result["status"] == "NOT DETECTED"
    )

    detection_rate = calculate_detection_rate(results)

    return {
        "project": "Custom Payload Encoder & Obfuscation Framework",
        "generated_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "total_tests": len(results),
        "detected": detected_count,
        "not_detected": not_detected_count,
        "detection_rate_percent": round(
            detection_rate,
            2
        ),
        "results": results,
    }


def save_json_report(
    report: dict,
    filename: str = "reports/analysis_report.json"
):
    """Save the report as a JSON file."""

    output_path = Path(filename)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with output_path.open(
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            report,
            file,
            indent=4
        )

    return output_path


def save_csv_report(
    results: list[dict],
    filename: str = "reports/detection_results.csv"
):
    """Save transformation results as a CSV file."""

    output_path = Path(filename)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with output_path.open(
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Method",
            "Detection Status",
            "Matched Signatures"
        ])

        for result in results:

            matches = ", ".join(
                result.get("matches", [])
            )

            writer.writerow([
                result["method"],
                result["status"],
                matches
            ])

    return output_path