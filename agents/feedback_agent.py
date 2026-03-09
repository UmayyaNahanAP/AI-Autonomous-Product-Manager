import pandas as pd
from textblob import TextBlob

def analyze_feedback(file_path):

    df = pd.read_csv(file_path)

    sentiments = []

    for review in df["review"]:
        polarity = TextBlob(review).sentiment.polarity

        if polarity > 0:
            sentiments.append("Positive")
        elif polarity < 0:
            sentiments.append("Negative")
        else:
            sentiments.append("Neutral")

    df["sentiment"] = sentiments

    complaints = df[df["sentiment"] == "Negative"]["review"].tolist()

    return df, complaints