# Phase 12: Facial Sentiment Processing
from deepface import DeepFace

def process_face_image(image_path):
    result = DeepFace.analyze(img_path=image_path, actions=['emotion'])
    return result[0]['dominant_emotion']