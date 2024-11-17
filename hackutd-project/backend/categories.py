import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from collections import Counter

# File path to the CSV
file_path = '/Users/rchittineni/Repos/Project/hackutd-project/backend/test bank statement data.csv'

# 1. Load CSV Data
def load_transactions(file_path):
    df = pd.read_csv(file_path)
    transactions = df.to_dict(orient="records")  # Convert DataFrame to a list of dictionaries
    return transactions

# 2. Calculate Category Spending
def calculate_category_spending(transactions):
    category_totals = {}
    for transaction in transactions:
        category = transaction['Category']
        amount = float(transaction['Amount'])
        category_totals[category] = category_totals.get(category, 0) + amount
    return category_totals

# 3. Monthly Trends
def monthly_trends(transactions):
    trends = {}
    for transaction in transactions:
        post_date = transaction['Post Date']
        month = post_date.split('/')[0]  # Extract month from the date
        category = transaction['Category']
        amount = float(transaction['Amount'])
        trends.setdefault(month, {}).setdefault(category, 0)
        trends[month][category] += amount
    return trends

# 4. Top N Largest Transactions
def top_largest_transactions(transactions, top_n=3):
    sorted_transactions = sorted(transactions, key=lambda x: abs(float(x['Amount'])), reverse=True)
    return sorted_transactions[:top_n]



# 6. Income vs Expenses
def income_vs_expenses(transactions, starting_balance):
    income = sum(float(t['Amount']) for t in transactions if float(t['Amount']) > 0)
    expenses = sum(float(t['Amount']) for t in transactions if float(t['Amount']) < 0)
    net_balance = starting_balance + income + expenses
    return {"Income": income, "Expenses": expenses, "Net Balance": net_balance}

# 7. Transaction Frequency
def transaction_frequency(transactions):
    frequency = Counter(t['Category'] for t in transactions)
    return dict(frequency)

# 8. Predicted Credit Score
def predicted_credit_score(transactions, starting_score=720):
    on_time_payments = sum(1 for t in transactions if t['Category'] == 'Payment' and float(t['Amount']) > 0)
    total_expenses = sum(abs(float(t['Amount'])) for t in transactions if float(t['Amount']) < 0)
    
    # Simplified formula
    credit_score = starting_score + (on_time_payments * 5) - (total_expenses / 100)
    return round(min(max(credit_score, 300), 850))  # Clamp between 300 and 850

# Main Function
if __name__ == "__main__":
    # Load transactions from the CSV
    transactions = load_transactions(file_path)
    
    # Starting balance
    starting_balance = 1800
    
    # Perform analysis
    print("Category Spending:", calculate_category_spending(transactions))
    print("Monthly Trends:", monthly_trends(transactions))
    print("Top 3 Largest Transactions:", top_largest_transactions(transactions))
    print("Income vs Expenses:", income_vs_expenses(transactions, starting_balance))
    print("Transaction Frequency:", transaction_frequency(transactions))
    print("Predicted Credit Score:", predicted_credit_score(transactions))
