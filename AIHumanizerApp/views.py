from django.shortcuts import render
import nltk
from nltk.tokenize import sent_tokenize
from rest_framework.response import Response
from rest_framework.decorators import api_view

import torch
from transformers import PegasusTokenizer, PegasusForConditionalGeneration

# Download sentence tokenizer
nltk.download('punkt')

# Load the model/tokenizer once
model_name = "tuner007/pegasus_paraphrase"
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name)

# Home Page
def index(request):
    return render(request, "index.html")

# Paraphrasing one sentence
def rephrase_sentence(sentence):
    inputs = tokenizer(sentence, truncation=True, padding="longest", return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=60,
            num_beams=5,
            num_return_sequences=1,
            temperature=1.5
        )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Processing full input
def humanize_text(text):
    sentences = sent_tokenize(text)
    rephrased = [rephrase_sentence(sentence) for sentence in sentences]
    return " ".join(rephrased)

# API Endpoint
@api_view(['POST'])
def humanize_text_api(request):
    input_text = request.data.get("text", "")
    if not input_text:
        return Response({"error": "No text provided"}, status=400)
    
    humanized = humanize_text(input_text)
    return Response({"humanized_text": humanized})
