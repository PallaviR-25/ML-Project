from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

# Simple response generator
def get_response(user_input):
    blob = TextBlob(user_input)
    sentiment = blob.sentiment.polarity
    user_input_lower = user_input.lower()

    if "sad" in user_input_lower or "depressed" in user_input_lower or "unhappy" in user_input_lower or sentiment < -0.3:
        return "I'm here for you. It's okay to feel sad sometimes. Would you like to try a breathing exercise or listen to calming music?"
    
    elif "happy" in user_input_lower or "joy" in user_input_lower or "excited" in user_input_lower or sentiment > 0.3:
        return "That's wonderful to hear! Keep smiling 😊 Life's little joys are worth celebrating!"
    
    elif "anxious" in user_input_lower or "stress" in user_input_lower or "worried" in user_input_lower or "panic" in user_input_lower:
        return "Stress and anxiety can be tough. Take a deep breath. Would you like a tip to help you feel more relaxed?"
    
    elif "angry" in user_input_lower or "mad" in user_input_lower or "frustrated" in user_input_lower:
        return "It's okay to feel angry. Sometimes talking it out helps. Would you like to try a calming exercise?"
    
    elif "tired" in user_input_lower or "exhausted" in user_input_lower or "burnt out" in user_input_lower:
        return "You sound tired. Rest is important. How about a short guided relaxation break?"
    
    elif "lonely" in user_input_lower or "alone" in user_input_lower:
        return "Feeling lonely is tough. I'm here for you. Want to talk more about what's going on?"

    else:
        return "I'm listening. Please tell me more about how you're feeling."


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    bot_response = get_response(user_input)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
