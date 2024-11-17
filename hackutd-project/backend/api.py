from flask import Flask, request, jsonify
from flask_cors import CORS
from gradio_client import Client

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"]) 

gradio_client = Client("http://127.0.0.1:7860/")

@app.route('/api/ask', methods=['POST'])
def chat():
    try:

        data = request.get_json()
        message = data.get("message")

        if not message:
            return jsonify({"error": "Message is required"}), 400

        result = gradio_client.predict(
            message=message,
            api_name="/chat"
        )

        return jsonify({"response": result}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Something went wrong!"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
