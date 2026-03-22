# LearnTinyML - Course Plan

## Course Names

| Course | Name | Full Name | Tagline |
|--------|------|-----------|---------|
| Audio/Voice | **TinyVox** | Vox = Voice (Latin) | _"From Sound Waves to Smart Ears"_ |
| Vision/Camera | **TinyVue** | Vue = Vision (French) | _"From Photons to Perception"_ |
| Motion/IMU | **TinyVibe** | Vibe = Vibration | _"From Movement to Meaning"_ |

> All three names share the **Tiny** prefix (aligning with TinyML) and start with **V** for cohesive branding.

---

## Target Hardware

| Board | MCU | Used In |
|-------|-----|---------|
| XIAO ESP32-S3 | ESP32-S3 | TinyVox, TinyVibe |
| XIAO ESP32-S3 Sense | ESP32-S3 | TinyVue (onboard OV2640 camera) |
| XIAO nRF54L15 | nRF54L15 | TinyVox, TinyVibe |

See [hardware.md](documents/hardware.md) for full BOM per course.

## Frameworks (Priority Order)
1. **Zephyr RTOS** - Primary (portable, RTOS features, upstream support)
2. **Arduino** - Secondary (beginner-friendly, rapid prototyping)
3. **ESP-IDF** - Fallback (ESP32-specific features when needed)

---

# Course 1: TinyVox (Audio/Voice)

## Book Title: *"TinyVox: Embedded Audio - From Sound Waves to Smart Listening"*

### Part I: Theory of Sound & Audio

#### Chapter 1: Physics of Sound
- 1.1 What is sound? Longitudinal pressure waves
- 1.2 Frequency, wavelength, amplitude, phase
- 1.3 Speed of sound in different media
- 1.4 Superposition, interference, and standing waves
- 1.5 Resonance and harmonics
- 1.6 Sound intensity, decibels (dB), and the inverse square law
- 1.7 Human hearing range (20 Hz - 20 kHz) and perception
- 1.8 Psychoacoustics: loudness, pitch, timbre

#### Chapter 2: Digital Audio Fundamentals
- 2.1 Analog vs digital signals
- 2.2 Sampling theorem (Nyquist-Shannon)
- 2.3 Sampling rate, bit depth, quantization
- 2.4 Aliasing and anti-aliasing filters
- 2.5 PCM, PDM, and I2S data formats
- 2.6 Audio codecs overview (PCM, ADPCM, Opus)
- 2.7 Signal-to-noise ratio (SNR) and dynamic range
- 2.8 Practical: What sample rate and bit depth do we need for embedded?

#### Chapter 3: Frequency Domain Analysis
- 3.1 Why frequency domain? Time vs frequency representation
- 3.2 Fourier Transform - intuition and math
- 3.3 Discrete Fourier Transform (DFT)
- 3.4 Fast Fourier Transform (FFT) - algorithm and complexity
- 3.5 Windowing functions (Hann, Hamming, Blackman)
- 3.6 Spectrograms and Short-Time Fourier Transform (STFT)
- 3.7 Mel-Frequency Cepstral Coefficients (MFCCs)
- 3.8 Power spectral density
- 3.9 Practical FFT on microcontrollers (CMSIS-DSP, ESP-DSP)

#### Chapter 4: Audio Filters & Signal Processing
- 4.1 Filter types: low-pass, high-pass, band-pass, notch
- 4.2 FIR vs IIR filters
- 4.3 Filter design basics (cutoff, order, roll-off)
- 4.4 Digital filter implementation on MCUs
- 4.5 Noise reduction techniques for embedded
- 4.6 Automatic Gain Control (AGC)
- 4.7 Voice Activity Detection (VAD) - non-ML approach
- 4.8 Echo cancellation basics

### Part II: Audio Hardware & Working Principles

#### Chapter 5: Microphone Technologies
- 5.1 Electret Condenser Microphones (ECM)
- 5.2 MEMS Microphones - construction and working
- 5.3 Analog vs Digital MEMS microphones
- 5.4 PDM microphones - how PDM encoding works
- 5.5 I2S microphones - interface and timing
- 5.6 Microphone specifications: sensitivity, SNR, frequency response, AOP
- 5.7 Microphone arrays and beamforming basics
- 5.8 Selecting the right microphone for TinyML

