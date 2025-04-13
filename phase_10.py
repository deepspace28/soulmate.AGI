# Phase 10: Emotion Reinforcement Learner
import random

def adapt_response(text):
    feedback = random.choice(["good", "bad"])
    if feedback == "good":
        return f"{text} (Learned Good Response)"
    else:
        return f"{text} (Adjusting...)"