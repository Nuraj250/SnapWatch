import pytesseract
from PIL import Image
import os
import csv
from datetime import datetime

LOG_FILE = os.path.join("data", "ocr_logs.csv")
os.makedirs("data", exist_ok=True)

def perform_ocr(image_path):
    if not os.path.exists(image_path):
        return None
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text.strip()

def perform_ocr_and_log(filename):
    image_path = os.path.join("static", "screenshots", filename)
    text = perform_ocr(image_path)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, filename, text])

    return text
