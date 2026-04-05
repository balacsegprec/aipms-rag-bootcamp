from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "cross-encoder/ms-marco-MiniLM-L-12-v2"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

inputs = tokenizer(
    ["What is AI?", "What is AI?"],
    ["AI stands for artificial intelligence.", "Bananas are yellow."],
    padding=True, truncation=True, return_tensors="pt"
)

with torch.no_grad():
    scores = model(**inputs).logits

print(scores)
