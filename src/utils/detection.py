from ultralytics import YOLO

def load_model(model_path):
    return YOLO(model_path)

def detect_objects(model, frame):
    results = model(frame)
    detections = []
    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            detections.append((x1, y1, x2, y2, conf, cls))
    return detections