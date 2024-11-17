import React, { useState } from 'react';
import ReactMarkdown from 'react-markdown';

const Chatbot = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const handleSendMessage = async () => {
    if (input.trim()) {
      const newMessages = [...messages, { text: input, sender: 'user' }];
      setMessages(newMessages);

      try {
        const response = await fetch('http://127.0.0.1:5000/api/ask', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ message: input }),
        });

        if (response.ok) {
          const data = await response.json();
          console.log('Response from backend:', data);

          const botResponse = { text: data.response, sender: 'bot' };
          setMessages((prevMessages) => [...prevMessages, botResponse]);
        } else {
          console.error('Error with API response:', response.statusText);
        }
      } catch (error) {
        console.error('Error communicating with backend:', error);
      }

      setInput('');
    }
  };

  return (
    <div className="chatbot-container">
      <div className="chat-window">
        {messages.map((message, index) => (
          <div key={index} className={message.sender}>
            <p><ReactMarkdown className="react-markdown">{message.text}</ReactMarkdown></p>
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