#### Chapter 6: Audio Output - Speakers & DACs
- 6.1 Speaker types and working principles
- 6.2 DAC fundamentals
- 6.3 I2S DAC modules (MAX98357, PCM5102)
- 6.4 PWM audio output
- 6.5 Class-D amplifiers
- 6.6 Audio codec ICs (WM8960, ES8388)

### Part III: Firmware Implementation

#### Chapter 7: Audio Capture on ESP32-S3 (XIAO)
- 7.1 PDM microphone on XIAO ESP32-S3 Sense
- 7.2 I2S peripheral configuration
- 7.3 **Zephyr:** I2S driver, PDM/PCM capture, DMA buffers
- 7.4 **Arduino:** I2S library, simple recording sketch
- 7.5 **ESP-IDF:** I2S driver (new API), ring buffers
- 7.6 Circular buffer design for real-time audio
- 7.7 Storing audio to SD card (WAV file format)
- 7.8 Streaming audio over BLE/WiFi

#### Chapter 8: Audio Capture on nRF54L15 (XIAO)
- 8.1 nRF PDM peripheral
- 8.2 **Zephyr:** nrfx PDM driver integration
- 8.3 EasyDMA and double buffering
- 8.4 Low-power audio capture strategies
- 8.5 BLE audio streaming (LE Audio concepts)

#### Chapter 9: Real-Time Audio Processing on MCU
- 9.1 FFT on ESP32-S3 (CMSIS-DSP vs ESP-DSP)
- 9.2 Real-time spectrogram generation
- 9.3 MFCC computation on MCU
- 9.4 Digital filter implementation (CMSIS-DSP biquad)
- 9.5 Audio feature extraction pipeline
- 9.6 Memory and CPU budget for audio processing
- 9.7 Lab: Build a real-time audio spectrum analyzer

### Part IV: Projects & Preparation for ML

#### Chapter 10: Audio Projects (Pre-ML)
- 10.1 Project: Sound level meter with dB display
- 10.2 Project: Audio recorder with playback
- 10.3 Project: Tone/frequency detector (DTMF decoder)
- 10.4 Project: Simple clap detector using threshold + timing
- 10.5 Project: Audio streaming over WiFi (web interface)
- 10.6 Project: Guitar tuner using FFT
- 10.7 What's next: Audio features as ML input

---

# Course 2: TinyVue (Vision/Camera)

## Book Title: *"TinyVue: Embedded Vision - From Photons to Pixel Intelligence"*

### Part I: Theory of Light & Vision

#### Chapter 1: Physics of Light
- 1.1 Electromagnetic spectrum and visible light
- 1.2 Wave-particle duality (photons)
- 1.3 Wavelength, frequency, and energy
- 1.4 Reflection, refraction, and Snell's law
- 1.5 Lenses: convex, concave, focal length, aperture
- 1.6 Thin lens equation and magnification
- 1.7 Depth of field and f-number
- 1.8 Diffraction limit and resolution

#### Chapter 2: Color Science
- 2.1 How humans perceive color (cones, rods)
- 2.2 Additive color model (RGB)
- 2.3 Color spaces: RGB, HSV, YUV/YCbCr, Grayscale
- 2.4 Color temperature and white balance
- 2.5 Gamma correction
- 2.6 Why YUV matters for embedded (chroma subsampling)
- 2.7 Color depth: 8-bit, 16-bit (RGB565), 24-bit

#### Chapter 3: Digital Image Fundamentals
- 3.1 Pixels, resolution, and aspect ratio
- 3.2 Image as a matrix (grayscale and multi-channel)
- 3.3 Image file formats: BMP, JPEG, PNG
- 3.4 JPEG compression: DCT, quantization, Huffman
- 3.5 Image histogram and contrast
- 3.6 Coordinate systems and pixel addressing
- 3.7 Memory requirements: resolution x color depth calculations
- 3.8 Frame rate, bandwidth, and throughput considerations

