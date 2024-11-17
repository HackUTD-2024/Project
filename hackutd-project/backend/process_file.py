# process_file.py
import pandas as pd


        

def process_file(input_file):
    # Read the input file
    try:
        # Load the data
        content = pd.read_csv(input_file)

        # Preprocess the data
        content['Transaction Date'] = pd.to_datetime(content['Transaction Date'])
        content['Post Date'] = pd.to_datetime(content['Post Date'])
        content['Amount'] = pd.to_numeric(content['Amount'], errors='coerce')

        # Group by category (sorted by highest total spending)
        category_stats = content[content['Amount'] < 0].groupby('Category').agg(
            total_spending=('Amount', 'sum'),
            avg_spending=('Amount', 'mean')
        ).sort_values(by="total_spending", ascending=True)

        # Display category frequency
        category_frequency = content[content['Amount'] < 0].groupby('Category')['Amount'].count().sort_values(ascending=False)

        # Time-based analysis (monthly)
        content['Month'] = content['Transaction Date'].dt.to_period('M')
        monthly_stats_spend = content[content['Amount'] < 0].groupby('Month').agg(
            total_spending=('Amount', 'sum'),
            avg_spending=('Amount', 'mean')
        )
        monthly_stats_recieve = content[content['Amount'] > 0].groupby('Month').agg(
            total_revenue=('Amount', 'sum'),
            avg_revenue=('Amount', 'mean')
        )
        total_revenue_sum = monthly_stats_recieve['total_revenue'].sum()
        total_spend_sum = monthly_stats_spend['total_spending'].sum()
        largest_3_spends = content[content['Amount'] < 0].nsmallest(3, 'Amount')

        # Extract week numbers from transaction dates
        content['Week'] = content['Transaction Date'].dt.to_period('W')

        # Calculate weekly total spending
        weekly_spending = content[content['Amount'] < 0].groupby('Week')['Amount'].sum().abs()

        # Define the threshold dynamically (e.g., 1.5 times average weekly spending)
        threshold = weekly_spending.mean() * 1.5

        # Identify weeks with high spending
        high_spending_weeks = weekly_spending[weekly_spending > threshold]

        # # Plot weekly spending
        # plt.figure(figsize=(12, 6))
        # plt.plot(weekly_spending.index.astype(str), weekly_spending, label='Weekly Spending', color='blue')
        # plt.scatter(high_spending_weeks.index.astype(str), high_spending_weeks, color='red', label='High Expenditure', zorder=5)
        # plt.axhline(threshold, color='green', linestyle='--', label=f'Threshold (${threshold:.2f})')
        # plt.xticks(rotation=45)
        # plt.title('Weekly Spending with High Expenditure Highlighted')
        # plt.ylabel('Spending')
        # plt.xlabel('Week')
        # plt.legend()
        # plt.tight_layout()
        # plt.show()

        # # Plot monthly spending trends
        # monthly_stats_spend['total_spending'].plot(kind='line', figsize=(10, 6))
        # plt.title('Monthly Total Spending')
        # plt.ylabel('Total Spending')
        # plt.xlabel('Month')
        # plt.show()

        # # Visualize spending distribution
        # plt.figure(figsize=(10, 6))
        # sns.histplot(content[content['Amount'] < 0]['Amount'], kde=True, color='red')
        # plt.title('Distribution of Spending')
        # plt.xlabel('Spending Amount')
        # plt.ylabel('Frequency')
        # plt.show()

        # Display results
        print("Category Statistics:")
        print(category_stats)
        print("Frequency of Transactions by Category:")
        print(category_frequency)
        print("Monthly Spending Stats:")
        print(monthly_stats_spend)
        print(monthly_stats_recieve)
        print(total_revenue_sum)
        print(total_spend_sum)
        print(largest_3_spends)
        print("High Spending Weeks:")
        print(high_spending_weeks)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    input_file = "D:/VS Code Projects/Project/hackutd-project/backend/test bank statement data.csv"
    process_file(input_file)