from transformers import pipeline

classifier = pipeline("sentiment-analysis",
                      model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")
response = classifier("i like large language models very much")
print(response)