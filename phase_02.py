# Phase 02: Emotional Analysis
from deepface import DeepFace
import cv2

def detect_emotion():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']
        print(f"Detected Emotion: {emotion}")
    cap.release()

if __name__ == "__main__":
    detect_emotion()