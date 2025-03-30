import React from 'react';

export default function ScreenshotGallery({ screenshots, onSelect }) {
  return (
    <div className="gallery">
      <h3>📂 Captured Screenshots</h3>
      <div className="images">
        {screenshots.map((file) => (
          <img
            key={file}
            src={`http://localhost:5000/screenshot/${file}`}
            alt={file}
            onClick={() => onSelect(file)}
          />
        ))}
      </div>
    </div>
  );
}
