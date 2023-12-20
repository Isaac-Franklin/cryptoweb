from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from useronboard.models import UserSignUp
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string

# Create your views here.




import platform
# Get the operating system name
import subprocess
import os

# Print the operating system name



import requests
@login_required(login_url='UserSignUpFxn')
def Dashboard(request):
    currentUser = UserSignUp.objects.get(email = request.user.email)
    browser_type = request.user_agent.browser.family
    browser_version = request.user_agent.browser.version_string
    os_type = request.user_agent.os.family
    os_version = request.user_agent.os.version_string
    os_name = platform.system()
    user_IP_Self = request.META.get('REMOTE_ADDR')
    context = {'currentUser':currentUser, 'browser_type':browser_type, 'os_type':os_type, 'user_IP_Self':user_IP_Self}
    return render(request, 'app/dashboard.html', context)


def Nav(request):
    return render(request, 'generalapp.html')


@login_required(login_url='UserSignUpFxn')
def Deposite(request):
    if request.method == 'POST':
        planselected = request.POST['planselected']
        wallet = request.POST['wallet']
        amount = request.POST['amount']
        print(f'{planselected}, {wallet}, {amount}')
        if planselected == 'bronzeplan':
            if int(request.POST['amount']) < 30:
                messages.error(request, 'ERROR: You entered an amount less than $30 for the Bronze plan. Please try again.')
                return redirect('Deposite')
            elif int(request.POST['amount']) > 499:
                messages.error(request, 'ERROR: You entered an amount more than $499 for the Bronze plan. Please select a higher plan.')
                return redirect('Deposite')
       
        if planselected == 'silverplan':
            if int(request.POST['amount']) < 500:
                messages.error(request, 'ERROR: You entered an amount less than $500 for the Silver plan. Please try again.')
                return redirect('Deposite')
            elif int(request.POST['amount']) > 3999:
                messages.error(request, 'ERROR: You entered an amount more than $3,999 for the Silver plan. Please select a higher plan.')
                return redirect('Deposite')
       
        if planselected == 'goldplan':
            if int(request.POST['amount']) < 4000:
                messages.error(request, 'ERROR: You entered an amount less than $4,000 for the Gold plan. Please try again.')
                return redirect('Deposite')
            elif int(request.POST['amount']) > 29999:
                messages.error(request, 'ERROR: You entered an amount more than $2,999 for the Gold plan. Please select a higher plan.')
                return redirect('Deposite')
            
       
        if planselected == 'diamondplan':
            if int(request.POST['amount']) < 30000:
                messages.error(request, 'ERROR: You entered an amount less than $30,000 for the Diamond plan. Enter a higher amount for this plan.')
                return redirect('Deposite')
        planIDMain = planselected +'-'+ get_random_string(length=10)
        PotentialDepositeForm = PotentialDeposite(user = request.user, planID = planIDMain, planSelected = planselected, amount = amount, wallet = wallet)
        PotentialDepositeForm.save()
        PotentialDepositeByID = PotentialDepositeForm.id
        print(PotentialDepositeByID)
        return redirect('ConfirmDeposite', pk=PotentialDepositeByID)
    return render(request, 'app/deposite.html')


@login_required(login_url='UserSignUpFxn')
def ConfirmDeposite(request, pk):
    neworder = PotentialDeposite.objects.get(id=pk)
    if request.method == 'POST':
        ConfrimedOrdersForm =  ConfrimedOrdersStatuses(user = request.user, orderID = pk, depositestatus = 'Pending')
        ConfrimedOrdersForm.save()
        messages.success(request, 'Your deposite is currently pending and will be approved when confirmed.')
        return redirect('History')

    context = {'neworder': neworder}
    return render(request, 'app/confirmdeposite.html', context)


@login_required(login_url='UserSignUpFxn')
def ConfirmInvest(request):
    return render(request, 'app/confirminvest.html')


def Withdraw(request):
    return render(request, 'app/Withdraw.html')


@login_required(login_url='UserSignUpFxn')
def History(request):
    AllOrders = ConfrimedOrdersStatuses.objects.filter(user = request.user)
    OrderDetails = PotentialDeposite.objects.filter(user = request.user)
    context = {'AllOrders': AllOrders, 'OrderDetails':OrderDetails}
    return render(request, 'app/history.html', context)


def Invest(request):
    return render(request, 'app/investment.html')


def Support(request):
    return render(request, 'app/support.html')



def BannerAd(request):
    return render(request, 'app/bannerad.html')



@login_required(login_url='UserSignUpFxn')
def ReferalFxn(request):
    # currentUser = UserSignUp.objects.get(email = request.user.email)
    AllReferals = ReferalData.objects.filter(refererEmail = request.user.email)
    context = {'AllReferals':AllReferals}
    return render(request, 'app/referal.html', context)


def Profile(request):
    return render(request, 'app/profile.html')


@login_required(login_url='UserSignUpFxn')
def ReferedUser(request, username):
    findReferer = UserSignUp.objects.get(username = username)
    # FindDeviceUserEmail = FamilyMemberReg.objects.filter(Q(user = request.user) & Q(memberid = request.POST['deviceUserID']))
    # FindDeviceUserEmailMain = FindDeviceUserEmail.values_list('memberemail', flat=True)
    findRefererEmail = findReferer.email
    if findReferer:
        ReferalDataForm = ReferalData(user = request.user, refererUsername = username, refererEmail = findRefererEmail)
        ReferalDataForm.save()
    return render(request, 'app/dashboard.html')
