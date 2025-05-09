from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from useronboard.models import UserSignUp
# from adminapp.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from django.db.models import Q
import math 
# from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.shortcuts import redirect


# Create your views here.

def custom_csrf_failure(request, reason=""):
    # You can log the reason here if you want
    return redirect('/') 


import platform
# Get the operating system name
import subprocess
import os
import time

current_time = time.ctime()
# Print the operating system name



# import requests
@login_required(login_url='UserSignUpFxn')
def Dashboard(request):
    currentUser = UserSignUp.objects.filter(email = request.user.email)
    AllApprovedWithdrawalRequest = WithdrawalRequest.objects.filter(Q(user=request.user) & Q(withdrawalRequestStatus = 'Approved')).values_list('withdrawamount', flat=True)
    if AllApprovedWithdrawalRequest:
        totalAllApprovedWithdrawalRequest = 0
        for i in AllApprovedWithdrawalRequest:
            totalAllApprovedWithdrawalRequest = totalAllApprovedWithdrawalRequest + int(i)
        totalFretotalAllApprovedWithdrawalRequestMain = totalAllApprovedWithdrawalRequest
    else:
        totalFretotalAllApprovedWithdrawalRequestMain = 0
    
    totalAllApprovedWithdrawalRequestAmount = "${:,.2f}".format(totalFretotalAllApprovedWithdrawalRequestMain)
    print(f' here {totalAllApprovedWithdrawalRequestAmount}')

    AllPendingWithdrawalRequest = WithdrawalRequest.objects.filter(Q(user=request.user) & Q(withdrawalRequestStatus = 'Pending')).values_list('withdrawamount', flat=True)
    if AllPendingWithdrawalRequest:
        totalAllPendingWithdrawalRequest = 0
        for i in AllPendingWithdrawalRequest:
            totalAllPendingWithdrawalRequest = totalAllPendingWithdrawalRequest + int(i)
        totalAllPendingWithdrawalRequestMain = totalAllPendingWithdrawalRequest
    else:
        totalAllPendingWithdrawalRequestMain = 0

    AllFreeWithdrawalBalance = totalAllPendingWithdrawalRequestMain + totalFretotalAllApprovedWithdrawalRequestMain
    
    # CHECK ACCOUNT BALANCE STARTS HERE
    AllDueForWithdrawalAmount = DueForWithdrawal.objects.filter(user=request.user).values_list('earnedamount', flat=True)
    totalDueWithdrawal = 0
    if AllDueForWithdrawalAmount:
        for i in AllDueForWithdrawalAmount:
            totalDueWithdrawal = totalDueWithdrawal + int(float(i))


    UserAccountBalance = totalDueWithdrawal - AllFreeWithdrawalBalance
    UserAccountBalanceMain = "${:,.2f}".format(UserAccountBalance)
    print(f'{UserAccountBalance}')
    # CHECK ACCOUNT BALANCE ENDS HERE
    CurrentUserAccountBalance = UserAccountBalanceModel.objects.filter(user = request.user).values_list('useraccountbalance', flat=True).first()
    if CurrentUserAccountBalance:
        CurrentUserAccountBalanceMain = "${:,.2f}".format(CurrentUserAccountBalance)
    else:
        CurrentUserAccountBalanceMain = '$0'

    latestWithdrawalReq = WithdrawalRequest.objects.filter(user=request.user).values_list('withdrawamount', flat=True).first()
    latestPendingWithdrawalReqs = WithdrawalRequest.objects.filter(Q(user=request.user) & Q(withdrawalRequestStatus = 'Pending')).values_list('withdrawamount', flat=True)
    totalPendingWithdrawalReqs = 0
    if latestPendingWithdrawalReqs:
        for i in latestPendingWithdrawalReqs:
            totalPendingWithdrawalReqs = totalPendingWithdrawalReqs + int(i)
        totalPendingWithdrawalReqsMain = "${:,.2f}".format(totalPendingWithdrawalReqs)
    else:
        totalPendingWithdrawalReqsMain = 0

    AllDueForWithdrawal = DueForWithdrawal.objects.filter(user=request.user).values_list('earnedamount', flat=True)
    totalDueWithdrawal = 0
    if AllDueForWithdrawal:
        for i in AllDueForWithdrawal:
            totalDueWithdrawal = totalDueWithdrawal + int(float(i))

        totalDueWithdrawalMainPre  = totalDueWithdrawal - AllFreeWithdrawalBalance
        totalDueWithdrawalMain = "${:,.2f}".format(totalDueWithdrawalMainPre)
        # print(totalDueWithdrawalMain)

    else:
        totalDueWithdrawalMain = '$0'
        totalDueWithdrawalDraft = 0
    
    ApprovedDeposites = PotentialDeposite.objects.filter(Q(user = request.user) & Q(depositestatus = 'Approved')).values_list('amount', flat=True)
    totalApprovedDeposites = 0
    if ApprovedDeposites:
        for i in ApprovedDeposites:
            totalApprovedDeposites = totalApprovedDeposites + int(float(i))
        # print(totalApprovedDeposites)
        totalApprovedDepositesMain = "${:,.2f}".format(totalApprovedDeposites)
    else:
        ApprovedDeposites = 0
        totalApprovedDepositesMain = 0

    LatestDeposites = PotentialDeposite.objects.filter(user=request.user).values_list('amount', flat=True).first()
    AllDeposites = PotentialDeposite.objects.filter(Q(user=request.user) & Q(depositestatus = 'Approved')).values_list('amount', flat=True)
    totalAllDeposites = 0
    if AllDeposites:
        for i in AllDeposites:
            totalAllDeposites = totalAllDeposites + int(float(i))
        # print(totalAllDeposites)
        totalAllDepositesMain = "${:,.2f}".format(totalAllDeposites)
    else:
        AllDeposites = 0
        totalAllDepositesMain = 0
   
   
    PendingDeposites = PotentialDeposite.objects.filter(Q(user=request.user) & Q(depositestatus = 'Pending')).values_list('amount', flat=True)
    totalPendingDeposites = 0
    if PendingDeposites:
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
     'totalAllDepositesMain':totalAllDepositesMain, 'totalDueWithdrawalMain':totalDueWithdrawalMain, 'LatestDeposites':LatestDeposites, 'ApprovedDeposites': ApprovedDeposites, 'totalAllApprovedWithdrawalRequestAmount':totalAllApprovedWithdrawalRequestAmount,
     'latestWithdrawalReq':latestWithdrawalReq, 'totalPendingWithdrawalReqsMain' : totalPendingWithdrawalReqsMain, 'UserAccountBalance':UserAccountBalance, 'UserAccountBalanceMain':UserAccountBalanceMain,
     'CurrentUserAccountBalanceMain':CurrentUserAccountBalanceMain}
    return render(request, 'app/dashboard.html', context)


