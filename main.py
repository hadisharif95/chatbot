from flask import Flask, request, jsonify
from transformers import pipeline

# Load GPT-2 model
chatbot = pipeline("text-generation", model="gpt2")

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")  # دریافت پیام کاربر
    response = chatbot(user_input, max_length=100, num_return_sequences=1)
    return jsonify({"response": response[0]['generated_text']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
