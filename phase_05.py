# Phase 05: Sentiment Classifier
from textblob import TextBlob

def classify_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.5:
        return "Positive"
    elif polarity < -0.5:
        return "Negative"
    return "Neutral"