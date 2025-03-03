# Enhanced chatbot logic
def get_bot_response(message):
    message = message.lower()

    # Greetings
    if any(word in message for word in ["hello", "hi", "hey"]):
        return "Hello! How can I assist you today?"

    # Farewells
    elif any(word in message for word in ["bye", "goodbye", "see you"]):
        return "Goodbye! Have a great day!"

    # Help
    elif "help" in message:
        return (
            "I can help you with the following:\n"
            "- View your grades\n"
            "- Check your fee balance\n"
            "- See your current phase\n"
            "- Make a payment\n"
            "What do you need?"
        )

    # Grades
    elif any(word in message for word in ["grades", "marks", "results"]):
        return "You can view your grades on the Grades page. Would you like me to take you there?"

    # Fee Balance
    elif any(word in message for word in ["fee", "balance", "outstanding", "payment"]):
        return "Your fee balance is available on the Fee Balance page. Would you like me to take you there?"

    # Current Phase
    elif any(word in message for word in ["phase", "current phase", "training phase"]):
        return "Your current phase is displayed on the Current Phase page. Would you like me to take you there?"

    # Payments
    elif any(word in message for word in ["pay", "payment", "make payment"]):
        return "You can make a payment through the Payment page. Would you like me to take you there?"

    # Unknown queries
    else:
        return (
            "I'm sorry, I didn't understand that. Here are some things I can help with:\n"
            "- View your grades\n"
            "- Check your fee balance\n"
            "- See your current phase\n"
            "- Make a payment\n"
            "What do you need?"
        )