import threading
import time
from screenshot import take_screenshot
from ocr import perform_ocr_and_log

class CaptureScheduler:
    def __init__(self, interval=10):
        self.interval = interval
        self.running = False
        self.thread = None

    def start(self, ocr_enabled=False):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._run, args=(ocr_enabled,))
            self.thread.start()

    def _run(self, ocr_enabled):
        while self.running:
            filename = take_screenshot()
            if ocr_enabled:
                perform_ocr_and_log(filename)
            time.sleep(self.interval)

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()
            self.thread = None