def Nav(request):    
    ApprovedDeposites = PotentialDeposite.objects.filter(Q(user = request.user) & Q(depositestatus = 'Approved')).values_list('amount', flat=True)
    totalApprovedDeposites = 0
    if ApprovedDeposites:
        for i in ApprovedDeposites:
            totalApprovedDeposites = totalApprovedDeposites + int(float(i))
        # print(totalApprovedDeposites)
        totalApprovedDepositesMain = "${:,.2f}".format(totalApprovedDeposites)
    else:
        ApprovedDeposites = 0
        totalApprovedDepositesMain = 0
    
    # CHECK ACCOUNT BALANCE STARTS HERE

    AllApprovedWithdrawalRequest = WithdrawalRequest.objects.filter(Q(user=request.user) & Q(withdrawalRequestStatus = 'Approved')).values_list('withdrawamount', flat=True)
    if AllApprovedWithdrawalRequest:
        totalAllApprovedWithdrawalRequest = 0
        for i in AllApprovedWithdrawalRequest:
            totalAllApprovedWithdrawalRequest = totalAllApprovedWithdrawalRequest + int(i)
        totalFretotalAllApprovedWithdrawalRequestMain = totalAllApprovedWithdrawalRequest
    else:
        totalFretotalAllApprovedWithdrawalRequestMain = 0
    
    totalAllApprovedWithdrawalRequestAmount = "${:,.2f}".format(totalFretotalAllApprovedWithdrawalRequestMain)
    print(f' here {totalAllApprovedWithdrawalRequestAmount}')
    # CHECK ACCOUNT BALANCE ENDS HERE
    CurrentUserAccountBalance = UserAccountBalanceModel.objects.filter(user = request.user).values_list('useraccountbalance', flat=True).first()
    CurrentUserAccountBalanceMain = "${:,.2f}".format(CurrentUserAccountBalance)

    AllPendingWithdrawalRequest = WithdrawalRequest.objects.filter(Q(user=request.user) & Q(withdrawalRequestStatus = 'Pending')).values_list('withdrawamount', flat=True)
    if AllPendingWithdrawalRequest:
        totalAllPendingWithdrawalRequest = 0
        for i in AllPendingWithdrawalRequest:
            totalAllPendingWithdrawalRequest = totalAllPendingWithdrawalRequest + int(i)
        totalAllPendingWithdrawalRequestMain = totalAllPendingWithdrawalRequest
    else:
        totalAllPendingWithdrawalRequestMain = 0

    AllFreeWithdrawalBalance = totalAllPendingWithdrawalRequestMain + totalFretotalAllApprovedWithdrawalRequestMain

    AllDueForWithdrawalAmount = DueForWithdrawal.objects.filter(user=request.user).values_list('earnedamount', flat=True)
    totalDueWithdrawal = 0
    if AllDueForWithdrawalAmount:
        for i in AllDueForWithdrawalAmount:
            totalDueWithdrawal = totalDueWithdrawal + int(float(i))


    UserAccountBalance = totalDueWithdrawal - AllFreeWithdrawalBalance
    UserAccountBalanceMain = "${:,.2f}".format(UserAccountBalance)
    print(f'{UserAccountBalance}')
    # CHECK ACCOUNT BALANCE ENDS HERE

    context = {'UserAccountBalance':UserAccountBalance, 'UserAccountBalanceMain':UserAccountBalanceMain, 'totalApprovedDepositesMain':totalApprovedDepositesMain,
    'CurrentUserAccountBalanceMain':CurrentUserAccountBalanceMain}
    return render(request, 'generalapp.html', context)


