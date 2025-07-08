# Object Detection Web Application using YOLO

This project is a web application for real-time object detection using the YOLO (You Only Look Once) model. The application is built with Streamlit and allows users to detect objects through their camera input.

## Project Structure

```
web-deteksi-objek
├── src
│   ├── app.py            # Main entry point for the Streamlit application
│   ├── model
│   │   └── my_model.pt   # Trained YOLO model weights
│   └── utils
│       └── detection.py   # Utility functions for object detection
├── requirements.txt       # List of dependencies
└── README.md              # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AchmadMuafiTaufiqurrochman/UAS-Visi-Komputer.git
   cd UAS-Visi-Komputer
   ```

2. **Install the required dependencies:**
   Make sure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   Start the Streamlit application by executing:
   ```bash
   streamlit run src/app.py
   ```

## Usage Guidelines

- Once the application is running, it will open in your default web browser.
- Allow access to your camera when prompted.
- The application will display the video feed from your camera with detected objects highlighted in real-time.

## Additional Information

- Ensure that the `my_model.pt` file is located in the `src/model` directory.
- You can modify the detection parameters in `src/utils/detection.py` to adjust the model's performance based on your requirements.

## License

This project is licensed under the MIT License.
