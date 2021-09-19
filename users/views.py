from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        forma = UserRegistrationForm(request.POST)
        if forma.is_valid():
            forma.save()
            username = forma.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}! You can now login')
            return redirect('login')
    else:
        forma = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': forma})

@login_required
def profile(request):
    return render(request, 'users/profile.html')