#### Chapter 4: Image Processing Fundamentals
- 4.1 Point operations: brightness, contrast, thresholding
- 4.2 Convolution and kernels
- 4.3 Spatial filters: blur, sharpen, edge detection
- 4.4 Sobel, Prewitt, and Canny edge detectors
- 4.5 Morphological operations: erosion, dilation, opening, closing
- 4.6 Image resizing and interpolation (nearest, bilinear)
- 4.7 Histogram equalization
- 4.8 Connected component analysis
- 4.9 Practical: Which operations are feasible on MCUs?

#### Chapter 5: Feature Detection (Classical)
- 5.1 What are features? Corners, edges, blobs
- 5.2 Harris corner detection
- 5.3 FAST feature detector (designed for real-time)
- 5.4 BRIEF and ORB descriptors
- 5.5 Template matching
- 5.6 Hough transform (line and circle detection)
- 5.7 Optical flow basics (Lucas-Kanade)
- 5.8 Background subtraction
- 5.9 Why classical CV still matters for TinyML

### Part II: Camera Hardware & Working Principles

#### Chapter 6: Image Sensor Technologies
- 6.1 CCD vs CMOS sensors
- 6.2 Bayer filter pattern and demosaicing
- 6.3 Rolling shutter vs global shutter
- 6.4 Sensor specifications: resolution, pixel size, sensitivity, dynamic range
- 6.5 OV2640 sensor deep dive (used in XIAO ESP32-S3 Sense)
- 6.6 OV5640 and other common sensors
- 6.7 Infrared sensors and thermal cameras (AMG8833, MLX90640)
- 6.8 Time-of-Flight (ToF) sensors

#### Chapter 7: Camera Interfaces & Data Flow
- 7.1 DVP (Digital Video Port) / parallel interface
- 7.2 MIPI CSI-2 interface
- 7.3 SPI cameras (e.g., Arducam SPI)
- 7.4 USB cameras (UVC)
- 7.5 SCCB/I2C for camera register configuration
- 7.6 DMA and frame buffer management
- 7.7 Image output formats: RGB565, YUV422, JPEG
- 7.8 Camera control: exposure, gain, white balance registers

### Part III: Firmware Implementation

#### Chapter 8: Camera on ESP32-S3 (XIAO Sense)
- 8.1 OV2640 on XIAO ESP32-S3 Sense: pin mapping and schematic
- 8.2 **ESP-IDF:** esp_camera driver, frame buffer management
- 8.3 **Arduino:** ESP32 Camera library, basic capture
- 8.4 **Zephyr:** Video subsystem, camera driver (if available)
- 8.5 Resolution and format selection trade-offs
- 8.6 JPEG capture and storage to SD card
- 8.7 Frame rate optimization techniques
- 8.8 Memory management: PSRAM for frame buffers

#### Chapter 9: Image Processing on MCU
- 9.1 Grayscale conversion on MCU
- 9.2 Image downscaling for ML input
- 9.3 Real-time edge detection implementation
- 9.4 Histogram computation
- 9.5 Simple motion detection (frame differencing)
- 9.6 Color tracking (HSV thresholding)
- 9.7 ROI (Region of Interest) extraction
- 9.8 CPU and memory profiling for image operations

#### Chapter 10: Camera Streaming & Display
- 10.1 HTTP MJPEG streaming (web server)
- 10.2 WebSocket-based streaming
- 10.3 LVGL display integration (SPI LCD)
- 10.4 BLE image transfer (chunked)

### Part IV: Projects & Preparation for ML

#### Chapter 11: Vision Projects (Pre-ML)
- 11.1 Project: Time-lapse camera with SD card storage
- 11.2 Project: Motion-triggered camera (frame differencing)
- 11.3 Project: Color-based object tracker
- 11.4 Project: QR/Barcode reader (using Quirc library)
- 11.5 Project: Web-based camera dashboard with controls
- 11.6 Project: Simple line-following robot (threshold-based)
- 11.7 What's next: Image features as ML input

---

# Course 3: TinyVibe (Motion/IMU)

## Book Title: *"TinyVibe: Embedded Motion Sensing - From Inertia to Intelligence"*

