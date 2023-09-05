from flask import Flask, request, jsonify
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="michellejieli/emotion_text_classifier")
app = Flask(__name__)
# the endpoint should be http://localhost:5000/api/v1?text=YOUR_TEXT_HERE
@app.route('/api/v1', methods=['GET'])
def classify():
    text = request.args.get('text')
    return classifier(text)

app.run(host='0.0.0.0', port=5000)