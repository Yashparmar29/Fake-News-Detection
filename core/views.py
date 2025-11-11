from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from transformers import pipeline

# Load the fake news detection model pipeline
fake_news_classifier = pipeline("text-classification", model="mrm8488/bert-tiny-finetuned-fake-news-detection")

# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def fake_news_detection(request):
    result = None
    if request.method == 'POST':
        news_text = request.POST.get('news_text')
        if news_text:
            # Perform prediction
            prediction = fake_news_classifier(news_text)[0]
            label = prediction['label']
            confidence = prediction['score']
            if label == 'LABEL_0':
                result = f"Real News (Confidence: {confidence:.2f})"
            else:
                result = f"Fake News (Confidence: {confidence:.2f})"
        else:
            result = "Please enter news text to analyze."
    return render(request, 'fake_news_detection.html', {'result': result})

@login_required
def email_spam_detection(request):
    result = None
    if request.method == 'POST':
        email_content = request.POST.get('email_content')
        # Placeholder for analysis logic
        result = f"Analyzed email: {email_content[:50]}... (Spam/Ham detection logic here)"
    return render(request, 'email_spam_detection.html', {'result': result})