@login_required(login_url='UserSignUpFxn')
def Deposite(request):
    FetchAllAppPlans = AllAppPlans.objects.all()
    BronzePlan = AllAppPlans.objects.get(PlanName = 'Bronze Plan')
    BronzePlanMinValue = AllAppPlans.objects.filter(PlanName = 'Bronze Plan').values_list('minamount', flat=True)[0]
    BronzePlanMaxValue = AllAppPlans.objects.filter(PlanName = 'Bronze Plan').values_list('maxamount', flat=True)[0]
    print(type(int(BronzePlanMinValue)))
    
    SilverPlan = AllAppPlans.objects.get(PlanName = 'Silver plan')
    SilverPlanMinValue = AllAppPlans.objects.filter(PlanName = 'Silver plan').values_list('minamount', flat=True)[0]
    SilverPlanMaxValue = AllAppPlans.objects.filter(PlanName = 'Silver plan').values_list('maxamount', flat=True)[0]

    GoldPlan = AllAppPlans.objects.get(PlanName = 'Gold plan')
    GoldPlanMinValue = AllAppPlans.objects.filter(PlanName = 'Gold plan').values_list('minamount', flat=True)[0]
    GoldPlanMaxValue = AllAppPlans.objects.filter(PlanName = 'Gold plan').values_list('maxamount', flat=True)[0]
    
    DiamondPlan = AllAppPlans.objects.filter(PlanName = 'Diamond plan')
    DiamondPlanMinValue = AllAppPlans.objects.filter(PlanName = 'Diamond plan').values_list('minamount', flat=True)[0]
    DiamondPlanMaxValue = AllAppPlans.objects.filter(PlanName = 'Diamond plan').values_list('maxamount', flat=True)[0]

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
    print('neworder')
    print(neworder)
    BTCWalletID = AdminWalletIds.objects.filter(walletType = 'btc').values_list('walletID', flat = True)[0]
    BNBWalletID = AdminWalletIds.objects.filter(walletType = 'bnb').values_list('walletID', flat = True)[0]
    USDTWalletID = AdminWalletIds.objects.filter(walletType = 'usdt').values_list('walletID', flat = True)[0]
    TRONWalletID = AdminWalletIds.objects.filter(walletType = 'tron').values_list('walletID', flat = True)[0]
    if request.method == 'POST' and 'depositeconfirmed' in request.POST:
        checkDepositStatus = ConfrimedOrdersStatuses.objects.filter(depositeID = pk)
        if checkDepositStatus:
            messages.error(request, 'This deposit has already been recorded.')
            return redirect('Deposite')
            # return redirect('ConfirmDeposite', pk=pk)
        else:
            ConfrimedOrdersForm =  ConfrimedOrdersStatuses(user = request.user, depositeID = pk, depositestatus = 'Payment is made')
            ConfrimedOrdersForm.save()
            messages.success(request, 'Your deposite is currently pending and will be approved when confirmed.')
            return redirect('History')

    context = {'neworder': neworder, 'BTCWalletID':BTCWalletID, 'BNBWalletID':BNBWalletID, 'USDTWalletID':USDTWalletID, 'TRONWalletID':TRONWalletID}
    return render(request, 'app/confirmdeposite.html', context)



@login_required(login_url='UserSignUpFxn')
def ConfirmInvest(request):
    return render(request, 'app/confirminvest.html')


