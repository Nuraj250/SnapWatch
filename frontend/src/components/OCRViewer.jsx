import React from 'react';

export default function OCRViewer({ filename, text }) {
  return (
    <div className="ocr-viewer">
      <h3>📝 OCR Result - {filename}</h3>
      <pre>{text || "No text detected."}</pre>
    </div>
  );
}
