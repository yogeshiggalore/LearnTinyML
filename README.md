# LearnTinyML

A hands-on learning platform for **Embedded Machine Learning (TinyML)** — designed for students and professionals.

Before diving into ML on microcontrollers, this platform builds a strong foundation through three prerequisite courses covering audio, vision, and motion sensing.

## Courses

```
TinyVox  (Audio)  ──┐
TinyVue  (Vision) ──┼──> TinyML (Machine Learning on Edge)
TinyVibe (Motion) ──┘
```

### TinyVox — *"From Sound Waves to Smart Ears"*
Embedded audio fundamentals: physics of sound, digital audio, FFT, filters, microphone technologies, and real-time audio processing on microcontrollers.

### TinyVue — *"From Photons to Perception"*
Embedded vision fundamentals: physics of light, color science, image processing, camera sensors, and real-time image processing on microcontrollers.

### TinyVibe — *"From Movement to Meaning"*
Embedded motion sensing fundamentals: physics of motion, magnetism, sensor fusion, accelerometers, gyroscopes, magnetometers, and IMU integration on microcontrollers.

## What Each Course Covers

| Part | Content |
|------|---------|
| Theory | Physics, math, and signal processing foundations |
| Working Principles | How sensors and hardware work internally |
| Firmware | Code to integrate and test on real hardware |
| Projects | Hands-on projects to solidify learning |

## Hardware

| Course | MCU | Sensors / Peripherals |
|--------|-----|-----------------------|
| TinyVox | XIAO ESP32-S3 / nRF54L15 | 2x INMP441 (I2S mic), MAX98357A (I2S amp), 4 Ohm speaker |
| TinyVue | XIAO ESP32-S3 Sense | Onboard OV2640 camera, PDM mic, SD card |
| TinyVibe | XIAO ESP32-S3 / nRF54L15 | ICM-20948 (9-DoF IMU), W25Q128 (16MB SPI flash) |

See [documents/hardware.md](documents/hardware.md) for full BOM and component details.

## Frameworks

1. **Zephyr RTOS** — Primary (portable, RTOS features, upstream support)
2. **Arduino** — Secondary (beginner-friendly, rapid prototyping)
3. **ESP-IDF** — Fallback (ESP32-specific features when needed)

## Documentation

- Web-based interactive documentation hosted on GitHub Pages
- Python backend for real-time data visualization and serial tools
- Jupyter notebooks for theory demonstrations

## Repository Structure

```
LearnTinyML/
├── app.py              # Flask backend server
├── data.py             # Course data (modules, BOM, outlines)
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Main HTML page
├── static/
│   ├── css/
│   │   └── style.css   # Styling
│   └── js/
│       └── app.js      # Frontend logic
├── documents/
│   ├── course.md       # Detailed course outline
│   ├── naming.md       # Course naming rationale
│   ├── hardware.md     # Bill of materials per course
│   └── claude_context.txt
└── README.md
```

## Running the Web App

```bash
pip install -r requirements.txt
python app.py
```

Open http://localhost:5000 in your browser.

## License

TBD
