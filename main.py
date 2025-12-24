from modules.reader import (
    read_feedback_today,
    read_chat_logs,
    read_email_feedback
)

if __name__ == "__main__":
    print("System started...\n")

    all_feedback = []

    all_feedback.extend(read_feedback_today())
    all_feedback.extend(read_chat_logs())
    all_feedback.extend(read_email_feedback())

    print(f"Total feedback records: {len(all_feedback)}\n")

    for feedback in all_feedback:
        print(feedback)
