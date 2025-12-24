from modules.reader import (
    read_feedback_today,
    read_chat_logs,
    read_email_feedback
)
from modules.sentiment import analyze_sentiment

if __name__ == "__main__":
    print("System started...\n")

    all_feedback = []
    all_feedback.extend(read_feedback_today())
    all_feedback.extend(read_chat_logs())
    all_feedback.extend(read_email_feedback())

    print("Sentiment Analysis Results:\n")

    for feedback in all_feedback:
        score, sentiment = analyze_sentiment(feedback["message"])

        feedback["sentiment_score"] = score
        feedback["sentiment_type"] = sentiment

        print(
            f"{feedback['customer_id']} | "
            f"{sentiment} ({score}) | "
            f"{feedback['message']}"
        )
