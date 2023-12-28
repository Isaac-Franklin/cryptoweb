from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from useronboard.models import UserSignUp
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from django.db.models import Q

# Create your views here.




import platform
# Get the operating system name
import subprocess
import os
import time

current_time = time.ctime()
print(current_time)
# Print the operating system name



import requests
@login_required(login_url='UserSignUpFxn')
def Dashboard(request):
    currentUser = UserSignUp.objects.get(email = request.user.email)
    AllDueForWithdrawal = DueForWithdrawal.objects.filter(user=request.user).values_list('earnedamount', flat=True)
    latestWithdrawalReq = WithdrawalRequest.objects.filter(user=request.user).values_list('withdrawamount', flat=True).first()
    latestPendingWithdrawalReqs = WithdrawalRequest.objects.filter(Q(user=request.user) & Q(withdrawalRequestStatus = 'Pending')).values_list('withdrawamount', flat=True)
    print(latestPendingWithdrawalReqs                                                                                                      )
    if latestPendingWithdrawalReqs:
        totalPendingWithdrawalReqs = 0
        for i in latestPendingWithdrawalReqs:
            print(f'see {i}')
            totalPendingWithdrawalReqs = totalPendingWithdrawalReqs + int(i)
        # print(totalPendingWithdrawalReqs)
        totalPendingWithdrawalReqsMain = "${:,.2f}".format(totalPendingWithdrawalReqs)
    else:
        totalPendingWithdrawalReqsMain = 0

    if AllDueForWithdrawal:
        totalDueWithdrawal = 0
        for i in AllDueForWithdrawal:
            totalDueWithdrawal = totalDueWithdrawal + int(i)
        totalDueWithdrawalMain = "${:,.2f}".format(totalDueWithdrawal)
    else:
        AllDueForWithdrawal = 0
        totalDueWithdrawalMain = 0
    
    ApprovedDeposites = PotentialDeposite.objects.filter(Q(user = request.user) & Q(depositestatus = 'Approved')).values_list('amount', flat=True)
    if ApprovedDeposites:
        totalApprovedDeposites = 0
        for i in ApprovedDeposites:
            totalApprovedDeposites = totalApprovedDeposites + int(i)
        print(totalApprovedDeposites)
        totalApprovedDepositesMain = "${:,.2f}".format(totalApprovedDeposites)
    else:
        ApprovedDeposites = 0
        totalApprovedDepositesMain = 0

    LatestDeposites = PotentialDeposite.objects.filter(user=request.user).values_list('amount', flat=True).first()
    AllDeposites = PotentialDeposite.objects.filter(user=request.user).values_list('amount', flat=True)
    if AllDeposites:
        totalAllDeposites = 0
        for i in AllDeposites:
            totalAllDeposites = totalAllDeposites + int(i)
        # print(totalAllDeposites)
        totalAllDepositesMain = "${:,.2f}".format(totalAllDeposites)
    else:
        AllDeposites = 0
        totalAllDepositesMain = 0

    if currentUser is None:
        return redirect('UserSignUpFxn')
    browser_type = request.user_agent.browser.family
    browser_version = request.user_agent.browser.version_string
    os_type = request.user_agent.os.family
    os_version = request.user_agent.os.version_string
    os_name = platform.system()
    user_IP_Self = request.META.get('REMOTE_ADDR')
    context = {'currentUser':currentUser, 'browser_type':browser_type, 'os_type':os_type, 'user_IP_Self':user_IP_Self, 'totalApprovedDepositesMain':totalApprovedDepositesMain,
     'totalAllDepositesMain':totalAllDepositesMain, 'totalDueWithdrawalMain':totalDueWithdrawalMain, 'LatestDeposites':LatestDeposites,
     'latestWithdrawalReq':latestWithdrawalReq, 'totalPendingWithdrawalReqsMain' : totalPendingWithdrawalReqsMain}
    return render(request, 'app/dashboard.html', context)


