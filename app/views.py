from django.shortcuts import render


# Create your views here.
from secrets import choice
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login

from app.models import User
from .forms import *
from django.contrib.auth.decorators import login_required
from .decorators import check_user_is_authenticated, user_required
from django.core.paginator import Paginator
# Create your views here.

@check_user_is_authenticated
def register_user(request):
    if request.method == 'POST':
        form = RegisterEmployee(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users/contas/login/')
    else:
        form = RegisterEmployee()
    return render(request, 'app/register.html', {'form':form})

# def login_user(request):
#     return render(request, 'users/login.html')







def index(request):
    return render(request, 'app/index.html')


def tables(request):
    return render(request, 'app/tables.html')


def register(request):
    return render(request, 'app/register.html')


def login(request):
    return render(request, 'app/login.html')


def charts(request):
    return render(request, 'app/charts.html')


def password(request):
    return render(request, 'app/password.html')
