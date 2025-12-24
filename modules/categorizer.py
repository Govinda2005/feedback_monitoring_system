def categorize_feedback(message):
    message_lower = message.lower()

    if any(word in message_lower for word in ["service", "support", "agent", "help"]):
        return "Service Issue"

    if any(word in message_lower for word in ["delivery", "late", "delay", "arrived"]):
        return "Delivery Delay"

    if any(word in message_lower for word in ["bill", "billing", "charged", "payment"]):
        return "Billing Problem"

    if any(word in message_lower for word in ["app", "website", "crash", "crashing", "bug"]):
        return "App/Website Issue"

    if any(word in message_lower for word in ["good", "great", "excellent", "thanks", "happy"]):
        return "General Appreciation"

    return "General"
