import logging
import os
from collections import defaultdict


# make sure logs directory exists
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "negative_alerts.log")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)


logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(message)s"
)


customer_negative_count = defaultdict(int)


def process_negative_feedback(feedback):
    """
    Logs negative feedback.
    Marks repeat complaints from same customer as URGENT.
    """

    customer_id = feedback["customer_id"]
    message = feedback["message"]
    category = feedback["category"]

    customer_negative_count[customer_id] += 1

    urgency = "URGENT" if customer_negative_count[customer_id] > 1 else "NORMAL"

    log_message = (
        f"{urgency} | "
        f"Customer: {customer_id} | "
        f"Category: {category} | "
        f"Message: {message}"
    )

    logging.info(log_message)

    return urgency
