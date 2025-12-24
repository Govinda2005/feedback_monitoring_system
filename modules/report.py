import os
from collections import Counter


def generate_daily_report(feedback_list):
    ## Generates a daily feedback summary report.
    output_dir = "output"
    report_file = os.path.join(output_dir, "daily_feedback_report.txt")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    sentiment_counter = Counter()
    category_counter = Counter()
    customer_complaints = Counter()
    negative_samples = []

    for feedback in feedback_list:
        sentiment_counter[feedback["sentiment_type"]] += 1
        category_counter[feedback["category"]] += 1

        if feedback["sentiment_type"] == "Negative":
            customer_complaints[feedback["customer_id"]] += 1
            if len(negative_samples) < 5:
                negative_samples.append(feedback["message"])

    most_common_category = "None"
    if category_counter:
        most_common_category = category_counter.most_common(1)[0][0]

    suggestions = []

    if category_counter.get("Delivery Delay", 0) > 0:
        suggestions.append("Review delivery timelines and logistics performance.")

    if category_counter.get("Billing Problem", 0) > 0:
        suggestions.append("Audit billing system for duplicate or incorrect charges.")

    if category_counter.get("App/Website Issue", 0) > 0:
        suggestions.append("Investigate application stability and bug reports.")

    if not suggestions:
        suggestions.append("Maintain current service quality and continue monitoring.")

    with open(report_file, "w", encoding="utf-8") as file:
        file.write("DAILY CUSTOMER FEEDBACK REPORT\n")
        file.write("----------*****----------" + "\n\n")

        file.write("Sentiment Summary:\n")
        for sentiment, count in sentiment_counter.items():
            file.write(f"- {sentiment}: {count}\n")

        file.write("\nMost Common Complaint Category:\n")
        file.write(f"- {most_common_category}\n")

        file.write("\nTop Customer Complaints:\n")
        if customer_complaints:
            for customer, count in customer_complaints.most_common(3):
                file.write(f"- {customer}: {count} complaints\n")
        else:
            file.write("- No repeated complaints\n")

        file.write("\nSample Negative Feedback:\n")
        if negative_samples:
            for msg in negative_samples:
                file.write(f"- {msg}\n")
        else:
            file.write("- No negative feedback today\n")

        file.write("\nSystem Suggestions:\n")
        for suggestion in suggestions:
            file.write(f"- {suggestion}\n")

    return report_file
