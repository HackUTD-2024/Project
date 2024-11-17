import React, { useState } from 'react';
import Chatbot from '../componets/Chatbot';
import { Chart as ChartJS, ArcElement, Tooltip, Legend, LineElement, CategoryScale, LinearScale } from 'chart.js';

ChartJS.register(ArcElement, Tooltip, Legend, LineElement, CategoryScale, LinearScale);


const Home = () => {
  const [selectedCard, setSelectedCard] = useState(null);

  const cardData = [
    { title: 'Balance', description: 'Current account balance.', chart: null, },
    { title: 'Category Spending', description: 'Pie chart', chart: null, },
    { title: 'Monthly Trends', description: 'Bar graph for spending trends by month.', chart: null, },
    { title: 'Largest Transactions', description: '3 biggest transactions', chart: null, },
    { title: 'Trend Forecasting', description: 'Spending trend analysis to forecast future trends by category.', chart: null, },
    { title: 'Income vs Expenses', description: 'comparison to track surplus or deficit.', chart: null, },
    { title: 'Transaction Frequency', description: 'Frequency of transactions per category.', chart: null, },
    { title: 'Predicted Credit Score', description: 'Credit Score', chart: null, },
  ];

  const closeModal = () => {
    setSelectedCard(null);
  };

  return (
    <div className="home-container">
      <div className="left-section">
        <h1>Welcome to U-Bank</h1>
        <p style={{ fontSize: '13x' }}>Making Banking easy and infromative for you</p>
        <div className="card-container">
          {cardData.map((card, index) => (
            <div
              key={index}
              className="gradient-card"
              onClick={() => setSelectedCard(card)}
            >
              <h2>{card.title}</h2>
              <p>{card.description}</p>
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
      onChange={(e) => console.log(e.target.files[0])}
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
            <p>{selectedCard.description}</p>
          </div>
        </div>
      )}
    </div>
  );
};

export default Home;
