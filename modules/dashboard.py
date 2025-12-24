from collections import Counter
def show_dashboard(feedback_list):
    ##Displays a simple console dashboard.
    sentiment_counter = Counter()
    category_counter = Counter()
    alert_count = 0

    for feedback in feedback_list:
        sentiment_counter[feedback["sentiment_type"]] += 1
        category_counter[feedback["category"]] += 1

        if feedback["sentiment_type"] == "Negative":
            alert_count += 1

    print("\n" )
    print("        REAL-TIME FEEDBACK DASHBOARD")
    print(" ")

    print("\nSentiment Overview:")
    print(f"  Positive : {sentiment_counter.get('Positive', 0)}")
    print(f"  Neutral  : {sentiment_counter.get('Neutral', 0)}")
    print(f"  Negative : {sentiment_counter.get('Negative', 0)}")

    print("\nComplaint Category Distribution:")
    for category, count in category_counter.items():
        print(f"  {category} : {count}")

    print(f"\nAlerts Triggered Today: {alert_count}")
    print(" ")
