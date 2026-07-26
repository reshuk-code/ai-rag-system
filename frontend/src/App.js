import React, { useState } from 'react';
import './App.css';

function App() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setResponse('');

    try {
      // Step 1: Retrieve context
      const retrievalResponse = await fetch('http://localhost:8005/retrieve/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: query }),
      });

      if (!retrievalResponse.ok) {
        throw new Error(`Retrieval failed: ${retrievalResponse.statusText}`);
      }
      const retrievalData = await retrievalResponse.json();
      const context = retrievalData.context;

      // Step 2: Generate response
      const generationResponse = await fetch('http://localhost:8006/generate/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query, context }),
      });

      if (!generationResponse.ok) {
        throw new Error(`Generation failed: ${generationResponse.statusText}`);
      }
      const generationData = await generationResponse.json();
      setResponse(generationData.response);

    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>AI-powered RAG System</h1>
      </header>
      <main className="main-content">
        <form onSubmit={handleSubmit} className="query-form">
          <textarea
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Ask a question..."
            rows="5"
            disabled={loading}
          ></textarea>
          <button type="submit" disabled={loading}>
            {loading ? 'Processing...' : 'Get Answer'}
          </button>
        </form>

        {error && <p className="error-message">Error: {error}</p>}

        {response && (
          <div className="response-container">
            <h2>Answer:</h2>
            <p>{response}</p>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
