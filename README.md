<div align="center">

# 🛡️ Custom Payload Encoder & Obfuscation Framework

### Educational Cybersecurity Framework for Encoding, Obfuscation Analysis & Defensive Detection

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Security](https://img.shields.io/badge/Focus-Cybersecurity-red)
![Testing](https://img.shields.io/badge/Tests-9%20Passing-success)
![License](https://img.shields.io/badge/License-MIT-green)

</div>

---</div>

---

## 🏗️ Architecture

![Custom Payload Encoder & Obfuscation Framework Architecture](a_wide_dark_themed_infographic_diagram_with_neon.png)

The framework follows a defensive analysis workflow:

**Input → Encoding → Obfuscation → Detection → Analysis → Reporting**

# Custom Payload Encoder & Obfuscation Framework

A Python-based cybersecurity research and educational framework for studying encoding, string transformation, basic obfuscation techniques, defensive signature detection, and detection-rate analysis using safe and benign test strings.

---

## ⚠️ Ethical and Safety Notice

This project is designed strictly for educational, defensive cybersecurity research and authorized laboratory testing.

The framework uses benign test strings and simulated signatures. It does not contain real malware, shellcode, credential theft functionality, persistence mechanisms, or real antivirus/EDR bypass functionality.

Do not use this project to evade security controls, bypass antivirus/EDR systems, or conceal malicious software.

Use the framework only in systems and environments where you have explicit authorization.

---

## 📌 Project Overview

The Custom Payload Encoder & Obfuscation Framework demonstrates how different transformations can change the representation of a text string and how a simple signature-based detector responds to those transformations.

The framework provides:

- Base64 encoding and decoding
- XOR transformation
- ROT13 transformation
- String splitting
- Character insertion
- Hexadecimal escape representation
- Basic signature detection
- Normalized defensive detection
- Multi-layer transformation demonstration
- JSON report generation
- CSV report generation
- Automated unit testing
- Interactive command-line interface

The project demonstrates the following security workflow:

Original Data → Transformation → Detection → Analysis → Reporting

---

## 🎯 Project Objectives

1. Understand common text encoding techniques.
2. Understand reversible XOR transformations.
3. Understand ROT13 transformation.
4. Demonstrate basic string obfuscation techniques.
5. Understand how simple signature-based detection works.
6. Demonstrate limitations of exact string matching.
7. Implement normalized defensive detection.
8. Compare detection results before and after transformations.
9. Generate structured security analysis reports.
10. Build a modular cybersecurity research framework using Python.
11. Practice unit testing and software organization.
12. Demonstrate defensive cybersecurity research concepts.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Base64 | Text encoding |
| XOR | Reversible transformation |
| ROT13 | Text transformation |
| Regular Expressions | Text normalization |
| JSON | Report generation |
| CSV | Result export |
| unittest | Automated testing |
| PowerShell | Project execution |
| Visual Studio Code | Development environment |
| Git/GitHub | Version control |

---

## 🏗️ Project Architecture

    User Input
        |
        v
    Transformation
        |
        +---- Base64
        |
        +---- XOR
        |
        +---- ROT13
        |
        +---- String Split
        |
        +---- Character Insertion
        |
        +---- Hex Escape
        |
        v
    Simulated Signature Detector
        |
        +---- Basic Detection
        |
        +---- Normalized Detection
        |
        v
    Detection Analysis
        |
        v
    JSON / CSV Reporting

---

## 📂 Project Structure

    Custom-Payload-Encoder-Obfuscation-Framework/
    |
    +-- main.py
    +-- README.md
    +-- requirements.txt
    |
    +-- encoders/
    |   +-- __init__.py
    |   +-- base64_encoder.py
    |   +-- xor_encoder.py
    |   +-- rot13_encoder.py
    |
    +-- obfuscators/
    |   +-- __init__.py
    |   +-- string_splitter.py
    |   +-- char_insertion.py
    |   +-- escape_obfuscator.py
    |
    +-- detector/
    |   +-- __init__.py
    |   +-- signature_detector.py
    |
    +-- reporting/
    |   +-- __init__.py
    |   +-- report_generator.py
    |
    +-- tests/
    |   +-- test_framework.py
    |
    +-- samples/
    |   +-- test_payloads.txt
    |
    +-- reports/
        +-- analysis_report.json
        +-- detection_results.csv

---

# 🔐 Encoding and Transformation Techniques

## 1. Base64 Encoding

Base64 converts text into a printable ASCII representation.

Example:

    Original:
    TEST_SECURITY_STRING

    Base64:
    VEVTVF9TRUNVUklUWV9TVFJJTkc=

The framework supports both encoding and decoding.

### Module

`encoders/base64_encoder.py`

### Functions

`encode()`

`decode()`

---

## 2. XOR Transformation

XOR applies a bitwise XOR operation using a numeric key.

Example:

    Original:
    TEST_SECURITY_STRING

    Key:
    23

    Recovered:
    TEST_SECURITY_STRING

XOR is reversible when the same key is used.

### Module

`encoders/xor_encoder.py`

### Function

`xor_transform()`

The key is validated between `0 - 255`.

---

## 3. ROT13

ROT13 replaces alphabetic characters with the character 13 positions away in the alphabet.

Example:

    Original:
    TEST_SECURITY_STRING

    ROT13:
    GRFG_FRPHEVGL_FGEVAT

Applying ROT13 again returns the original text.

### Module

`encoders/rot13_encoder.py`

### Function

`transform()`

---

# 🧩 String Obfuscation Techniques

## 4. String Splitting

A string can be divided into smaller chunks.

Example:

    Original:

    TEST_SECURITY_STRING

    Chunks:

    TES
    T_S
    ECU
    RIT
    Y_S
    TRI
    NG

The chunks can be reconstructed to recover the original string.

### Module

`obfuscators/string_splitter.py`

### Functions

`split_string()`

`join_chunks()`

---

## 5. Character Insertion

The framework can insert a separator between characters.

Example:

    Original:

    TEST_SECURITY_STRING

    Transformed:

    T|E|S|T|_|S|E|C|U|R|I|T|Y|_|S|T|R|I|N|G

The separator can be removed to reconstruct the original string.

### Module

`obfuscators/char_insertion.py`

### Functions

`insert_separator()`

`remove_separator()`

---

## 6. Hexadecimal Escape Representation

Characters can be represented using hexadecimal escape sequences.

Example:

    T -> \x54
    E -> \x45
    S -> \x53
    T -> \x54

Example representation:

    \x54\x45\x53\x54

The framework can reconstruct the original text.

### Module

`obfuscators/escape_obfuscator.py`

### Functions

`to_hex_escape()`

`from_hex_escape()`

---

# 🛡️ Defensive Signature Detection

The project includes a simulated signature detector.

The detector searches for predefined benign test signatures.

Example:

    SIGNATURES = [
        "TEST_SECURITY_STRING",
        "DEMO_SIGNATURE_PATTERN",
    ]

The detector performs a basic case-insensitive comparison.

Example:

    Input:
    TEST_SECURITY_STRING

    Result:
    DETECTED

A transformed representation may produce:

    NOT DETECTED

This demonstrates a limitation of simple exact-string matching.

---

# 🔎 Normalized Defensive Detection

The project also implements a basic normalization approach.

The normalization process:

1. Converts text to lowercase.
2. Removes non-alphanumeric characters.
3. Compares the normalized text with normalized signatures.

Example:

    Original:

    TEST_SECURITY_STRING

Character insertion:

    T|E|S|T|_|S|E|C|U|R|I|T|Y|_|S|T|R|I|N|G

After normalization:

    TESTSECURITYSTRING

This allows the defensive detector to identify some formatting changes that a basic exact detector may miss.

---

# 🔬 Multi-Layer Transformation Demonstration

The framework demonstrates multiple transformations applied sequentially to a benign test string.

Example:

    Original Text
         |
         v
       ROT13
         |
         v
      Base64
         |
         v
      Base64
         |
         v
    Final Representation

This is included for educational analysis of data representation.

It is not intended for bypassing antivirus, EDR, or other security products.

---

# 📊 Detection Analysis

The framework compares detection results across different representations.

Example:

| Method | Detection |
|---|---|
| Original | DETECTED |
| Base64 | NOT DETECTED |
| XOR | NOT DETECTED |
| ROT13 | NOT DETECTED |
| String Split | NOT DETECTED |
| Character Insertion | NOT DETECTED |
| Escape Representation | NOT DETECTED |

The exact results depend on the test string and configured simulated signatures.

---

# 📈 Improved Detection

The project compares basic detection with normalized detection.

Example:

| Transformation | Basic Detector | Normalized Detector |
|---|---|---|
| Original | DETECTED | DETECTED |
| String Split | NOT DETECTED | DETECTED |
| Character Insertion | NOT DETECTED | DETECTED |

This demonstrates how defensive normalization can improve detection against simple formatting transformations.

---

# 📋 Reporting System

The framework automatically generates analysis reports.

Supported formats:

- JSON
- CSV

## JSON Report

Generated file:

`reports/analysis_report.json`

The JSON report contains:

- Project name
- Timestamp
- Total tests
- Number detected
- Number not detected
- Detection rate
- Individual test results

Example:

    {
        "project": "Custom Payload Encoder & Obfuscation Framework",
        "total_tests": 8,
        "detected": 1,
        "not_detected": 7,
        "detection_rate_percent": 12.5
    }

The exact values depend on the test input.

---

# 📑 CSV Report

Generated file:

`reports/detection_results.csv`

The CSV report contains:

- Method
- Detection Status
- Matched Signatures

The CSV file can be opened using:

- Microsoft Excel
- LibreOffice Calc
- Google Sheets
- Python pandas

---

# 🧪 Unit Testing

The project includes automated unit tests.

Test file:

`tests/test_framework.py`

The tests verify:

- Base64 encoding and decoding
- XOR transformation and recovery
- ROT13 transformation and recovery
- String splitting and reconstruction
- Character insertion and removal
- Hexadecimal escape conversion
- Signature detection
- No-match detection
- Normalized detection

Run the tests:

    python -m unittest discover -s tests -v

Expected result:

    Ran 9 tests

    OK

---

# 💻 Command-Line Interface

The framework provides an interactive command-line interface.

Run:

    python main.py

The menu provides:

    ========================================
     Custom Payload Encoder Framework
    ========================================

    1. Base64
    2. XOR
    3. ROT13
    4. String Split
    5. Character Insertion
    6. Escape Representation
    7. Run Complete Test Suite
    8. Improved Detection Test
    9. Exit

---

# ▶️ How to Run the Project

## Step 1: Open the Project

Open the project in Visual Studio Code.

    Custom-Payload-Encoder-Obfuscation-Framework

## Step 2: Create a Virtual Environment

Run:

    python -m venv venv

## Step 3: Activate the Virtual Environment

Windows PowerShell:

    .\venv\Scripts\Activate.ps1

After activation, you should see:

    (venv)

in the terminal.

## Step 4: Install Dependencies

Run:

    pip install -r requirements.txt

The project primarily uses Python standard-library modules.

## Step 5: Run Unit Tests

Run:

    python -m unittest discover -s tests -v

Expected:

    Ran 9 tests

    OK

## Step 6: Run the Framework

Run:

    python main.py

---

# 🧪 Example Test

Use a benign test string:

    TEST_SECURITY_STRING

Select:

    7. Run Complete Test Suite

The framework performs:

    Original Detection
           |
           v
    Base64
           |
           v
    XOR
           |
           v
    ROT13
           |
           v
    String Splitting
           |
           v
    Character Insertion
           |
           v
    Escape Representation
           |
           v
    Multi-Layer Transformation
           |
           v
    Detection Analysis
           |
           v
    Report Generation

---

# 📊 Example Output

    ========================================
     Running Complete Security Test Suite
    ========================================

    === Detection Result: Original ===
    Status  : DETECTED

    === Base64 Test ===
    Original : TEST_SECURITY_STRING
    Encoded  : VEVTVF9TRUNVUklUWV9TVFJJTkc=
    Decoded  : TEST_SECURITY_STRING

    === XOR Test ===
    Original : TEST_SECURITY_STRING
    Key      : 23
    Recovered: TEST_SECURITY_STRING

    === ROT13 Test ===
    Original : TEST_SECURITY_STRING
    ROT13    : GRFG_FRPHEVGL_FGEVAT
    Recovered: TEST_SECURITY_STRING

The exact output depends on the test input.

---

# 📁 Generated Files

After running the complete test suite:

    reports/
    |
    +-- analysis_report.json
    +-- detection_results.csv

These files can be used for:

- Project documentation
- Academic reports
- Data analysis
- Screenshots
- Presentation demonstrations

---

# 🧠 Key Cybersecurity Concepts Demonstrated

## Encoding

Encoding changes the representation of information without necessarily providing security.

Example:

`Base64`

## Transformation

A transformation modifies the representation of data.

Examples:

- XOR
- ROT13

## String Obfuscation

String obfuscation changes the structure or representation of text.

Examples:

- String splitting
- Character insertion
- Escape representation

## Signature-Based Detection

A signature detector searches for known patterns.

    Known Pattern
         |
         v
    Compare Input
         |
         v
       Match?
         |
         v
    DETECTED / NOT DETECTED

## Normalization

Normalization attempts to create a consistent representation before comparison.

    Original
       |
       v
    Lowercase
       |
       v
    Remove special characters
       |
       v
    Normalized representation
       |
       v
    Signature comparison

---

# 🏆 Project Highlights

- Modular Python architecture
- Multiple encoding techniques
- Multiple string transformation techniques
- Defensive signature detection
- Normalized detection
- Multi-layer transformation demonstration
- Automated testing
- JSON reporting
- CSV reporting
- Interactive CLI
- Safe cybersecurity laboratory environment
- Clear separation between transformation and detection modules

---

# 🔮 Future Enhancements

Possible future improvements include:

### 1. Graphical User Interface

Develop a GUI using Tkinter or a web interface using Flask.

### 2. Visualization

Add charts showing transformation methods, detection results, and detection rates.

### 3. Advanced Defensive Detection

Possible improvements:

- Pattern normalization
- Entropy analysis
- Token analysis
- Regex-based detection
- Multiple signature databases
- Statistical analysis
- Feature-based detection

### 4. Detection Dashboard

A dashboard could display:

- Total Tests
- Detected
- Not Detected
- Detection Rate

### 5. Additional Report Formats

Future versions could support:

- PDF
- HTML
- Excel

### 6. Test Dataset Support

A larger collection of benign cybersecurity test strings could be used to evaluate detection behavior under controlled laboratory conditions.

---

# 🔐 Security and Ethical Considerations

This project is intentionally limited to safe and controlled experimentation.

The project does not provide:

- Real malware
- Malware generation
- Shellcode
- Credential theft
- Persistence mechanisms
- Exploit deployment
- Real antivirus bypass
- Real EDR bypass
- Unauthorized access
- Malicious payload deployment

The goal is to understand cybersecurity concepts from both sides:

    Transformation Techniques
              +
       Defensive Detection
              =
    Security Research Understanding

---

# 🎓 Educational Value

This project provides practical experience in:

- Python programming
- Cybersecurity fundamentals
- Encoding
- Data transformation
- Obfuscation concepts
- Signature-based detection
- Defensive security
- Regular expressions
- File handling
- JSON
- CSV
- Unit testing
- CLI application development
- Software architecture
- Security research methodology

---

# 📌 Learning Outcomes

After completing this project, the developer should understand:

1. How common encoding techniques work.
2. How reversible transformations work.
3. How strings can be structurally transformed.
4. How basic signature detection works.
5. Why exact matching has limitations.
6. How normalization can improve defensive detection.
7. How to organize a Python cybersecurity project.
8. How to create automated tests.
9. How to generate structured reports.
10. How to document a cybersecurity research project professionally.

---

# 🧰 Requirements

Recommended environment:

- Python 3.10+
- Visual Studio Code
- Windows or Linux
- PowerShell or Terminal

The project primarily uses Python's standard library.

---

# 📜 License

This project is intended for educational and authorized cybersecurity research purposes.

Users are responsible for ensuring that any testing performed using this project complies with applicable laws, regulations, organizational policies, and authorization requirements.

---

# 👨‍💻 Author

**Mohammed Rukhnuddin Shariff**

Cybersecurity Enthusiast | Computer Science & Engineering

### Areas of Interest

- Cybersecurity
- Ethical Hacking
- Network Security
- SOC Operations
- Defensive Security
- Threat Detection
- Security Automation
- Python

---

# ⭐ Project Purpose

The purpose of this project is to demonstrate how different text representations affect simple signature-based detection and how defensive normalization techniques can improve detection.

    INPUT
      |
      v
    +---------------+
    | Transformation|
    +-------+-------+
            |
            v
    +---------------+
    |   Detection   |
    +-------+-------+
            |
            v
    +---------------+
    |    Analysis   |
    +-------+-------+
            |
            v
    +---------------+
    |   Reporting   |
    +---------------+

---

**Custom Payload Encoder & Obfuscation Framework — Educational Cybersecurity Research Project**
