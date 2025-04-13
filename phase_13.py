# Phase 13: Wellness Advice Generator
def generate_wellness_tip(emotion):
    tips = {
        "happy": "Keep smiling. Share your joy.",
        "sad": "Try talking to a friend.",
        "angry": "Take deep breaths, go for a walk."
    }
    return tips.get(emotion, "Take care.")