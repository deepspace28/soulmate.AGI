# Phase 06: Web API using Flask
from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
chatbot = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = chatbot(user_input, max_new_tokens=100)[0]['generated_text']
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)