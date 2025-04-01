import os
import csv
from datetime import datetime
import easyocr

LOG_FILE = os.path.join("data", "ocr_logs.csv")
os.makedirs("data", exist_ok=True)

reader = easyocr.Reader(['en'])  # Only once

def perform_ocr(image_path):
    if not os.path.exists(image_path):
        return None
    result = reader.readtext(image_path, detail=0)
    return "\n".join(result)

def perform_ocr_and_log(filename):
    image_path = os.path.join("static", "screenshots", filename)
    text = perform_ocr(image_path)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, filename, text])

    return text