def Withdraw(request):
    AllDueForWithdrawal = DueForWithdrawal.objects.filter(user=request.user)
    AllWithdrawalRequest = WithdrawalRequest.objects.filter(user=request.user)
    
    # FIND ACCOUNT BALANCE STARTS BELOW 
    AllApprovedWithdrawalRequest = WithdrawalRequest.objects.filter(Q(user=request.user) & Q(withdrawalRequestStatus = 'Approved')).values_list('withdrawamount', flat=True)
    print(AllApprovedWithdrawalRequest)
    totalAllApprovedWithdrawalRequest = 0
    if AllApprovedWithdrawalRequest:
        for i in AllApprovedWithdrawalRequest:
            totalAllApprovedWithdrawalRequest = totalAllApprovedWithdrawalRequest + int(i)
        totalFretotalAllApprovedWithdrawalRequestMain = totalAllApprovedWithdrawalRequest
    else:
        totalFretotalAllApprovedWithdrawalRequestMain = 0

    AllPendingWithdrawalRequest = WithdrawalRequest.objects.filter(Q(user=request.user) & Q(withdrawalRequestStatus = 'Pending')).values_list('withdrawamount', flat=True)
    totalAllPendingWithdrawalRequest = 0
    if AllPendingWithdrawalRequest:
        for i in AllPendingWithdrawalRequest:
            totalAllPendingWithdrawalRequest = totalAllPendingWithdrawalRequest + int(i)
        totalAllPendingWithdrawalRequestMain = totalAllPendingWithdrawalRequest
    else:
        totalAllPendingWithdrawalRequestMain = 0

    AllFreeWithdrawalBalance = totalAllPendingWithdrawalRequestMain + totalFretotalAllApprovedWithdrawalRequestMain

    AllDueForWithdrawalAmount = DueForWithdrawal.objects.filter(user=request.user).values_list('earnedamount', flat=True)
    totalDueWithdrawal = 0
    if AllDueForWithdrawalAmount:
        for i in AllDueForWithdrawalAmount:
            totalDueWithdrawal = totalDueWithdrawal + int(float(i))


    UserAccountBalance = totalDueWithdrawal - AllFreeWithdrawalBalance
    # FIND ACCOUNT BALANCE ENDS ABOVE
    CurrentUserAccountBalance = UserAccountBalanceModel.objects.filter(user = request.user).values_list('useraccountbalance', flat=True).first()
    
    
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
            if int(amountEntered) > int(CurrentUserAccountBalance):
                messages.success(request, f'ERROR: You entered an amount greater than the amount in your wallet. Your account balance is ${CurrentUserAccountBalance}')
                return redirect('Withdraw')
            else:
                WithdrawalRequestForm = WithdrawalRequest(user=request.user, withdrawalID=withdrawalIDMain, withdrawamount=amountEntered, withdrawcrptocurrency=walletSelected,
                withdrawalRequestStatus='Pending', cryptowalletID=cryptowalletID)
                messages.success(request, 'Success! An admin will review your withdrawal request within the next 12 working hours.')
                WithdrawalRequestForm.save()

                

                # FIND ACCOUNT BALANCE STARTS BELOW 
                # AllApprovedWithdrawalRequest = WithdrawalRequest.objects.filter(Q(user=request.user) & Q(withdrawalRequestStatus = 'Approved')).values_list('withdrawamount', flat=True)
                # print(AllApprovedWithdrawalRequest)
                # totalAllApprovedWithdrawalRequest = 0
                # if AllApprovedWithdrawalRequest:
                #     for i in AllApprovedWithdrawalRequest:
                #         totalAllApprovedWithdrawalRequest = totalAllApprovedWithdrawalRequest + int(i)
                #     totalFretotalAllApprovedWithdrawalRequestMain = totalAllApprovedWithdrawalRequest
                # else:
                #     totalFretotalAllApprovedWithdrawalRequestMain = 0

                # AllPendingWithdrawalRequest = WithdrawalRequest.objects.filter(Q(user=request.user) & Q(withdrawalRequestStatus = 'Pending')).values_list('withdrawamount', flat=True)
                # totalAllPendingWithdrawalRequest = 0
                # if AllPendingWithdrawalRequest:
                #     for i in AllPendingWithdrawalRequest:
                #         totalAllPendingWithdrawalRequest = totalAllPendingWithdrawalRequest + int(i)
                #     totalAllPendingWithdrawalRequestMain = totalAllPendingWithdrawalRequest
                # else:
                #     totalAllPendingWithdrawalRequestMain = 0

                # AllFreeWithdrawalBalance = totalAllPendingWithdrawalRequestMain + totalFretotalAllApprovedWithdrawalRequestMain

                # AllDueForWithdrawalAmount = DueForWithdrawal.objects.filter(user=request.user).values_list('earnedamount', flat=True)
                # totalDueWithdrawal = 0
                # if AllDueForWithdrawalAmount:
                #     for i in AllDueForWithdrawalAmount:
                #         totalDueWithdrawal = totalDueWithdrawal + int(float(i))
                #     totalDueWithdrawalMain = totalAllPendingWithdrawalRequest
                # else:
                #     totalDueWithdrawalMain = 0


                # UserAccountBalance = totalDueWithdrawalMain - AllFreeWithdrawalBalance
                NewAccountBalance = CurrentUserAccountBalance - amountEntered
                if NewAccountBalance <= 0:
                    NewAccountBalanceSave = 0
                else:
                    NewAccountBalanceSave = NewAccountBalance
                # UPDATE ACCOUNT BALANCE BELOW
                NewAccountBalanceModelForm = UserAccountBalanceModel(user = request.user, useremail = request.user.email, useraccountbalance = NewAccountBalanceSave)
                NewAccountBalanceModelForm.save()
                print(f'{NewAccountBalanceSave}')
                # FIND ACCOUNT BALANCE ENDS ABOVE
                
                # CHECK ACCOUNT BALANCE ENDS HERE
                CurrentUserAccountBalance = UserAccountBalanceModel.objects.filter(user = request.user).values_list('useraccountbalance', flat=True).first()
                CurrentUserAccountBalanceMain = "${:,.2f}".format(CurrentUserAccountBalance)

                return redirect('Withdraw')
    context = {'UserAccountBalance':UserAccountBalance, 'AllDueForWithdrawal':AllDueForWithdrawal, 'AllWithdrawalRequest':AllWithdrawalRequest, 'CurrentUserAccountBalance':CurrentUserAccountBalance}
    return render(request, 'app/Withdraw.html', context)


