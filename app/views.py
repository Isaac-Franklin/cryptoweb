from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from useronboard.models import UserSignUp
from adminapp.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from django.db.models import Q
import math 
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail

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

    AllApprovedWithdrawalRequest = WithdrawalRequest.objects.filter(Q(user=request.user) & Q(withdrawalRequestStatus = 'Approved')).values_list('withdrawamount', flat=True)
    if AllApprovedWithdrawalRequest:
        totalAllApprovedWithdrawalRequest = 0
        for i in AllApprovedWithdrawalRequest:
            totalAllApprovedWithdrawalRequest = totalAllApprovedWithdrawalRequest + int(i)
        print(totalAllApprovedWithdrawalRequest)
        totalFretotalAllApprovedWithdrawalRequestMain = totalAllApprovedWithdrawalRequest
    else:
        totalFretotalAllApprovedWithdrawalRequestMain = 0

    AllPendingWithdrawalRequest = WithdrawalRequest.objects.filter(Q(user=request.user) & Q(withdrawalRequestStatus = 'Pending')).values_list('withdrawamount', flat=True)
    if AllPendingWithdrawalRequest:
        totalAllPendingWithdrawalRequest = 0
        for i in AllPendingWithdrawalRequest:
            totalAllPendingWithdrawalRequest = totalAllPendingWithdrawalRequest + int(i)
        totalAllPendingWithdrawalRequestMain = totalAllPendingWithdrawalRequest
    else:
        totalAllPendingWithdrawalRequestMain = 0

    AllFreeWithdrawalBalance = totalAllPendingWithdrawalRequestMain + totalFretotalAllApprovedWithdrawalRequestMain

    latestWithdrawalReq = WithdrawalRequest.objects.filter(user=request.user).values_list('withdrawamount', flat=True).first()
    latestPendingWithdrawalReqs = WithdrawalRequest.objects.filter(Q(user=request.user) & Q(withdrawalRequestStatus = 'Pending')).values_list('withdrawamount', flat=True)
    if latestPendingWithdrawalReqs:
        totalPendingWithdrawalReqs = 0
        for i in latestPendingWithdrawalReqs:
            totalPendingWithdrawalReqs = totalPendingWithdrawalReqs + int(i)
        totalPendingWithdrawalReqsMain = "${:,.2f}".format(totalPendingWithdrawalReqs)
    else:
        totalPendingWithdrawalReqsMain = 0

    AllDueForWithdrawal = DueForWithdrawal.objects.filter(user=request.user).values_list('earnedamount', flat=True)
    if AllDueForWithdrawal:
        totalDueWithdrawal = 0
        for i in AllDueForWithdrawal:
            totalDueWithdrawal = totalDueWithdrawal + int(float(i))
        print(totalDueWithdrawal)

        totalDueWithdrawalMainPre  = totalDueWithdrawal - AllFreeWithdrawalBalance
        totalDueWithdrawalMain = "${:,.2f}".format(totalDueWithdrawalMainPre)
        # print(totalDueWithdrawalMain)

    else:
        totalDueWithdrawalMain = '$0'
        totalDueWithdrawalDraft = 0
    
    ApprovedDeposites = PotentialDeposite.objects.filter(Q(user = request.user) & Q(depositestatus = 'Approved')).values_list('amount', flat=True)
    if ApprovedDeposites:
        totalApprovedDeposites = 0
        for i in ApprovedDeposites:
            totalApprovedDeposites = totalApprovedDeposites + int(float(i))
        # print(totalApprovedDeposites)
        totalApprovedDepositesMain = "${:,.2f}".format(totalApprovedDeposites)
    else:
        ApprovedDeposites = 0
        totalApprovedDepositesMain = 0

    LatestDeposites = PotentialDeposite.objects.filter(user=request.user).values_list('amount', flat=True).first()
    AllDeposites = PotentialDeposite.objects.filter(Q(user=request.user) & Q(depositestatus = 'Approved')).values_list('amount', flat=True)
    if AllDeposites:
        totalAllDeposites = 0
        for i in AllDeposites:
            totalAllDeposites = totalAllDeposites + int(float(i))
        # print(totalAllDeposites)
        totalAllDepositesMain = "${:,.2f}".format(totalAllDeposites)
    else:
        AllDeposites = 0
        totalAllDepositesMain = 0
   
   
    PendingDeposites = PotentialDeposite.objects.filter(Q(user=request.user) & Q(depositestatus = 'Pending')).values_list('amount', flat=True)
    if PendingDeposites:
        totalPendingDeposites = 0
        for i in PendingDeposites:
            totalPendingDeposites = totalPendingDeposites + int(float(i))
        # print(totalPendingDeposites)
        totalPendingDepositesMain = "${:,.2f}".format(totalPendingDeposites)
    else:
        PendingDeposites = 0
        totalPendingDepositesMain = 0

    if currentUser is None:
        return redirect('UserSignUpFxn')
    browser_type = request.user_agent.browser.family
    browser_version = request.user_agent.browser.version_string
    os_type = request.user_agent.os.family
    os_version = request.user_agent.os.version_string
    os_name = platform.system()
    user_IP_Self = request.META.get('REMOTE_ADDR')
    context = {'totalPendingDepositesMain':totalPendingDepositesMain, 'currentUser':currentUser, 'browser_type':browser_type, 'os_type':os_type, 'user_IP_Self':user_IP_Self, 'totalApprovedDepositesMain':totalApprovedDepositesMain,
     'totalAllDepositesMain':totalAllDepositesMain, 'totalDueWithdrawalMain':totalDueWithdrawalMain, 'LatestDeposites':LatestDeposites,
     'latestWithdrawalReq':latestWithdrawalReq, 'totalPendingWithdrawalReqsMain' : totalPendingWithdrawalReqsMain}
    return render(request, 'app/dashboard.html', context)


