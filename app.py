import os
from flask import Flask, request, jsonify
from pyrobale.client import Client

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BALE_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
bot = Client(BOT_TOKEN)

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    chat_id = data.get('chat_id')
    text = data.get('text')
    
    if not chat_id or not text:
        return jsonify({"status": "error", "message": "chat_id and text are required"}), 400
    
    try:
        bot.send_message(chat_id, text)
        return jsonify({"status": "success", "message": "Message sent"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/')
def home():
    return "Bale Webhook Service is Running!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)