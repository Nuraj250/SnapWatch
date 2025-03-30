from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
import os

from screenshot import take_screenshot
from ocr import perform_ocr, perform_ocr_and_log
from capture_scheduler import CaptureScheduler

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

SCREENSHOT_DIR = os.path.join("static", "screenshots")
scheduler = CaptureScheduler(interval=10)  # Set default interval (in seconds)

@app.route("/screenshot", methods=["POST"])
def screenshot():
    filename = take_screenshot()
    do_ocr = request.json.get("ocr", False)

    response = {"filename": filename}

    if do_ocr:
        text = perform_ocr_and_log(filename)
        response["ocr_text"] = text

    return jsonify(response)

@app.route("/screenshots", methods=["GET"])
def list_screenshots():
    files = sorted(os.listdir(SCREENSHOT_DIR), reverse=True)
    return jsonify(files)

@app.route("/screenshot/<filename>")
def serve_screenshot(filename):
    return send_from_directory(SCREENSHOT_DIR, filename)

@app.route("/ocr/<filename>", methods=["GET"])
def get_ocr(filename):
    image_path = os.path.join(SCREENSHOT_DIR, filename)
    text = perform_ocr(image_path)
    return jsonify({"text": text})

@app.route("/start", methods=["POST"])
def start_auto_capture():
    ocr_enabled = request.json.get("ocr", False)
    scheduler.start(ocr_enabled=ocr_enabled)
    return jsonify({"status": "started", "ocr": ocr_enabled})

@app.route("/stop", methods=["POST"])
def stop_auto_capture():
    scheduler.stop()
    return jsonify({"status": "stopped"})

if __name__ == "__main__":
    app.run(debug=True)