def Nav(request):
    AllDueForWithdrawal = DueForWithdrawal.objects.filter(user=request.user).values_list('earnedamount', flat=True)        

    if AllDueForWithdrawal:
        totalDueWithdrawal = 0
        for i in AllDueForWithdrawal:
            totalDueWithdrawal = totalDueWithdrawal + int(float(i))
        totalDueWithdrawalMain = "${:,.2f}".format(totalDueWithdrawal)


    print(totalDueWithdrawalMain)
    context = {'totalDueWithdrawalMain':totalDueWithdrawalMain}
    return render(request, 'generalapp.html', context)


@login_required(login_url='UserSignUpFxn')
def Deposite(request):
    AllAppPlans = AppPlans.objects.all()

    BronzePlan = AppPlans.objects.get(planname = 'Bronze Plan')
    BronzePlanMinValue = AppPlans.objects.filter(planname = 'Bronze Plan').values_list('minamount', flat=True)[0]
    BronzePlanMaxValue = AppPlans.objects.filter(planname = 'Bronze Plan').values_list('maxamount', flat=True)[0]
    print(type(int(BronzePlanMinValue)))
    
    SilverPlan = AppPlans.objects.get(planname = 'Silver plan')
    SilverPlanMinValue = AppPlans.objects.filter(planname = 'Silver plan').values_list('minamount', flat=True)[0]
    SilverPlanMaxValue = AppPlans.objects.filter(planname = 'Silver plan').values_list('maxamount', flat=True)[0]

    GoldPlan = AppPlans.objects.get(planname = 'Gold plan')
    GoldPlanMinValue = AppPlans.objects.filter(planname = 'Gold plan').values_list('minamount', flat=True)[0]
    GoldPlanMaxValue = AppPlans.objects.filter(planname = 'Gold plan').values_list('maxamount', flat=True)[0]
    
    DiamondPlan = AppPlans.objects.filter(planname = 'Diamond plan')
    DiamondPlanMinValue = AppPlans.objects.filter(planname = 'Diamond plan').values_list('minamount', flat=True)[0]
    DiamondPlanMaxValue = AppPlans.objects.filter(planname = 'Diamond plan').values_list('maxamount', flat=True)[0]

    if request.method == 'POST':
        planselected = request.POST['planselected']
        wallet = request.POST['wallet']
        amount = request.POST['amount']
        print(f'{planselected}, {wallet}, {amount}')
        if planselected == 'bronzeplan':
            print('bronze selected')
            if int(request.POST['amount']) < int(BronzePlanMinValue):
                messages.error(request, f'ERROR: You entered an amount less than ${BronzePlanMinValue} for the Bronze plan. Please try again.')
                return redirect('Deposite')
            elif int(request.POST['amount']) > int(BronzePlanMaxValue):
                messages.error(request, f'ERROR: You entered an amount more than ${BronzePlanMaxValue} for the Bronze plan. Please select a higher plan.')
                return redirect('Deposite')
       
        if planselected == 'silverplan':
            print('silver selected')
            if int(request.POST['amount']) < int(SilverPlanMinValue):
                messages.error(request, f'ERROR: You entered an amount less than ${SilverPlanMinValue} for the Silver plan. Please try again.')
                return redirect('Deposite')
            elif int(request.POST['amount']) > int(SilverPlanMaxValue):
                messages.error(request, f'ERROR: You entered an amount more than ${SilverPlanMaxValue} for the Silver plan. Please select a higher plan.')
                return redirect('Deposite')
       
        if planselected == 'goldplan':
            print('gold selected')
            if int(request.POST['amount']) < int(GoldPlanMinValue):
                messages.error(request, f'ERROR: You entered an amount less than ${GoldPlanMinValue} for the Gold plan. Please try again.')
                return redirect('Deposite')
            elif int(request.POST['amount']) > int(GoldPlanMaxValue):
                messages.error(request, f'ERROR: You entered an amount more than ${GoldPlanMaxValue} for the Gold plan. Please select a higher plan.')
                return redirect('Deposite')
            
       
        if planselected == 'diamondplan':
            print('diamond selected')
            if int(request.POST['amount']) < int(DiamondPlanMinValue):
                messages.error(request, f'ERROR: You entered an amount less than ${DiamondPlanMinValue} for the Diamond plan. Enter a higher amount for this plan.')
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
    BTCWalletID = list(WalletIDs.objects.all().values_list('btc', flat=True))
    BTCWalletIDMain = BTCWalletID[0]
    BNBWalletID = WalletIDs.objects.all().values_list('bnb', flat=True)
    BNBWalletIDMain = BNBWalletID[0]
    USDTWalletID = WalletIDs.objects.all().values_list('usdt', flat=True)
    USDTWalletIDMain = USDTWalletID[0]
    TRONWalletID = WalletIDs.objects.all().values_list('tron', flat=True)
    TRONWalletIDMain = TRONWalletID[0]
    if request.method == 'POST':
        ConfrimedOrdersForm =  ConfrimedOrdersStatuses(user = request.user, depositeID = pk, depositestatus = 'Payment is made')
        ConfrimedOrdersForm.save()
        messages.success(request, 'Your deposite is currently pending and will be approved when confirmed.')
        return redirect('History')

    context = {'neworder': neworder, 'BTCWalletIDMain':BTCWalletIDMain, 'BNBWalletIDMain':BNBWalletIDMain, 'USDTWalletIDMain':USDTWalletIDMain, 'TRONWalletIDMain':TRONWalletIDMain}
    return render(request, 'app/confirmdeposite.html', context)


