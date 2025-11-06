from django.shortcuts import render, redirect
    from django.contrib import messages
    from .forms import RegisterForm

    # Create your views here.
    def register(request):
        if request.method == 'POST':
            # User is submitting the form
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}! You can now log in.')
                return redirect('login') # We will create the 'login' page next
        else:
            # User is just viewing the page
            form = RegisterForm()
        
        # We will create this 'users/register.html' file in the next step
        return render(request, 'users/register.html', {'form': form})