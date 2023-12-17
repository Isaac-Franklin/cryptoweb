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
            if int(request.POST['amount']) > 30000:
                messages.error(request, 'ERROR: You entered an amount less than $30,000 for the Diamond plan. Enter a higher amount for this plan.')
                return redirect('Deposite')

        PotentialDepositeForm = PotentialDeposite(user = request.user, planSelected = planselected, amount = amount, wallet = wallet)
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
        return redirect('Dashboard')

    context = {'neworder': neworder}
    return render(request, 'app/confirmdeposite.html', context)


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



def BannerAd(request):
    return render(request, 'app/bannerad.html')



def ReferalFxn(request):
    return render(request, 'app/referal.html')


def Profile(request):
    return render(request, 'app/profile.html')



