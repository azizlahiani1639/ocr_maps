import json
from paddleocr import PaddleOCR
import cv2
import os

ocr_model = PaddleOCR(lang='en', use_angle_cls=True, use_gpu=False)
img_path = 'Genova.png'
result = ocr_model.ocr(img_path)
output_data = []
for line in result[0]:
    entry = {
        'bounding_box': line[0],
        'text': line[1][0],
        'confidence': line[1][1]
    }
    output_data.append(entry)

output_path = 'ocr_output.json'
with open(output_path, 'w') as f:
    json.dump(output_data, f, indent=4)

print(f"OCR results saved to {output_path}")
