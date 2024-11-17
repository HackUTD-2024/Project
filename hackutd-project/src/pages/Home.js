import React from 'react';
import Chatbot from '../componets/Chatbot';

const Home = () => {
  return (
    <div className="home-container">
      <div className="left-section">
        <h1>Welcome to the AI Chatbot</h1>
        <p>This is the left side of the homepage.</p>
      </div>
      <div className="right-section">
        <Chatbot/>
      </div>s
    </div>
  );
};

export default Home;
