from transformers import pipeline
model_id = "cardiffnlp/twitter-roberta-base-sentiment-latest"
sentiment_pipeline = pipeline("sentiment-analysis", model = model_id)
data = ["I love you", "I hate you"]
print(sentiment_pipeline(data))