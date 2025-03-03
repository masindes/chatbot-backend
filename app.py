from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Simple rule-based chatbot logic
def get_bot_response(message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! How can I assist you today?"
    elif "how are you" in message:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "bye" in message:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Endpoint to handle chat messages
@app.route("/webhooks/rest/webhook", methods=["POST"])
def chat():
    data = request.json
    sender = data.get("sender", "user")
    message = data.get("message", "")

    if not message:
        return jsonify({"error": "Message is required"}), 400

    # Simulate a delay for bot response
    bot_response = get_bot_response(message)
    return jsonify([{"text": bot_response}])

# Start the server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)