### Part I: Theory of Motion & Inertial Sensing

#### Chapter 1: Physics of Motion
- 1.1 Newton's laws of motion
- 1.2 Linear motion: displacement, velocity, acceleration
- 1.3 Rotational motion: angular displacement, velocity, acceleration
- 1.4 Frames of reference and coordinate systems
- 1.5 Gravity and gravitational acceleration
- 1.6 Centripetal and Coriolis forces
- 1.7 Degrees of freedom (6-DoF, 9-DoF)
- 1.8 Rigid body dynamics basics

#### Chapter 2: Earth's Magnetic Field & Magnetism
- 2.1 Earth's magnetic field: declination, inclination, intensity
- 2.2 Magnetic field units (Tesla, Gauss)
- 2.3 Hard iron vs soft iron distortion
- 2.4 Magnetic interference in embedded systems
- 2.5 True north vs magnetic north
- 2.6 World Magnetic Model (WMM)

#### Chapter 3: Sensor Mathematics
- 3.1 Vectors and vector operations
- 3.2 Rotation representations: Euler angles, rotation matrices
- 3.3 Quaternions - intuition and math
- 3.4 Gimbal lock and why quaternions matter
- 3.5 Coordinate frame transformations
- 3.6 Sensor noise: white noise, bias, drift, random walk
- 3.7 Allan variance for noise characterization
- 3.8 Statistical basics: mean, variance, standard deviation for sensor data

#### Chapter 4: Sensor Fusion Theory
- 4.1 Why single sensors are not enough
- 4.2 Complementary filter - intuition and implementation
- 4.3 Kalman filter - intuition (state, prediction, update)
- 4.4 Extended Kalman Filter (EKF) for nonlinear systems
- 4.5 Madgwick filter (AHRS) - computationally efficient
- 4.6 Mahony filter
- 4.7 Comparison: complementary vs Kalman vs Madgwick
- 4.8 Choosing the right filter for MCU constraints

#### Chapter 5: Motion Signal Processing
- 5.1 Low-pass, high-pass filtering for IMU data
- 5.2 Moving average and exponential smoothing
- 5.3 Gravity removal from accelerometer
- 5.4 Integration: acceleration to velocity to position (and its problems)
- 5.5 Gyroscope drift compensation
- 5.6 Peak detection algorithms
- 5.7 Zero-crossing detection
- 5.8 Activity segmentation (windowing)
- 5.9 Feature extraction: RMS, energy, zero-crossings, dominant frequency

### Part II: Sensor Hardware & Working Principles

#### Chapter 6: Accelerometers
- 6.1 MEMS accelerometer working principle (capacitive, proof mass)
- 6.2 Specifications: range (g), sensitivity, bandwidth, noise density
- 6.3 Digital output: I2C/SPI registers
- 6.4 Built-in features: tap detection, free-fall, orientation
- 6.5 Common accelerometers: LIS2DH12, ADXL345, MC3419
- 6.6 High-g vs low-g accelerometers
- 6.7 Accelerometer as tilt sensor (using gravity vector)

#### Chapter 7: Gyroscopes
- 7.1 MEMS gyroscope working principle (Coriolis effect, vibrating mass)
- 7.2 Specifications: range (dps), sensitivity, bias stability, noise
- 7.3 Gyroscope drift and its causes
- 7.4 Angular rate vs angular position
- 7.5 Common gyroscopes and IMU combos

#### Chapter 8: Magnetometers
- 8.1 Hall-effect magnetometers
- 8.2 Magnetoresistive sensors (AMR, GMR, TMR)
- 8.3 Fluxgate magnetometers
- 8.4 Specifications: range, sensitivity, resolution, noise
- 8.5 Magnetic compass implementation
- 8.6 Tilt-compensated compass (combining accel + mag)
- 8.7 Magnetometer calibration: hard iron and soft iron compensation
- 8.8 Common magnetometers: LIS2MDL, MMC5603, QMC5883L

