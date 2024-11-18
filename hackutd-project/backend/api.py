from flask import Flask, request, jsonify
from flask_cors import CORS
from gradio_client import Client
import process_file
import json
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

        data = request.get_json() # user prompt
        message = data.get("message")

        if not message:
            return jsonify({"error": "Message is required"}), 400
        
        # classify prompt type
        prompt_type = classify_Prompt_Type(message)
        print(prompt_type)

        if prompt_type == 'GreetingAndFormalities':
            prompt_classification = 'The user may be asking about greeting or formalities. Provide polite and welcoming responses to address the user’s query, using friendly language and professional tone.'
        elif prompt_type == 'OpenAccount':
            prompt_classification = 'The user may be asking about opening an account. Provide clear itemized steps for the process, including any required documentation and timelines.'
        elif prompt_type == 'GeneralFinancialInfo':
            prompt_classification = 'The user may be asking about general financial information. Provide well-rounded, fundamental advice, using simple language to explain financial concepts.'
        elif prompt_type == 'GeneralInfoOnHowToDoSomethingNotRegardingUserData':
            prompt_classification = 'The user may be asking how to do something related to finance. Provide step-by-step instructions, using simple and easy-to-follow language.'
        elif prompt_type == 'ExplainMyData':
            prompt_classification = 'The user may want an explanation of their financial data. Refer specifically to the statistics and data below. Only answer from them. The transaction date is in MM-DD-YYYY format'
        elif prompt_type == 'GoalIncreaseSavings':
            prompt_classification = 'The user may be asking for ways to increase their savings. Provide practical strategies, tips, and methods for improving savings rates and managing expenses based on their data. Cite it too.'
        elif prompt_type == 'GoalDecreaseExpenditure':
            prompt_classification = 'The user may want to decrease their expenditures. Offer actionable tips to reduce costs, prioritize spending, and optimize budgets based on their data. Cite it too.'
        elif prompt_type == 'GoalRetirementPlans':
            prompt_classification = 'The user may be inquiring about retirement plans. Offer advice on retirement planning, including strategies for savings, investment, and long-term goals based on their data. Cite it too.'
        elif prompt_type == 'GoalLongTerm':
            prompt_classification = 'The user may be asking about long-term financial goals. Provide guidance on long-term planning, such as savings strategies, investments, and goal-setting based on their data. Cite it too.'
        elif prompt_type == 'AnalyzeDataAndMakeStatistics':
            prompt_classification = 'The user may want an analysis of their financial data. Provide statistical analysis of their data, pointing out patterns, trends, and key insights. Cite data'
        elif prompt_type == 'LookupSpecificInfoInMyData':
            prompt_classification = 'You are now a calculator. Exactly look over the data. All the data below. Formulate your answer based on that.The user may be asking to look up specific information in their financial data below. Provide precise, accurate responses, focused on retrieving specific data points. The transaction date is in MM-DD-YYYY format. '
        elif prompt_type == 'FindTrendsInData':
            prompt_classification = 'The user may want to identify trends in their financial data. Provide a thorough analysis of their financial data or statistics to uncover trends and patterns over time.'
        elif prompt_type == 'CalculateTax':
            prompt_classification = 'The user may be asking for tax-related information. Provide tax calculations, tax-saving strategies, and general tax advice based on the user’s financial data.'
        elif prompt_type == 'CalculateCreditScore':
            prompt_classification = 'The user may be asking to calculate their credit score. Explain the factors that affect the score and offer advice on how to improve or maintain a good credit score.'
        elif prompt_type == 'PredictNextMonth':
            prompt_classification = 'The user may be asking to predict their financial situation for the next month. Provide forecasts based on historical data and trends, keeping in mind relevant financial factors.'
        elif prompt_type == 'PredictLongTermOutlook':
            prompt_classification = 'The user may want predictions about their long-term financial outlook. Provide forecasts based on their financial data and relevant economic factors, with advice on planning for the future.'
        elif prompt_type == 'PredictNextMonthCreditScore':
            prompt_classification = 'The user may be asking for a prediction of their credit score next month. Provide a prediction based on current financial behavior and trends in their credit activity.'
        else:
            prompt_classification = 'The user’s query does not fall under a specific category. Provide a general response, asking for clarification if needed.'
        

        # prompt engineering
        context = 'You are a personal financial assistant. Be very accurate and knowledgeable about personal finance. DO NOT MAKE MISTAKES. If available, first refer to previous information disclosed or data available and cite it. The user Data below has transaction date in format MM-DD-YYYY. "01" corresponds to January, "02" to February, "03" to March, "04" to April, "05" to May, "06" to June, "07" to July, "08" to August, "09" to September, "10" to October, "11" to November, and "12" to December.'
        # prompt_classification = 'The user may be asking about ' + prompt_type # do an if statement
        instructions = 'Provide your response to the USER in on average 2 sentences such that an average adult can understand. Respond with good formatting (bullet points, new lines, etc). Generally be succinct and shorter answers, unless the user follows up and asks more in-depth. It is okay to say "i don\'t know or guide the user to a better source rather than making up information, but you should try your best to factually answer the user\'s query. BUT, do not add notes at the end that are intended for the instructions (the User should not know anything about the instructions provided and the format of the data provided)'
        statistics = process_file.process_file('C:/Users/abhir/Projects/HackUTD-Ripple/Project/hackutd-project/backend/test bank statement data.csv')
        if statistics is None:
            statistics = ""  # Or handle the error accordingly
        elif isinstance(statistics, dict):
            statistics = str(statistics)
        statistics = "Statistics: " + statistics
        data = process_file.get_data('C:/Users/abhir/Projects/HackUTD-Ripple/Project/hackutd-project/backend/test bank statement data.csv').to_string(index=False)
        # print(data)
        full_prompt = context + "\n" + prompt_classification + "\n" + instructions + '\n' + statistics + "\n" + data + "\n" + message
        print (full_prompt)
        # call the gradio chatbot
        result = gradio_client.predict(
            message=full_prompt,
            api_name="/chat"
        )

        return jsonify({"response": result}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Something went wrong!"}), 500

def classify_Prompt_Type(msg):
    instructions = 'Classify the below user prompt into one of the following categories. Return a 1-word response. Be accurate.'
    categories = 'Here are the categories: \n GreetingAndFormalities, OpenAccount, GeneralFinancialInfo, GeneralInfoOnHowToDoSomethingNotRegardingUserData, ExplainMyData, GoalIncreaseSavings, GoalDecreaseExpenditure, GoalRetirementPlans, GoalLongTerm, AnalyzeDataAndMakeStatistics, LookupSpecificInfoInMyData, FindTrendsInData, CalculateTax, CalculateCreditScore, PredictNextMonth, PredictLongTermOutlook, PredictNextMonthCreditScore, Other'
    fullPrompt = instructions + "\n" + categories + "\nHere is the prompt that you should classify:\n" + msg
    prompt_type = gradio_client.predict(
            message=fullPrompt,
            api_name="/chat"
        )
    return prompt_type

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
