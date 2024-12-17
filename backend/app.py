from flask import Flask, request, jsonify
from flask_cors import CORS
from routes.predict import predict_news

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Routes
@app.route('/')
def home():
    return "Real-Time Fake News Detection API"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get('news')
    result = predict_news(text)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
