from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fake-news-detection/', views.fake_news_detection, name='fake_news_detection'),
    path('email-spam-detection/', views.email_spam_detection, name='email_spam_detection'),
]
