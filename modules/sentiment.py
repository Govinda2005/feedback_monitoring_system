POSITIVE_KEYWORDS = {
    "good", "great", "excellent", "fast", "happy",
    "satisfied", "awesome", "thanks", "thank you"
}

NEGATIVE_KEYWORDS = {
    "bad", "poor", "delay", "late", "crash",
    "crashing", "issue", "problem", "worst",
    "billing", "charged", "slow"
}

def analyze_sentiment(message):
    """
    Returns:
        sentiment_score: +1 / 0 / -1
        sentiment_type: Positive / Neutral / Negative
    """

    message_lower = message.lower()

    positive_hits = 0
    negative_hits = 0

    for word in POSITIVE_KEYWORDS:
        if word in message_lower:
            positive_hits += 1

    for word in NEGATIVE_KEYWORDS:
        if word in message_lower:
            negative_hits += 1

    if positive_hits > negative_hits:
        return 1, "Positive"

    if negative_hits > positive_hits:
        return -1, "Negative"

    return 0, "Neutral"
