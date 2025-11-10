from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Registration Page
    path('register/', views.register, name='register'),

    # Login/Logout Pages (using Django's built-in views)
    # We will create the templates for these in the next step
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

]
