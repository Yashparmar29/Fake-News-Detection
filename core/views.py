from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    result = None
    if request.method == 'POST':
        if 'news_text' in request.POST:
            # Handle news analysis
            news_text = request.POST.get('news_text')
            # Placeholder for analysis logic
            result = f"Analyzed news: {news_text[:50]}... (Fake/Real detection logic here)"
        elif 'email_content' in request.POST:
            # Handle email analysis
            email_content = request.POST.get('email_content')
            # Placeholder for analysis logic
            result = f"Analyzed email: {email_content[:50]}... (Spam/Ham detection logic here)"
        else:
            result = "No valid input provided."
    return render(request, 'home.html', {'result': result})