@login_required(login_url='UserSignUpFxn')
def History(request):
    # AllOrders = ConfrimedOrdersStatuses.objects.filter(user = request.user)
    OrderDetails = PotentialDeposite.objects.filter(user = request.user)
    if request.method == 'POST':
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

            # FIND ACCOUNT BALANCE STARTS BELOW 
            AllApprovedWithdrawalRequest = WithdrawalRequest.objects.filter(Q(user=request.user) & Q(withdrawalRequestStatus = 'Approved')).values_list('withdrawamount', flat=True)
            print(AllApprovedWithdrawalRequest)
            totalAllApprovedWithdrawalRequest = 0
            if AllApprovedWithdrawalRequest:
                for i in AllApprovedWithdrawalRequest:
                    totalAllApprovedWithdrawalRequest = totalAllApprovedWithdrawalRequest + int(i)
                totalFretotalAllApprovedWithdrawalRequestMain = totalAllApprovedWithdrawalRequest
            else:
                totalFretotalAllApprovedWithdrawalRequestMain = 0

            AllPendingWithdrawalRequest = WithdrawalRequest.objects.filter(Q(user=request.user) & Q(withdrawalRequestStatus = 'Pending')).values_list('withdrawamount', flat=True)
            totalAllPendingWithdrawalRequest = 0
            if AllPendingWithdrawalRequest:
                for i in AllPendingWithdrawalRequest:
                    totalAllPendingWithdrawalRequest = totalAllPendingWithdrawalRequest + int(i)
                totalAllPendingWithdrawalRequestMain = totalAllPendingWithdrawalRequest
            else:
                totalAllPendingWithdrawalRequestMain = 0

            AllFreeWithdrawalBalance = totalAllPendingWithdrawalRequestMain + totalFretotalAllApprovedWithdrawalRequestMain

            AllDueForWithdrawalAmount = DueForWithdrawal.objects.filter(user=request.user).values_list('earnedamount', flat=True)
            totalDueWithdrawal = 0
            if AllDueForWithdrawalAmount:
                for i in AllDueForWithdrawalAmount:
                    totalDueWithdrawal = totalDueWithdrawal + int(float(i))


            UserAccountBalance = totalDueWithdrawal - AllFreeWithdrawalBalance
            # UPDATE ACCOUNT BALANCE BELOW
            UserAccountBalanceModelForm = UserAccountBalanceModel(user = request.user, useremail = request.user.email, useraccountbalance = UserAccountBalance)
            UserAccountBalanceModelForm.save()
            print(f'{UserAccountBalance}')
            # FIND ACCOUNT BALANCE ENDS ABOVE

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




def Logout(request):
    logout(request)
    messages.success(request, 'Logout Successful')
    return redirect('UserSignUpFxn')

