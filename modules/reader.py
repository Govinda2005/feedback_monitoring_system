import os

def read_feedback_today():
    feedback_list = []

    file_path = os.path.join("data", "feedback_today.txt")

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split(",")
            if len(parts) < 3:
                continue

            feedback = {
                "timestamp": parts[0].strip(),
                "customer_id": parts[1].strip(),
                "message": ",".join(parts[2:]).strip()
            }

            feedback_list.append(feedback)

    return feedback_list

def read_chat_logs():
    chat_feedback = []

    file_path = os.path.join("data", "chat_logs.txt")

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split("|")
            if len(parts) != 3:
                continue

            feedback = {
                "timestamp": parts[0].strip(),
                "customer_id": parts[1].strip(),
                "message": parts[2].strip()
            }

            chat_feedback.append(feedback)

    return chat_feedback
