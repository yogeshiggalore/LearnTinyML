# LearnTinyML - Hardware Bill of Materials (BOM)

## TinyVox (Audio/Voice)

| # | Component | Description | Qty | Interface |
|---|-----------|-------------|-----|-----------|
| 1 | XIAO ESP32-S3 | Main MCU board (WiFi/BLE, 8MB PSRAM) | 1 | - |
| 2 | XIAO nRF54L15 | Alternate MCU board (BLE, ultra-low power) | 1 | - |
| 3 | INMP441 | I2S MEMS digital microphone | 2 | I2S |
| 4 | MAX98357A | I2S Class-D mono amplifier | 1 | I2S |
| 5 | 4 Ohm Speaker | Small speaker for audio output | 1 | via MAX98357A |

### TinyVox Notes
- Two INMP441 microphones enable stereo capture and beamforming experiments
- INMP441 is I2S output (not PDM), provides 24-bit audio data
- MAX98357A is an I2S input Class-D amplifier — no DAC needed, direct digital to speaker
- Audio path: **Mic (INMP441) -> I2S -> MCU -> I2S -> MAX98357A -> Speaker**

---

## TinyVue (Vision/Camera)

| # | Component | Description | Qty | Interface |
|---|-----------|-------------|-----|-----------|
| 1 | XIAO ESP32-S3 Sense | MCU board with onboard OV2640 camera and PDM mic | 1 | - |

### TinyVue Notes
- XIAO ESP32-S3 Sense has the OV2640 camera module built-in (no external wiring)
- OV2640: 2MP, supports JPEG/RGB565/YUV422, max 1600x1200
- Board also includes onboard PDM microphone and SD card slot
- 8MB PSRAM available for frame buffers

---

## TinyVibe (Motion/IMU)

| # | Component | Description | Qty | Interface |
|---|-----------|-------------|-----|-----------|
| 1 | XIAO ESP32-S3 | Main MCU board (WiFi/BLE, 8MB PSRAM) | 1 | - |
| 2 | XIAO nRF54L15 | Alternate MCU board (BLE, ultra-low power) | 1 | - |
| 3 | ICM-20948 | 9-DoF IMU (accel + gyro + mag) | 1 | I2C / SPI |
| 4 | W25Q128 | 128Mbit (16MB) external SPI NOR flash | 1 | SPI |

### TinyVibe Notes
- ICM-20948 is a 9-DoF IMU from TDK InvenSense:
  - Accelerometer: +/-2g, 4g, 8g, 16g
  - Gyroscope: +/-250, 500, 1000, 2000 dps
  - Magnetometer: AK09916 (built-in), +/-4900 uT
  - Built-in DMP (Digital Motion Processor) for on-chip sensor fusion
  - I2C (up to 400kHz) and SPI (up to 7MHz)
- W25Q128 external flash for:
  - Data logging (high-speed motion capture sessions)
  - Storing calibration data
  - Recording sensor datasets for offline analysis / future ML training

---

## Common Accessories (Recommended)

| Component | Purpose |
|-----------|---------|
| Breadboard | Prototyping |
| Jumper wires | Connections |
| USB-C cable | Programming and power |
| Micro SD card (16GB+) | Data storage (TinyVue, TinyVox) |
| SPI/I2C OLED display (SSD1306) | Optional: real-time data display |

---

## Hardware Summary

```
TinyVox:  XIAO ESP32-S3/nRF54L15 + 2x INMP441 + MAX98357A + Speaker
TinyVue:  XIAO ESP32-S3 Sense (all-in-one: camera + mic + SD)
TinyVibe: XIAO ESP32-S3/nRF54L15 + ICM-20948 + W25Q128
```
