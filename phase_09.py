# Phase 09: Real-time Tone Modulator
def tone_modifier(text, mood="cheerful"):
    if mood == "cheerful":
        return f"😊 {text} Yay!"
    elif mood == "serious":
        return f"⚠️ {text}."
    else:
        return text