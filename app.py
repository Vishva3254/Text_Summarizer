from flask import Flask, request, jsonify
from transformers import pipeline
from transformers import T5Tokenizer, T5ForConditionalGeneration
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

# Extractive summary
def extract_summary(input_text):
    summarizer = pipeline("summarization")
    summary = summarizer(input_text, max_length=500, min_length=10)
    return summary

# Abstractive summary
def abstract_summary(input_text):
    checkpoint = "MBZUAI/LaMini-Flan-T5-248M"
    tokenizer = T5Tokenizer.from_pretrained(checkpoint)
    base_model = T5ForConditionalGeneration.from_pretrained(checkpoint)

    pipe_sum = pipeline(
        'summarization',
        model=base_model,
        tokenizer=tokenizer,
        max_length=500,
        min_length=10
    )
    summary = pipe_sum(input_text)
    return summary

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get("text", "")

    if len(text.split()) < 100:
        return jsonify({"error": "Text must be at least 100 words long."}), 400

    extractive_summary = extract_summary(text)
    abstractive_summary = abstract_summary(text)

    return jsonify({
        "extractive_summary": extractive_summary[0]['summary_text'],
        "abstractive_summary": abstractive_summary[0]['summary_text']
    })

if __name__ == "__main__":
    app.run(debug=True)
