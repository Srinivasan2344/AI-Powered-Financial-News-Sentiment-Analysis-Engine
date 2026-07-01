from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="ProsusAI/finbert"
)

def analyze_sentiment(text: str):
    result = classifier(text)

    return {
        "text": text,
        "sentiment": result[0]["label"],
        "confidence": round(result[0]["score"], 4)
    }