def Nav(request):
    AllDueForWithdrawal = DueForWithdrawal.objects.filter(user=request.user).values_list('earnedamount', flat=True)        

    if AllDueForWithdrawal:
        totalDueWithdrawal = 0
        for i in AllDueForWithdrawal:
            totalDueWithdrawal = totalDueWithdrawal + int(i)
        totalDueWithdrawalMain = "${:,.2f}".format(totalDueWithdrawal)


    print(totalDueWithdrawalMain)
    context = {'totalDueWithdrawalMain':totalDueWithdrawalMain}
    return render(request, 'generalapp.html', context)


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
        PotentialDepositeForm = PotentialDeposite(user = request.user, depositeID = planIDMain, planSelected = planselected, amount = amount, wallet = wallet)
        PotentialDepositeForm.save()
        PotentialDepositeByID = PotentialDepositeForm.depositeID
        print(PotentialDepositeByID)
        return redirect('ConfirmDeposite', pk=PotentialDepositeByID)
    return render(request, 'app/deposite.html')


@login_required(login_url='UserSignUpFxn')
def ConfirmDeposite(request, pk):
    neworder = PotentialDeposite.objects.get(depositeID=pk)
    if request.method == 'POST':
        ConfrimedOrdersForm =  ConfrimedOrdersStatuses(user = request.user, depositeID = pk, depositestatus = 'Payment is made')
        ConfrimedOrdersForm.save()
        messages.success(request, 'Your deposite is currently pending and will be approved when confirmed.')
        return redirect('History')

    context = {'neworder': neworder}
    return render(request, 'app/confirmdeposite.html', context)


@login_required(login_url='UserSignUpFxn')
def ConfirmInvest(request):
    return render(request, 'app/confirminvest.html')


def Withdraw(request):
    AllDueForWithdrawal = DueForWithdrawal.objects.filter(user=request.user)
    AllWithdrawalRequest = WithdrawalRequest.objects.filter(user=request.user)
    if request.method == 'POST':
        withdrawalIDMain  = 'withdrawalRequest -'+ get_random_string(length=5)
        walletSelected = request.POST['walletselected']
        amountEntered = request.POST['amountEntered']
        cryptowalletID = request.POST['cryptowalletID']
        findAmountForWithdrawal = DueForWithdrawal.objects.filter(user=request.user).values_list('earnedamount', flat=True)
        # print(findAmountForWithdrawal)
        if findAmountForWithdrawal:
            totalDueForWithdrawal = 0
            for i in findAmountForWithdrawal:
                totalDueForWithdrawal = totalDueForWithdrawal + int(i)

            print(f'the sum of the numbers is: {totalDueForWithdrawal}')
            print(f'Amount user entered is {amountEntered}')

            if int(amountEntered) > int(totalDueForWithdrawal):
                messages.success(request, f'ERROR: You entered an amount greater than the amount in your wallet. Please enter an amount eqal to or below ${totalDueForWithdrawal}')
                return redirect('Withdraw')
            else:
                WithdrawalRequestForm = WithdrawalRequest(user=request.user, withdrawalID=withdrawalIDMain, withdrawamount=amountEntered, withdrawcrptocurrency=walletSelected,
                withdrawalRequestStatus='Pending', cryptowalletID=cryptowalletID)
                WithdrawalRequestForm.save()
                messages.success(request, 'Success! An admin will review your withdrawal request within the next 12 working hours.')
                return redirect('Withdraw')
    context = {'AllDueForWithdrawal':AllDueForWithdrawal, 'AllWithdrawalRequest':AllWithdrawalRequest}
    return render(request, 'app/Withdraw.html', context)


@login_required(login_url='UserSignUpFxn')
def History(request):
    # AllOrders = ConfrimedOrdersStatuses.objects.filter(user = request.user)
    OrderDetails = PotentialDeposite.objects.filter(user = request.user)
    if request.method == 'POST':
        print('form is checked')
        orderID = request.POST['orderID']
        orderamount = request.POST['orderamount']
        earnedamount = request.POST['earnedamount']
        ordercrptocurrency = request.POST['cryptocurrentcy']
        plan = request.POST['plan']
        DueForWithdrawalCheck = DueForWithdrawal.objects.filter(orderID = orderID)
        if DueForWithdrawalCheck:
            messages.success(request, 'This order has been updated for withdrawal already.')
            return redirect ('History')
        else:
            messages.success(request, 'You can request withdrawal for this deposite now.')
            DueForWithdrawalForm = DueForWithdrawal(user = request.user, plan = plan, orderID = orderID, orderamount = orderamount, earnedamount = earnedamount, ordercrptocurrency = ordercrptocurrency)
            DueForWithdrawalForm.save()

    context = { 'OrderDetails':OrderDetails}
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




def Logout(request):
    logout(request)
    messages.success(request, 'Logout Successful')
    return redirect('UserSignUpFxn')



