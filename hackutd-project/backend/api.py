from flask import Flask, request, jsonify
from flask_cors import CORS
from gradio_client import Client
from categories import (
    load_transactions,
    calculate_category_spending,
    monthly_trends,
    top_largest_transactions,
    income_vs_expenses,
    transaction_frequency,
    predicted_credit_score,
)

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"]) 

gradio_client = Client("http://127.0.0.1:7860/")

file_path = '/Users/rchittineni/Repos/Project/hackutd-project/backend/test bank statement data.csv'

@app.route('/api/analyze', methods=['POST'])
def analyze_data():
    try:
        # Load transactions
        transactions = load_transactions(file_path)
        starting_balance = 1800  # Example starting balance

        # Perform analyses using functions from categories.py
        category_spending = calculate_category_spending(transactions)
        monthly_trend = monthly_trends(transactions)
        largest_transactions = top_largest_transactions(transactions)
        income_expenses = income_vs_expenses(transactions, starting_balance)
        transaction_freq = transaction_frequency(transactions)
        credit_score = predicted_credit_score(transactions)

        # Return all results in a single JSON response
        return jsonify({
            "categorySpending": category_spending,
            "monthlyTrends": monthly_trend,
            "topLargestTransactions": largest_transactions,
            "incomeVsExpenses": income_expenses,
            "transactionFrequency": transaction_freq,
            "predictedCreditScore": credit_score
        }), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Something went wrong!"}), 500

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
