from modules.reader import read_feedback_today

if __name__ == "__main__":
    print("System started...")

    feedback = read_feedback_today()

    print("Feedback read from file:")
    for item in feedback:
        print(item)
