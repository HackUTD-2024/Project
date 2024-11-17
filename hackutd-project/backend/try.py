import os
import requests
import pandas as pd
from PyPDF2 import PdfReader
from dotenv import load_dotenv  # Import dotenv

# Load environment variables from the .env file
load_dotenv()

# Function to process CSV data
def process_csv(input_file):
    data = pd.read_csv(input_file.name)  # Assuming the file has headers
    data['Amount'] = pd.to_numeric(data['Amount'], errors='coerce')  # Convert Amount to numeric
    spending_by_category = data.groupby('Category').agg(
        total_spending=('Amount', 'sum'),
        avg_spending=('Amount', 'mean')
    ).reset_index()
    return spending_by_category

# Function to process PDF data
def process_pdf(input_file):
    reader = PdfReader(input_file.name)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    
    # Assuming the PDF contains category, amount, and type information in a specific format
    # Example text parsing should be added here, this is just an outline
    # Convert text data to a DataFrame or directly into structured data to pass to the model
    return text

# Function to create a prompt from financial data (CSV or processed PDF)
def create_prompt(spending_data):
    prompt = "Analyze the following personal financial data and provide insights and suggestions on user's spending:\n"
    for _, row in spending_data.iterrows():
        prompt += f"Category: {row['Category']}, Total Spending: {row['total_spending']}, Average Spending: {row['avg_spending']}\n"
    
    prompt += "Provide a suggestion for reducing or optimizing spending in each category. If their spending is good, provide positive encouragement to maintain. "
    return prompt

# Function to send the prompt to SambaNova API and get a response
def generate_dynamic_response(prompt):
    try:
        # Replace with your SambaNova API endpoint and key
        sambanova_api_url = 'https://api.sambanova.ai/v1/chat/completions'  # Example endpoint
        api_key = os.getenv("SAMBANOVA_API_KEY")  # Get the API key from the .env file
        headers = {'Authorization': f'Bearer {api_key}'}
        data = {
            'model': 'Meta-Llama-3.1-405B-Instruct',  # Specify the model you want to use
            'messages': [
                {"role": "system", "content": "You are a helpful financial assistant."},
                {"role": "user", "content": prompt}
            ],
            'temperature': 0.1,
            'top_p': 0.1
        }
        response = requests.post(sambanova_api_url, json=data, headers=headers)

        if response.status_code == 200:
            # Assuming the response contains a 'choices' key with 'message' field
            return response.json()['choices'][0]['message']['content']
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error: {e}"

# Function to analyze the uploaded financial data
def analyze_financial_data(input_file):
    # Check file type (CSV or PDF)
    if input_file.name.endswith('.csv'):
        spending_data = process_csv(input_file)
    elif input_file.name.endswith('.pdf'):
        spending_data = process_pdf(input_file)
    else:
        return "Please upload a CSV or PDF file."

    # Create the prompt for the model
    prompt = create_prompt(spending_data)

    # Get the dynamic response from the model
    analysis = generate_dynamic_response(prompt)
    return analysis

# For testing purposes, let's simulate uploading a file and getting a response
if __name__ == "__main__":
    # Replace with a real file upload in your web app
    file_path = "D:/VS Code Projects/Project/hackutd-project/backend/test bank statement data.csv"  # Path to your CSV or PDF file
    with open(file_path, 'rb') as f:
        analysis_output = analyze_financial_data(f)
        print(analysis_output)











      