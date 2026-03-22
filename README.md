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

| Board | MCU | Key Features |
|-------|-----|-------------|
| XIAO ESP32-S3 Sense | ESP32-S3 | Camera (OV2640), PDM Mic, WiFi/BLE, 8MB PSRAM |
| XIAO nRF54L15 | nRF54L15 | BLE, Ultra-low power, PDM Mic support |
| XIAO MG24 | EFR32MG24 | BLE/Zigbee/Thread, AI/ML accelerator |

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
├── documents/          # Course plans and naming documentation
│   ├── course.md       # Detailed course outline
│   ├── naming.md       # Course naming rationale
│   └── claude_context.txt
└── README.md
```

## License

TBD
