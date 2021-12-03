from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm

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
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)