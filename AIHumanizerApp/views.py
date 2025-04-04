from django.shortcuts import render
import random
import nltk
from textblob import TextBlob
from nltk.tokenize import sent_tokenize
from rest_framework.response import Response
from rest_framework.decorators import api_view

def index(request):
    nltk.download('punkt_tab')
    return render(request,"index.html")

nltk.download('punkt')

def humanize_text(text):
    """Processes AI-generated text and makes it sound more human-like."""
    sentences = sent_tokenize(text)  # Break text into sentences
    random.shuffle(sentences)  # Shuffle for natural flow
    improved_sentences = [str(TextBlob(sentence).correct()) for sentence in sentences]  # Grammar correction
    return " ".join(improved_sentences)

@api_view(['POST'])
def humanize_text_api(request):
    print("running!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    """Receives text from frontend and returns humanized text."""
    input_text = request.data.get("text", "")
    if not input_text:
        return Response({"error": "No text provided"}, status=400)
    
    humanized = humanize_text(input_text)
    return Response({"humanized_text": humanized})
