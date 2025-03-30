import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Header from './components/Header';
import ControlPanel from './components/ControlPanel';
import ScreenshotGallery from './components/ScreenshotGallery';
import OCRViewer from './components/OCRViewer';
import './styles/app.css';

const API_BASE = 'http://localhost:5000';

function App() {
  const [screenshots, setScreenshots] = useState([]);
  const [selected, setSelected] = useState(null);
  const [ocrText, setOcrText] = useState("");
  const [ocrEnabled, setOcrEnabled] = useState(true);
  const [isCapturing, setIsCapturing] = useState(false);

  const fetchScreenshots = async () => {
    const res = await axios.get(`${API_BASE}/screenshots`);
    setScreenshots(res.data);
  };

  const takeScreenshot = async () => {
    await axios.post(`${API_BASE}/screenshot`, { ocr: ocrEnabled });
    fetchScreenshots();
  };

  const toggleAutoCapture = async () => {
    if (isCapturing) {
      await axios.post(`${API_BASE}/stop`);
      setIsCapturing(false);
    } else {
      await axios.post(`${API_BASE}/start`, { ocr: ocrEnabled });
      setIsCapturing(true);
    }
  };

  const viewOCR = async (filename) => {
    const res = await axios.get(`${API_BASE}/ocr/${filename}`);
    setSelected(filename);
    setOcrText(res.data.text);
  };

  useEffect(() => {
    fetchScreenshots();
  }, []);

  return (
    <div className="app-container">
      <Header />
      <ControlPanel
        ocrEnabled={ocrEnabled}
        setOcrEnabled={setOcrEnabled}
        takeScreenshot={takeScreenshot}
        toggleAutoCapture={toggleAutoCapture}
        isCapturing={isCapturing}
      />
      <ScreenshotGallery screenshots={screenshots} onSelect={viewOCR} />
      {selected && <OCRViewer filename={selected} text={ocrText} />}
    </div>
  );
}

export default App;
