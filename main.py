from modules.reader import read_feedback_today, read_chat_logs

if __name__ == "__main__":
    print("System started...\n")

    print("Reading feedback_today.txt")
    today_feedback = read_feedback_today()
    for item in today_feedback:
        print(item)

    print("\nReading chat_logs.txt")
    chat_feedback = read_chat_logs()
    for item in chat_feedback:
        print(item)