#### Chapter 9: IMU (Inertial Measurement Unit) Modules
- 9.1 What makes an IMU? (accel + gyro, optionally mag)
- 9.2 6-DoF IMUs: LSM6DSO, ICM-42688-P, BMI270
- 9.3 9-DoF IMUs: ICM-20948, BNO055 (with built-in fusion)
- 9.4 IMU on XIAO boards (built-in and external)
- 9.5 I2C vs SPI for IMU communication
- 9.6 FIFO buffers and data-ready interrupts
- 9.7 IMU placement and mounting considerations
- 9.8 Calibration procedures: bias, scale factor, cross-axis

### Part III: Firmware Implementation

#### Chapter 10: IMU on ESP32-S3 (XIAO)
- 10.1 Connecting external IMU (LSM6DSO / ICM-42688-P) via I2C/SPI
- 10.2 **Zephyr:** Sensor subsystem, sensor_channel API, triggers
- 10.3 **Arduino:** Wire library, register-level and library-based access
- 10.4 **ESP-IDF:** I2C master driver, raw register access
- 10.5 Data rate configuration and FIFO usage
- 10.6 Interrupt-driven vs polled data acquisition

#### Chapter 11: IMU on nRF54L15 (XIAO)
- 11.1 I2C/SPI on nRF54L15
- 11.2 **Zephyr:** Device tree bindings for IMU sensors
- 11.3 Low-power motion sensing (wake-on-motion)
- 11.4 BLE motion data streaming

#### Chapter 12: Sensor Fusion Implementation on MCU
- 12.1 Complementary filter in C (step-by-step)
- 12.2 Madgwick filter implementation
- 12.3 Calibration routine implementation
- 12.4 Real-time orientation visualization (web dashboard)
- 12.5 Heading/compass implementation with tilt compensation
- 12.6 Step counter using accelerometer
- 12.7 Performance comparison: CPU cycles per fusion update

### Part IV: Projects & Preparation for ML

#### Chapter 13: Motion Projects (Pre-ML)
- 13.1 Project: Digital spirit level with display
- 13.2 Project: Pedometer/step counter
- 13.3 Project: Compass with tilt compensation
- 13.4 Project: Gesture logger (record & visualize on web dashboard)
- 13.5 Project: Fall detection using threshold-based algorithm
- 13.6 Project: Dead reckoning position tracker (illustrating drift problem)
- 13.7 Project: Motion-triggered wake-up system (ultra-low power)
- 13.8 What's next: Motion features as ML input

---

# Cross-Course Infrastructure

## Web Platform (GitHub Pages + Python Backend)

### Documentation Site
- Static site generator (MkDocs Material or Docusaurus)
- Interactive code examples with syntax highlighting
- Embedded waveform/signal visualizers (Web Audio API, Canvas)
- 3D sensor visualization (Three.js for IMU orientation)
- GitHub Pages deployment via CI/CD

### Python Backend (for interactive features)
- Flask/FastAPI server for:
  - Serial data receiver (from MCU via USB)
  - Real-time data plotting (WebSocket -> browser charts)
  - Audio/image upload and processing demos
  - Dataset collection tools (for future ML courses)
- Jupyter notebooks for theory demonstrations

### Tools & Utilities
- Python scripts for sensor data visualization
- Web-based serial monitor (Web Serial API)
- Firmware flashing guides per board
- Bill of materials (BOM) for each course

---

# Theory Depth Guide

| Audience | Theory Level | Math | Code Focus |
|----------|-------------|------|-----------|
| **Student (beginner)** | Intuition + visuals, minimal math | Algebra, basic trig | Arduino examples first |
| **Student (advanced)** | Full derivations, proofs | Linear algebra, calculus | Zephyr + register-level |
| **Professional** | Applied theory, trade-offs | As needed for design | All frameworks, optimization |

Each chapter should include:
1. **Concept** - What and why
2. **Theory** - Math and physics (with visual diagrams)
3. **Practical** - Firmware code implementing the concept
4. **Exercise** - Hands-on task for the reader
5. **Quiz** - Self-assessment questions

---

# Suggested Learning Path

```
TinyVox  (Audio)  ──┐
TinyVue  (Vision) ──┼──> TinyML (Machine Learning on Edge)
TinyVibe (Motion) ──┘
```

Students can take courses in any order, but all three should be completed before the TinyML course.
