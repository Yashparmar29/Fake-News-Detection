from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def fake_news_detection(request):
    result = None
    if request.method == 'POST':
        news_text = request.POST.get('news_text')
        # Placeholder for analysis logic
        result = f"Analyzed news: {news_text[:50]}... (Fake/Real detection logic here)"
    return render(request, 'fake_news_detection.html', {'result': result})

@login_required
def email_spam_detection(request):
    result = None
    if request.method == 'POST':
        email_content = request.POST.get('email_content')
        # Placeholder for analysis logic
        result = f"Analyzed email: {email_content[:50]}... (Spam/Ham detection logic here)"
    return render(request, 'email_spam_detection.html', {'result': result})
