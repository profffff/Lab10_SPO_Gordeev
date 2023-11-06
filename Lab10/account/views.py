from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, UserCreationForm
from .librarian_logins import librarians_username


#входа
def sign_in(request):
    if request.method == 'GET':
      #  if request.user.is_authenticated:
       #     return redirect('home')

        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        #проверка формы
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # проверка вводимых данных
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi {username.title()}, welcome back!')
                return redirect('database_home')

        # either form not valid or user is not authenticated
        messages.error(request, f'Invalid username or password')
        return render(request, 'account/login.html', {'form': form})



def sign_up(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'account/register.html', {'form': form})

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()


            if user.username in librarians_username():
                user.is_staff = True

            user.save()

            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('database_home')
        else:
            return render(request, 'account/register.html', {'form': form})
