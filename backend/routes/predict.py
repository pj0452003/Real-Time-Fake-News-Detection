from joblib import load

# Load pre-trained ML model
model = load("model/fake_news_model.joblib")

def predict_news(text):
    if not text:
        return {"error": "No text provided"}
    prediction = model.predict([text])[0]
    return {"prediction": "Fake" if prediction == 0 else "Real"}
