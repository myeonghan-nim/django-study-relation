from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')
    else:
        form = UserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'account/forms.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('post:index')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'account/forms.html', context)


def logout(request):
    auth_logout(request)
    return redirect('account:login')
