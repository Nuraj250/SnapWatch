import os
from datetime import datetime
from PIL import ImageGrab

SCREENSHOT_DIR = os.path.join("static", "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def take_screenshot():
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshot_{now}.png"
    filepath = os.path.join(SCREENSHOT_DIR, filename)

    img = ImageGrab.grab()
    img.save(filepath)

    return filename
