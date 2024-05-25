import json
from paddleocr import PaddleOCR
import cv2
import os

# Initialize PaddleOCR with English language, angle detection, and CPU usage
ocr_model = PaddleOCR(lang='en', use_angle_cls=True, use_gpu=False)

# Set the image path
img_path = 'Genova.png'

# Perform OCR on the image
result = ocr_model.ocr(img_path)

# Extract detected components
output_data = []
for line in result[0]:
    entry = {
        'bounding_box': line[0],
        'text': line[1][0],
        'confidence': line[1][1]
    }
    output_data.append(entry)

# Output result in JSON format
output_path = 'ocr_output.json'
with open(output_path, 'w') as f:
    json.dump(output_data, f, indent=4)

print(f"OCR results saved to {output_path}")
