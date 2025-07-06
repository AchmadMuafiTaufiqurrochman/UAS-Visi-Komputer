import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
from utils.detection import load_model, detect_objects
import os
import cv2

# Load the YOLO model
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model', 'my_model.pt')
model = load_model(MODEL_PATH)

st.title("Object Detection with YOLO")

# Daftar label class
CLASS_LABELS = ["deodorant", "parfume", "rokok"]

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    detections = detect_objects(model, img)
    for detection in detections:
        x1, y1, x2, y2, conf, cls = detection
        if conf > 0.60:
            # Ambil nama class dari CLASS_LABELS
            class_name = CLASS_LABELS[cls] if cls < len(CLASS_LABELS) else str(cls)
            label = f"{class_name}, Confidence: {conf:.2f}"
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    return av.VideoFrame.from_ndarray(img, format="bgr24")

webrtc_streamer(key="example", video_frame_callback=video_frame_callback)