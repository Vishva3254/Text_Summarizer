import React, { useState } from 'react';
import './App.css'; // For styling

function App() {
  const [text, setText] = useState('');
  const [extractiveSummary, setExtractiveSummary] = useState('');
  const [abstractiveSummary, setAbstractiveSummary] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  // Handle text input change
  const handleTextChange = (e) => {
    setText(e.target.value);
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (text.split(" ").length < 100) {
      setErrorMessage("Text must be at least 100 words.");
      return;
    }

    try {
      const response = await fetch('/summarize', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: text }),
      });

      if (!response.ok) {
        throw new Error('Error in summarizing');
      }

      const data = await response.json();
      setExtractiveSummary(data.extractive_summary);
      setAbstractiveSummary(data.abstractive_summary);
      setErrorMessage('');
    } catch (error) {
      setErrorMessage("There was an error processing your request.");
      console.error(error);
    }
  };

  return (
    <div className="App">
      <h1>Text Summarizer</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          value={text}
          onChange={handleTextChange}
          placeholder="Enter at least 100 words"
          rows="10"
          cols="50"
        />
        <button className="subbut" type="submit">Summarize</button>
      </form>
      {errorMessage && <p className="error">{errorMessage}</p>}
      <div className="summaries">
        <div className="summary">
          <h2>Extractive Summary</h2>
          <p>{extractiveSummary}</p>
        </div>
        <div className="summary">
          <h2>Abstractive Summary</h2>
          <p>{abstractiveSummary}</p>
        </div>
      </div>
    </div>
  );
}

export default App;
