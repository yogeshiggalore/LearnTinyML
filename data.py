MODULES = {
    "tinyvox": {
        "name": "TinyVox",
        "domain": "Audio / Voice",
        "tagline": "From Sound Waves to Smart Ears",
        "book_title": "TinyVox: Embedded Audio — From Sound Waves to Smart Listening",
        "color": "#6c5ce7",
        "icon": "tinyvox",
        "description": (
            "Embedded audio fundamentals: physics of sound, digital audio, FFT, "
            "filters, microphone technologies, and real-time audio processing on "
            "microcontrollers."
        ),
        "hardware": {
            "boards": ["XIAO ESP32-S3", "XIAO nRF54L15"],
            "summary": "XIAO ESP32-S3 / nRF54L15 + 2x INMP441 + MAX98357A + Speaker",
            "bom": [
                {"component": "XIAO ESP32-S3", "description": "Main MCU board (WiFi/BLE, 8MB PSRAM)", "qty": 1, "interface": "-"},
                {"component": "XIAO nRF54L15", "description": "Alternate MCU board (BLE, ultra-low power)", "qty": 1, "interface": "-"},
                {"component": "INMP441", "description": "I2S MEMS digital microphone", "qty": 2, "interface": "I2S"},
                {"component": "MAX98357A", "description": "I2S Class-D mono amplifier", "qty": 1, "interface": "I2S"},
                {"component": "4 Ohm Speaker", "description": "Small speaker for audio output", "qty": 1, "interface": "via MAX98357A"},
            ],
            "notes": [
                "Two INMP441 microphones enable stereo capture and beamforming experiments",
                "INMP441 is I2S output (not PDM), provides 24-bit audio data",
                "MAX98357A is an I2S input Class-D amplifier — no DAC needed, direct digital to speaker",
                "Audio path: Mic (INMP441) → I2S → MCU → I2S → MAX98357A → Speaker",
            ],
        },
        "outline": [
            {
                "part": "Part I: Theory of Sound & Audio",
                "chapters": [
                    {
                        "title": "Chapter 1: Physics of Sound",
                        "sections": [
                            "What is sound? Longitudinal pressure waves",
                            "Frequency, wavelength, amplitude, phase",
                            "Speed of sound in different media",
                            "Superposition, interference, and standing waves",
                            "Resonance and harmonics",
                            "Sound intensity, decibels (dB), and the inverse square law",
                            "Human hearing range (20 Hz – 20 kHz) and perception",
                            "Psychoacoustics: loudness, pitch, timbre",
                        ],
                    },
                    {
                        "title": "Chapter 2: Digital Audio Fundamentals",
                        "sections": [
                            "Analog vs digital signals",
                            "Sampling theorem (Nyquist-Shannon)",
                            "Sampling rate, bit depth, quantization",
                            "Aliasing and anti-aliasing filters",
                            "PCM, PDM, and I2S data formats",
                            "Audio codecs overview (PCM, ADPCM, Opus)",
                            "Signal-to-noise ratio (SNR) and dynamic range",
                            "Practical: What sample rate and bit depth do we need for embedded?",
                        ],
                    },
                    {
                        "title": "Chapter 3: Frequency Domain Analysis",
                        "sections": [
                            "Why frequency domain? Time vs frequency representation",
                            "Fourier Transform — intuition and math",
                            "Discrete Fourier Transform (DFT)",
                            "Fast Fourier Transform (FFT) — algorithm and complexity",
                            "Windowing functions (Hann, Hamming, Blackman)",
                            "Spectrograms and Short-Time Fourier Transform (STFT)",
                            "Mel-Frequency Cepstral Coefficients (MFCCs)",
                            "Power spectral density",
                            "Practical FFT on microcontrollers (CMSIS-DSP, ESP-DSP)",
                        ],
                    },
                    {
                        "title": "Chapter 4: Audio Filters & Signal Processing",
                        "sections": [
                            "Filter types: low-pass, high-pass, band-pass, notch",
                            "FIR vs IIR filters",
                            "Filter design basics (cutoff, order, roll-off)",
                            "Digital filter implementation on MCUs",
                            "Noise reduction techniques for embedded",
                            "Automatic Gain Control (AGC)",
                            "Voice Activity Detection (VAD) — non-ML approach",
                            "Echo cancellation basics",
                        ],
                    },
                ],
            },
            {
                "part": "Part II: Audio Hardware & Working Principles",
                "chapters": [
                    {
                        "title": "Chapter 5: Microphone Technologies",
                        "sections": [
                            "Electret Condenser Microphones (ECM)",
                            "MEMS Microphones — construction and working",
                            "Analog vs Digital MEMS microphones",
                            "PDM microphones — how PDM encoding works",
                            "I2S microphones — interface and timing",
                            "Microphone specifications: sensitivity, SNR, frequency response, AOP",
                            "Microphone arrays and beamforming basics",
                            "Selecting the right microphone for TinyML",
                        ],
                    },
                    {
                        "title": "Chapter 6: Audio Output — Speakers & DACs",
                        "sections": [
                            "Speaker types and working principles",
                            "DAC fundamentals",
                            "I2S DAC modules (MAX98357, PCM5102)",
                            "PWM audio output",
                            "Class-D amplifiers",
                            "Audio codec ICs (WM8960, ES8388)",
                        ],
                    },
                ],
            },
            {
                "part": "Part III: Firmware Implementation",
                "chapters": [
                    {
                        "title": "Chapter 7: Audio Capture on ESP32-S3 (XIAO)",
                        "sections": [
                            "PDM microphone on XIAO ESP32-S3 Sense",
                            "I2S peripheral configuration",
                            "Zephyr: I2S driver, PDM/PCM capture, DMA buffers",
                            "Arduino: I2S library, simple recording sketch",
                            "ESP-IDF: I2S driver (new API), ring buffers",
                            "Circular buffer design for real-time audio",
                            "Storing audio to SD card (WAV file format)",
                            "Streaming audio over BLE/WiFi",
                        ],
                    },
                    {
                        "title": "Chapter 8: Audio Capture on nRF54L15 (XIAO)",
                        "sections": [
                            "nRF PDM peripheral",
                            "Zephyr: nrfx PDM driver integration",
                            "EasyDMA and double buffering",
                            "Low-power audio capture strategies",
                            "BLE audio streaming (LE Audio concepts)",
                        ],
                    },
                    {
                        "title": "Chapter 9: Real-Time Audio Processing on MCU",
                        "sections": [
                            "FFT on ESP32-S3 (CMSIS-DSP vs ESP-DSP)",
                            "Real-time spectrogram generation",
                            "MFCC computation on MCU",
                            "Digital filter implementation (CMSIS-DSP biquad)",
                            "Audio feature extraction pipeline",
                            "Memory and CPU budget for audio processing",
                            "Lab: Build a real-time audio spectrum analyzer",
                        ],
                    },
                ],
            },
            {
                "part": "Part IV: Projects & Preparation for ML",
                "chapters": [
                    {
                        "title": "Chapter 10: Audio Projects (Pre-ML)",
                        "sections": [
                            "Project: Sound level meter with dB display",
                            "Project: Audio recorder with playback",
                            "Project: Tone/frequency detector (DTMF decoder)",
                            "Project: Simple clap detector using threshold + timing",
                            "Project: Audio streaming over WiFi (web interface)",
                            "Project: Guitar tuner using FFT",
                            "What's next: Audio features as ML input",
                        ],
                    },
                ],
            },
        ],
    },
    "tinyvue": {
        "name": "TinyVue",
        "domain": "Vision / Camera",
        "tagline": "From Photons to Perception",
        "book_title": "TinyVue: Embedded Vision — From Photons to Pixel Intelligence",
        "color": "#00b894",
        "icon": "tinyvue",
        "description": (
            "Embedded vision fundamentals: physics of light, color science, "
            "image processing, camera sensors, and real-time image processing on "
            "microcontrollers."
        ),
        "hardware": {
            "boards": ["XIAO ESP32-S3 Sense"],
            "summary": "XIAO ESP32-S3 Sense (all-in-one: camera + mic + SD)",
            "bom": [
                {"component": "XIAO ESP32-S3 Sense", "description": "MCU with onboard OV2640 camera and PDM mic", "qty": 1, "interface": "-"},
            ],
            "notes": [
                "XIAO ESP32-S3 Sense has the OV2640 camera module built-in (no external wiring)",
                "OV2640: 2MP, supports JPEG/RGB565/YUV422, max 1600x1200",
                "Board also includes onboard PDM microphone and SD card slot",
                "8MB PSRAM available for frame buffers",
            ],
        },
        "outline": [
            {
                "part": "Part I: Theory of Light & Vision",
                "chapters": [
                    {
                        "title": "Chapter 1: Physics of Light",
                        "sections": [
                            "Electromagnetic spectrum and visible light",
                            "Wave-particle duality (photons)",
                            "Wavelength, frequency, and energy",
                            "Reflection, refraction, and Snell's law",
                            "Lenses: convex, concave, focal length, aperture",
                            "Thin lens equation and magnification",
                            "Depth of field and f-number",
                            "Diffraction limit and resolution",
                        ],
                    },
                    {
                        "title": "Chapter 2: Color Science",
                        "sections": [
                            "How humans perceive color (cones, rods)",
                            "Additive color model (RGB)",
                            "Color spaces: RGB, HSV, YUV/YCbCr, Grayscale",
                            "Color temperature and white balance",
                            "Gamma correction",
                            "Why YUV matters for embedded (chroma subsampling)",
                            "Color depth: 8-bit, 16-bit (RGB565), 24-bit",
                        ],
                    },
                    {
                        "title": "Chapter 3: Digital Image Fundamentals",
                        "sections": [
                            "Pixels, resolution, and aspect ratio",
                            "Image as a matrix (grayscale and multi-channel)",
                            "Image file formats: BMP, JPEG, PNG",
                            "JPEG compression: DCT, quantization, Huffman",
                            "Image histogram and contrast",
                            "Coordinate systems and pixel addressing",
                            "Memory requirements: resolution x color depth calculations",
                            "Frame rate, bandwidth, and throughput considerations",
                        ],
                    },
                    {
                        "title": "Chapter 4: Image Processing Fundamentals",
                        "sections": [
                            "Point operations: brightness, contrast, thresholding",
                            "Convolution and kernels",
                            "Spatial filters: blur, sharpen, edge detection",
                            "Sobel, Prewitt, and Canny edge detectors",
                            "Morphological operations: erosion, dilation, opening, closing",
                            "Image resizing and interpolation (nearest, bilinear)",
                            "Histogram equalization",
                            "Connected component analysis",
                            "Practical: Which operations are feasible on MCUs?",
                        ],
                    },
                    {
                        "title": "Chapter 5: Feature Detection (Classical)",
                        "sections": [
                            "What are features? Corners, edges, blobs",
                            "Harris corner detection",
                            "FAST feature detector (designed for real-time)",
                            "BRIEF and ORB descriptors",
                            "Template matching",
                            "Hough transform (line and circle detection)",
                            "Optical flow basics (Lucas-Kanade)",
                            "Background subtraction",
                            "Why classical CV still matters for TinyML",
                        ],
                    },
                ],
            },
            {
                "part": "Part II: Camera Hardware & Working Principles",
                "chapters": [
                    {
                        "title": "Chapter 6: Image Sensor Technologies",
                        "sections": [
                            "CCD vs CMOS sensors",
                            "Bayer filter pattern and demosaicing",
                            "Rolling shutter vs global shutter",
                            "Sensor specifications: resolution, pixel size, sensitivity, dynamic range",
                            "OV2640 sensor deep dive (used in XIAO ESP32-S3 Sense)",
                            "OV5640 and other common sensors",
                            "Infrared sensors and thermal cameras (AMG8833, MLX90640)",
                            "Time-of-Flight (ToF) sensors",
                        ],
                    },
                    {
                        "title": "Chapter 7: Camera Interfaces & Data Flow",
                        "sections": [
                            "DVP (Digital Video Port) / parallel interface",
                            "MIPI CSI-2 interface",
                            "SPI cameras (e.g., Arducam SPI)",
                            "USB cameras (UVC)",
                            "SCCB/I2C for camera register configuration",
                            "DMA and frame buffer management",
                            "Image output formats: RGB565, YUV422, JPEG",
                            "Camera control: exposure, gain, white balance registers",
                        ],
                    },
                ],
            },
            {
                "part": "Part III: Firmware Implementation",
                "chapters": [
                    {
                        "title": "Chapter 8: Camera on ESP32-S3 (XIAO Sense)",
                        "sections": [
                            "OV2640 on XIAO ESP32-S3 Sense: pin mapping and schematic",
                            "ESP-IDF: esp_camera driver, frame buffer management",
                            "Arduino: ESP32 Camera library, basic capture",
                            "Zephyr: Video subsystem, camera driver (if available)",
                            "Resolution and format selection trade-offs",
                            "JPEG capture and storage to SD card",
                            "Frame rate optimization techniques",
                            "Memory management: PSRAM for frame buffers",
                        ],
                    },
                    {
                        "title": "Chapter 9: Image Processing on MCU",
                        "sections": [
                            "Grayscale conversion on MCU",
                            "Image downscaling for ML input",
                            "Real-time edge detection implementation",
                            "Histogram computation",
                            "Simple motion detection (frame differencing)",
                            "Color tracking (HSV thresholding)",
                            "ROI (Region of Interest) extraction",
                            "CPU and memory profiling for image operations",
                        ],
                    },
                    {
                        "title": "Chapter 10: Camera Streaming & Display",
                        "sections": [
                            "HTTP MJPEG streaming (web server)",
                            "WebSocket-based streaming",
                            "LVGL display integration (SPI LCD)",
                            "BLE image transfer (chunked)",
                        ],
                    },
                ],
            },
            {
                "part": "Part IV: Projects & Preparation for ML",
                "chapters": [
                    {
                        "title": "Chapter 11: Vision Projects (Pre-ML)",
                        "sections": [
                            "Project: Time-lapse camera with SD card storage",
                            "Project: Motion-triggered camera (frame differencing)",
                            "Project: Color-based object tracker",
                            "Project: QR/Barcode reader (using Quirc library)",
                            "Project: Web-based camera dashboard with controls",
                            "Project: Simple line-following robot (threshold-based)",
                            "What's next: Image features as ML input",
                        ],
                    },
                ],
            },
        ],
    },
    "tinyvibe": {
        "name": "TinyVibe",
        "domain": "Motion / IMU",
        "tagline": "From Movement to Meaning",
        "book_title": "TinyVibe: Embedded Motion Sensing — From Inertia to Intelligence",
        "color": "#e17055",
        "icon": "tinyvibe",
        "description": (
            "Embedded motion sensing fundamentals: physics of motion, magnetism, "
            "sensor fusion, accelerometers, gyroscopes, magnetometers, and IMU "
            "integration on microcontrollers."
        ),
        "hardware": {
            "boards": ["XIAO ESP32-S3", "XIAO nRF54L15"],
            "summary": "XIAO ESP32-S3 / nRF54L15 + ICM-20948 + W25Q128",
            "bom": [
                {"component": "XIAO ESP32-S3", "description": "Main MCU board (WiFi/BLE, 8MB PSRAM)", "qty": 1, "interface": "-"},
                {"component": "XIAO nRF54L15", "description": "Alternate MCU board (BLE, ultra-low power)", "qty": 1, "interface": "-"},
                {"component": "ICM-20948", "description": "9-DoF IMU (accel + gyro + mag)", "qty": 1, "interface": "I2C / SPI"},
                {"component": "W25Q128", "description": "128Mbit (16MB) external SPI NOR flash", "qty": 1, "interface": "SPI"},
            ],
            "notes": [
                "ICM-20948 is a 9-DoF IMU from TDK InvenSense with built-in DMP",
                "Accelerometer: +/-2g, 4g, 8g, 16g",
                "Gyroscope: +/-250, 500, 1000, 2000 dps",
                "Magnetometer: AK09916 (built-in), +/-4900 uT",
                "W25Q128 external flash for data logging, calibration storage, and dataset recording",
            ],
        },
        "outline": [
            {
                "part": "Part I: Theory of Motion & Inertial Sensing",
                "chapters": [
                    {
                        "title": "Chapter 1: Physics of Motion",
                        "sections": [
                            "Newton's laws of motion",
                            "Linear motion: displacement, velocity, acceleration",
                            "Rotational motion: angular displacement, velocity, acceleration",
                            "Frames of reference and coordinate systems",
                            "Gravity and gravitational acceleration",
                            "Centripetal and Coriolis forces",
                            "Degrees of freedom (6-DoF, 9-DoF)",
                            "Rigid body dynamics basics",
                        ],
                    },
                    {
                        "title": "Chapter 2: Earth's Magnetic Field & Magnetism",
                        "sections": [
                            "Earth's magnetic field: declination, inclination, intensity",
                            "Magnetic field units (Tesla, Gauss)",
                            "Hard iron vs soft iron distortion",
                            "Magnetic interference in embedded systems",
                            "True north vs magnetic north",
                            "World Magnetic Model (WMM)",
                        ],
                    },
                    {
                        "title": "Chapter 3: Sensor Mathematics",
                        "sections": [
                            "Vectors and vector operations",
                            "Rotation representations: Euler angles, rotation matrices",
                            "Quaternions — intuition and math",
                            "Gimbal lock and why quaternions matter",
                            "Coordinate frame transformations",
                            "Sensor noise: white noise, bias, drift, random walk",
                            "Allan variance for noise characterization",
                            "Statistical basics: mean, variance, standard deviation for sensor data",
                        ],
                    },
                    {
                        "title": "Chapter 4: Sensor Fusion Theory",
                        "sections": [
                            "Why single sensors are not enough",
                            "Complementary filter — intuition and implementation",
                            "Kalman filter — intuition (state, prediction, update)",
                            "Extended Kalman Filter (EKF) for nonlinear systems",
                            "Madgwick filter (AHRS) — computationally efficient",
                            "Mahony filter",
                            "Comparison: complementary vs Kalman vs Madgwick",
                            "Choosing the right filter for MCU constraints",
                        ],
                    },
                    {
                        "title": "Chapter 5: Motion Signal Processing",
                        "sections": [
                            "Low-pass, high-pass filtering for IMU data",
                            "Moving average and exponential smoothing",
                            "Gravity removal from accelerometer",
                            "Integration: acceleration to velocity to position (and its problems)",
                            "Gyroscope drift compensation",
                            "Peak detection algorithms",
                            "Zero-crossing detection",
                            "Activity segmentation (windowing)",
                            "Feature extraction: RMS, energy, zero-crossings, dominant frequency",
                        ],
                    },
                ],
            },
            {
                "part": "Part II: Sensor Hardware & Working Principles",
                "chapters": [
                    {
                        "title": "Chapter 6: Accelerometers",
                        "sections": [
                            "MEMS accelerometer working principle (capacitive, proof mass)",
                            "Specifications: range (g), sensitivity, bandwidth, noise density",
                            "Digital output: I2C/SPI registers",
                            "Built-in features: tap detection, free-fall, orientation",
                            "Common accelerometers: LIS2DH12, ADXL345, MC3419",
                            "High-g vs low-g accelerometers",
                            "Accelerometer as tilt sensor (using gravity vector)",
                        ],
                    },
                    {
                        "title": "Chapter 7: Gyroscopes",
                        "sections": [
                            "MEMS gyroscope working principle (Coriolis effect, vibrating mass)",
                            "Specifications: range (dps), sensitivity, bias stability, noise",
                            "Gyroscope drift and its causes",
                            "Angular rate vs angular position",
                            "Common gyroscopes and IMU combos",
                        ],
                    },
                    {
                        "title": "Chapter 8: Magnetometers",
                        "sections": [
                            "Hall-effect magnetometers",
                            "Magnetoresistive sensors (AMR, GMR, TMR)",
                            "Fluxgate magnetometers",
                            "Specifications: range, sensitivity, resolution, noise",
                            "Magnetic compass implementation",
                            "Tilt-compensated compass (combining accel + mag)",
                            "Magnetometer calibration: hard iron and soft iron compensation",
                            "Common magnetometers: LIS2MDL, MMC5603, QMC5883L",
                        ],
                    },
                    {
                        "title": "Chapter 9: IMU (Inertial Measurement Unit) Modules",
                        "sections": [
                            "What makes an IMU? (accel + gyro, optionally mag)",
                            "6-DoF IMUs: LSM6DSO, ICM-42688-P, BMI270",
                            "9-DoF IMUs: ICM-20948, BNO055 (with built-in fusion)",
                            "IMU on XIAO boards (built-in and external)",
                            "I2C vs SPI for IMU communication",
                            "FIFO buffers and data-ready interrupts",
                            "IMU placement and mounting considerations",
                            "Calibration procedures: bias, scale factor, cross-axis",
                        ],
                    },
                ],
            },
            {
                "part": "Part III: Firmware Implementation",
                "chapters": [
                    {
                        "title": "Chapter 10: IMU on ESP32-S3 (XIAO)",
                        "sections": [
                            "Connecting external IMU (ICM-20948) via I2C/SPI",
                            "Zephyr: Sensor subsystem, sensor_channel API, triggers",
                            "Arduino: Wire library, register-level and library-based access",
                            "ESP-IDF: I2C master driver, raw register access",
                            "Data rate configuration and FIFO usage",
                            "Interrupt-driven vs polled data acquisition",
                        ],
                    },
                    {
                        "title": "Chapter 11: IMU on nRF54L15 (XIAO)",
                        "sections": [
                            "I2C/SPI on nRF54L15",
                            "Zephyr: Device tree bindings for IMU sensors",
                            "Low-power motion sensing (wake-on-motion)",
                            "BLE motion data streaming",
                        ],
                    },
                    {
                        "title": "Chapter 12: Sensor Fusion Implementation on MCU",
                        "sections": [
                            "Complementary filter in C (step-by-step)",
                            "Madgwick filter implementation",
                            "Calibration routine implementation",
                            "Real-time orientation visualization (web dashboard)",
                            "Heading/compass implementation with tilt compensation",
                            "Step counter using accelerometer",
                            "Performance comparison: CPU cycles per fusion update",
                        ],
                    },
                ],
            },
            {
                "part": "Part IV: Projects & Preparation for ML",
                "chapters": [
                    {
                        "title": "Chapter 13: Motion Projects (Pre-ML)",
                        "sections": [
                            "Project: Digital spirit level with display",
                            "Project: Pedometer/step counter",
                            "Project: Compass with tilt compensation",
                            "Project: Gesture logger (record & visualize on web dashboard)",
                            "Project: Fall detection using threshold-based algorithm",
                            "Project: Dead reckoning position tracker (illustrating drift problem)",
                            "Project: Motion-triggered wake-up system (ultra-low power)",
                            "What's next: Motion features as ML input",
                        ],
                    },
                ],
            },
        ],
    },
}
