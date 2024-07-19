from django.shortcuts import render, redirect
# from . import models
from . import forms
from . import coreutils
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.db.models import Q
from django.contrib.auth import authenticate, login, logout


def main(request):
    city = request.GET.get('city') if request.GET.get('city') else ''

    try:
        with open("last_city.csv", "a+", encoding="UTF8") as file:
            file.write(f"{city}\n")

        with open('last_city.csv', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            cities: list = list()

        for line in lines:
            city = line.strip('\n')
            cities.append(city)

    except FileNotFoundError:
        with open("last_city.csv", "w+", encoding="UTF8") as file:
            file.write(f"{city}\n")

        cities: list = list()
        return cities

    coreutils.write_to_json(city)
    forecast = coreutils.read_from_json()

    context = {'city': city, 'forecast': forecast, 'last_cities': cities}
    return render(request, 'base/main.htm', context=context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('main')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        # noinspection PyBroadException
        try:
            login(request, user)
            return redirect('main')
        except BaseException:
            messages.error(request, "Email adress or password is incorrect")

    return render(request, 'base/login.htm')


def registration_page(request):
    if request.user.is_authenticated:
        return redirect('main')

    form = forms.UserCreationForm

    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            form.save()
            login(request, user)
            return redirect('main')
        else:
            messages.error(request, "Your password is weak or Fields are filled incorrectly")

    context = {'form': form}
    return render(request, 'base/registration.htm', context)


@login_required(login_url='login')
def logout_page(request):
    logout(request)
    return redirect('main')
