from modules.reader import (
    read_feedback_today,
    read_chat_logs,
    read_email_feedback
)
from modules.sentiment import analyze_sentiment
from modules.categorizer import categorize_feedback

if __name__ == "__main__":
    print("System started...\n")

    all_feedback = []
    all_feedback.extend(read_feedback_today())
    all_feedback.extend(read_chat_logs())
    all_feedback.extend(read_email_feedback())

    print("Sentiment & Categorization Results:\n")

    for feedback in all_feedback:
        score, sentiment = analyze_sentiment(feedback["message"])
        category = categorize_feedback(feedback["message"])

        feedback["sentiment_score"] = score
        feedback["sentiment_type"] = sentiment
        feedback["category"] = category

        print(
            f"{feedback['customer_id']} | "
            f"{sentiment} | "
            f"{category} | "
            f"{feedback['message']}"
        )
