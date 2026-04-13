from ultralytics import YOLO
import cv2
model=YOLO("yolov8n.pt")
cap=v2.VideoCapture(0)
while True:
    ret, frame=cap.read()
    results=model(frame)
    annotated_frame=results[0].plot()
    cv2.imshow('object detection', annotated_frame)
    if cv2.waitkey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindow()
