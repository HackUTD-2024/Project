import React, { useState } from 'react';
import Chatbot from '../components/Chatbot';

const Home = () => {
  const [selectedCard, setSelectedCard] = useState(null);
  const [uploadedFile, setUploadedFile] = useState(null);

  // Hardcoded data for each card
  const analysisData = {
    balance: {
      '$322.11': 322.11
    },
    categorySpending: {
      'Entertainment': -156.2,
      'Groceries': -71.59,
      'Shopping': -311.08,
      'Health & Wellness': -64.74,
      'Food & Drink': -226.79,
      'Fees & Adjustments': -54.86,
      'Travel': -360.48,
      'Gas': -22.85,
      'Education': -74.45,
      'Personal': -30.74,
      'Professional Services': -94.11
    },
    monthlyTrends: {
      'December': {
        'Entertainment': -116.71,
        'Groceries': -26.93,
        'Shopping': -31.89,
        'Health & Wellness': -38.75,
        'Food & Drink': -69.55,
        'Fees & Adjustments': -9.9,
        'Travel': -17.09
      },
      'November': {
        'Food & Drink': -43.8,
        'Travel': -87.1,
        'Shopping': -5.1,
        'Groceries': -9.8,
        'Gas': -22.85,
        'Fees & Adjustments': -16.1
      },
      'October': {
        'Food & Drink': -59.08,
        'Travel': -197.03,
        'Miscellanous': 300.0,
        'Fees & Adjustments': -28.86,
        'Shopping': -18.0,
        'Entertainment': -39.49,
        'Health & Wellness': -16.91,
        'Education': -74.45
      },
      // Add more months if needed
    },
    topLargestTransactions: [
      { 'Transaction Date': '11/1/2023', 'Post Date': '11/1/2023', 'Description': 'Mobile Payment', 'Type': 'Payment', 'Amount': 500.0 },
      { 'Transaction Date': '11/29/2023', 'Post Date': '11/29/2023', 'Description': 'Mobile Payment',  'Type': 'Payment', 'Amount': 435.0 },
      { 'Transaction Date': '12/17/2023', 'Post Date': '12/17/2023', 'Description': 'Payment Confirmation', 'Type': 'Payment', 'Amount': 300.0 }
    ],
    incomeVsExpenses: {
      'Income': 1823.25,
      'Expenses': -1501.14,
      'Net Balance': 322.11
    },
    transactionFrequency: {
      'Entertainment': 6,
      'Groceries': 4,
      'Shopping': 8,
      'Miscellanous': 6,
      'Health & Wellness': 3,
      'Food & Drink': 45,
      'Fees & Adjustments': 4,
      'Travel': 21,
      'Gas': 1,
      'Education': 1,
      'Personal': 3,
      'Professional Services': 1
    },
    predictedCreditScore: 705
  };

  const cardData = [
    { title: 'Balance', description: 'Current account balance', key: 'balance' },
    { title: 'Category Spending', description: 'Spending by Category', key: 'categorySpending' },
    { title: 'Monthly Trends', description: 'Spending Trends', key: 'monthlyTrends' },
    { title: 'Largest Transactions', description: '3 biggest transactions', key: 'topLargestTransactions' },
    { title: 'Income vs Expenses', description: 'Comparison to track surplus or deficit.', key: 'incomeVsExpenses' },
    { title: 'Transaction Frequency', description: 'Frequency of transactions per category.', key: 'transactionFrequency' },
    { title: 'Predicted Credit Score', description: 'Credit Score', key: 'predictedCreditScore' },
  ];

  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      setUploadedFile(file);  // Simulate file upload and store it in state
      setSelectedCard(null);  // Clear any previously selected card
    }
  };
    { title: 'Balance', description: 'Current account balance', key: 'balance' },
    { title: 'Category Spending', description: 'Spending by Category', key: 'categorySpending' },
    { title: 'Monthly Trends', description: 'Spending Trends', key: 'monthlyTrends' },
    { title: 'Largest Transactions', description: '3 biggest transactions', key: 'topLargestTransactions' },
    { title: 'Income vs Expenses', description: 'Comparison to track surplus or deficit.', key: 'incomeVsExpenses' },
    { title: 'Transaction Frequency', description: 'Frequency of transactions per category.', key: 'transactionFrequency' },
    { title: 'Predicted Credit Score', description: 'Credit Score', key: 'predictedCreditScore' },
  ];

  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      setUploadedFile(file);  // Simulate file upload and store it in state
      setSelectedCard(null);  // Clear any previously selected card
    }
  };

  const closeModal = () => {
    setSelectedCard(null);
  };

  return (
    <div className="home-container">
      <div className="left-section">
      <h1>Welcome to U-Bank</h1>
      <p style={{ fontSize: '20px' }}>Making Banking easy and informative for you</p>
      <h1>Welcome to U-Bank</h1>
      <p style={{ fontSize: '20px' }}>Making Banking easy and informative for you</p>
        <div className="card-container">
          {cardData.map((card, index) => (
            <div
              key={index}
              className="gradient-card"
              onClick={() => setSelectedCard(card)}
            >
              <h2>{card.title}</h2>
            </div>
          ))}
        </div>
      </div>

      <div className="right-section">
        <Chatbot />
        <div className="file-upload-container">
          <label htmlFor="file-upload" className="file-upload-label">
            Upload File
          </label>
          <input
            type="file"
            id="file-upload"
            className="file-upload-input"
            onChange={handleFileUpload}
          />
        </div>
          <label htmlFor="file-upload" className="file-upload-label">
            Upload File
          </label>
          <input
            type="file"
            id="file-upload"
            className="file-upload-input"
            onChange={handleFileUpload}
          />
        </div>
      </div>

    

    

      {selectedCard && (
  <div className="modal-overlay" onClick={closeModal}>
    <div className="modal-content" onClick={(e) => e.stopPropagation()}>
      <button className="close-button" onClick={closeModal}>
        &times;
      </button>
      <h2>{selectedCard.title}</h2>
      <div className="card-content">
        {/* Render the hardcoded data dynamically based on the selected card */}
        {selectedCard.key && (
          <>
            {selectedCard.key === 'balance' && (
              <p>Account Balance: ${analysisData.balance["$322.11"]}</p>
            )}
            
            {selectedCard.key === 'categorySpending' && (
              <ul>
                {Object.entries(analysisData.categorySpending).map(([category, amount]) => (
                  <li key={category}>
                    {category}: ${amount.toFixed(2)}
                  </li>
                ))}
              </ul>
            )}

            {selectedCard.key === 'monthlyTrends' && (
              <>
                {Object.entries(analysisData.monthlyTrends).map(([month, trends]) => (
                  <div key={month}>
                    <h4>{month}</h4>
                    <ul>
                      {Object.entries(trends).map(([category, amount]) => (
                        <li key={category}>
                          {category || 'Unknown'}: ${amount.toFixed(2)}
                        </li>
                      ))}
                    </ul>
                  </div>
                ))}
              </>
            )}

            {selectedCard.key === 'topLargestTransactions' && (
              <table>
                <thead>
                  <tr>
                    <th>Transaction Date</th>
                    <th>Post Date</th>
                    <th>Description</th>
                    <th>Type</th>
                    <th>Amount</th>
                  </tr>
                </thead>
                <tbody>
                  {analysisData.topLargestTransactions.map((transaction, index) => (
                    <tr key={index}>
                      <td>{transaction["Transaction Date"]}</td>
                      <td>{transaction["Post Date"]}</td>
                      <td>{transaction.Description}</td>
                      <td>{transaction.Type}</td>
                      <td>${transaction.Amount.toFixed(2)}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            )}

            {selectedCard.key === 'incomeVsExpenses' && (
              <ul>
                {Object.entries(analysisData.incomeVsExpenses).map(([key, value]) => (
                  <li key={key}>
                    {key}: ${value.toFixed(2)}
                  </li>
                ))}
              </ul>
            )}

            {selectedCard.key === 'transactionFrequency' && (
              <ul>
                {Object.entries(analysisData.transactionFrequency).map(([category, frequency]) => (
                  <li key={category}>
                    {category || 'Unknown'}: {frequency} transactions
                  </li>
                ))}
              </ul>
            )}

            {selectedCard.key === 'predictedCreditScore' && (
              <p>Predicted Credit Score: {analysisData.predictedCreditScore}</p>
            )}
          </>
        )}
      </div>
    </div>
  </div>
)}
    </div>
  );
};

export default Home;