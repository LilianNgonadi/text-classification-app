from flask import Flask, request, jsonify
import joblib

# Load the model and vectorizer
rf_model = joblib.load('rf_model.pkl')
tfidf = joblib.load('tfidf_vectorizer.pkl')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    text = data['text']
    text_tfidf = tfidf.transform([text])
    prediction = rf_model.predict(text_tfidf)
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
