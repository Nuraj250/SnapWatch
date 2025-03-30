import React from 'react';

export default function ControlPanel({ ocrEnabled, setOcrEnabled, takeScreenshot, toggleAutoCapture, isCapturing }) {
  return (
    <div className="control-panel">
      <button onClick={takeScreenshot}>📷 Capture Now</button>
      <button onClick={toggleAutoCapture}>
        {isCapturing ? "🛑 Stop Auto-Capture" : "▶️ Start Auto-Capture"}
      </button>
      <label>
        <input
          type="checkbox"
          checked={ocrEnabled}
          onChange={() => setOcrEnabled(!ocrEnabled)}
        />
        Enable OCR
      </label>
    </div>
  );
}