@login_required(login_url='UserSignUpFxn')
def ConfirmInvest(request):
    return render(request, 'app/confirminvest.html')


def Withdraw(request):
    AllDueForWithdrawal = DueForWithdrawal.objects.filter(user=request.user)
    AllWithdrawalRequest = WithdrawalRequest.objects.filter(user=request.user)
    
    # FIND ACCOUNT BALANCE BELOW
    AllApprovedWithdrawalRequest = WithdrawalRequest.objects.filter(Q(user=request.user) & Q(withdrawalRequestStatus = 'Approved')).values_list('withdrawamount', flat=True)
    print(AllApprovedWithdrawalRequest)
    if AllApprovedWithdrawalRequest:
        totalAllApprovedWithdrawalRequest = 0
        for i in AllApprovedWithdrawalRequest:
            totalAllApprovedWithdrawalRequest = totalAllApprovedWithdrawalRequest + int(i)
        print(totalAllApprovedWithdrawalRequest)
        totalFretotalAllApprovedWithdrawalRequestMain = totalAllApprovedWithdrawalRequest
    else:
        totalFretotalAllApprovedWithdrawalRequestMain = 0

    AllPendingWithdrawalRequest = WithdrawalRequest.objects.filter(Q(user=request.user) & Q(withdrawalRequestStatus = 'Pending')).values_list('withdrawamount', flat=True)
    print(AllPendingWithdrawalRequest)
    if AllPendingWithdrawalRequest:
        totalAllPendingWithdrawalRequest = 0
        for i in AllPendingWithdrawalRequest:
            totalAllPendingWithdrawalRequest = totalAllPendingWithdrawalRequest + int(i)
        totalAllPendingWithdrawalRequestMain = totalAllPendingWithdrawalRequest
    else:
        totalAllPendingWithdrawalRequestMain = 0

    AllFreeWithdrawalBalance = totalAllPendingWithdrawalRequestMain + totalFretotalAllApprovedWithdrawalRequestMain
    print(f'{AllFreeWithdrawalBalance} 272')

    AllDueForWithdrawal = DueForWithdrawal.objects.filter(user=request.user).values_list('earnedamount', flat=True)
    print(f'{AllDueForWithdrawal} here')
    if AllDueForWithdrawal:
        totalDueWithdrawal = 0
        for i in AllDueForWithdrawal:
            totalDueWithdrawal = totalDueWithdrawal + int(float(i))
        print(f'{totalDueWithdrawal} total')


    UserAccountBalance = totalDueWithdrawal - AllFreeWithdrawalBalance
    print(f'{UserAccountBalance}')

    
    findAmountForWithdrawal = DueForWithdrawal.objects.filter(user=request.user).values_list('earnedamount', flat=True)
    # print(findAmountForWithdrawal)
    if request.method == 'POST':
        withdrawalIDMain  = 'withdrawalRequest -'+ get_random_string(length=5)
        walletSelected = request.POST['walletselected']
        amountEntered = math.floor(int(request.POST['amountEntered']))
        cryptowalletID = request.POST['cryptowalletID']
        if findAmountForWithdrawal:
            totalDueForWithdrawal = 0
            for i in findAmountForWithdrawal:
                totalDueForWithdrawal = totalDueForWithdrawal + int(float(i))

            # if int(amountEntered) > int(totalDueForWithdrawal):
            if int(amountEntered) > int(UserAccountBalance):
                messages.success(request, f'ERROR: You entered an amount greater than the amount in your wallet. Your account balance is ${UserAccountBalance}')
                return redirect('Withdraw')
            else:
                WithdrawalRequestForm = WithdrawalRequest(user=request.user, withdrawalID=withdrawalIDMain, withdrawamount=amountEntered, withdrawcrptocurrency=walletSelected,
                withdrawalRequestStatus='Pending', cryptowalletID=cryptowalletID)
                WithdrawalRequestForm.save()
                messages.success(request, 'Success! An admin will review your withdrawal request within the next 12 working hours.')
                return redirect('Withdraw')
    context = {'UserAccountBalance':UserAccountBalance, 'AllDueForWithdrawal':AllDueForWithdrawal, 'AllWithdrawalRequest':AllWithdrawalRequest}
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

