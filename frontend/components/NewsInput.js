import { useState } from 'react';
import axios from 'axios';

function NewsInput() {
    const [news, setNews] = useState("");
    const [result, setResult] = useState("");

    const handleSubmit = async () => {
        const response = await axios.post("http://localhost:5000/predict", { news });
        setResult(response.data.prediction);
    };

    return (
        <div>
            <h1>Fake News Detector</h1>
            <textarea placeholder="Paste news here..." onChange={(e) => setNews(e.target.value)} />
            <button onClick={handleSubmit}>Check News</button>
            {result && <h2>Result: {result}</h2>}
        </div>
    );
}

export default NewsInput;
