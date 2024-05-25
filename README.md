# OCR Project

This project uses PaddleOCR to extract text from an image and outputs the results in JSON format.

## Setup

1. **Create a virtual environment and activate it**:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # On Windows
    ```

2. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the OCR script**:
    ```bash
    python ocr_script.py
    ```

The output will be saved to `ocr_output.json`.

## Dependencies

- paddlepaddle
- paddleocr
- opencv-python-headless
- matplotlib
- setuptools
