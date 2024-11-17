import React, { useState } from 'react';

const Chatbot = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const handleSendMessage = () => {
    if (input.trim()) {
      const newMessages = [...messages, { text: input, sender: 'user' }];
      setMessages(newMessages);

      setTimeout(() => {
        const botResponse = { text: 'Hello, how can I assist you?', sender: 'bot' };
        setMessages((prevMessages) => [...prevMessages, botResponse]);
      }, 1000);

      setInput('');
    }
  };

  return (
    <div className="chatbot-container">
      <h2 className="chatbot-title">Chatbot</h2>
      <div className="chat-window">
        {messages.map((message, index) => (
          <div
            key={index}
            className={`message-bubble ${message.sender === 'user' ? 'user-message' : 'bot-message'}`}
          >
            <p>{message.text}</p>
          </div>
        ))}
      </div>
      <div className="input-container">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type a message"
        />
        <button onClick={handleSendMessage}>Send</button>
      </div>
    </div>
  );
};

export default Chatbot;
