from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


# @login_required(login_url='UserSignUpFxn')
def Dashboard(request):
    return render(request, 'app/dashboard.html')

def Nav(request):
    return render(request, 'generalapp.html')

@login_required(login_url='UserSignUpFxn')
def Deposite(request):
    return render(request, 'app/deposite.html')

# @login_required(login_url='UserSignUpFxn')
def ConfirmInvest(request):
    return render(request, 'app/confirminvest.html')

def Withdraw(request):
    return render(request, 'app/Withdraw.html')

def History(request):
    return render(request, 'app/history.html')

def Invest(request):
    return render(request, 'app/investment.html')


def Support(request):
    return render(request, 'app/support.html')


def Profile(request):
    return render(request, 'app/profile.html')



