# Phase 07: Camera Face Logger
import cv2

def capture_face():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite("captured_face.jpg", frame)
        print("Face captured.")
    cap.release()