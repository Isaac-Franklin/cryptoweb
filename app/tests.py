# from django.test import TestCase

# # Create your tests here.

# # 

# # FIND ACCOUNT BALANCE STARTS BELOW 
#             AllApprovedWithdrawalRequest = WithdrawalRequest.objects.filter(Q(user=request.user) & Q(withdrawalRequestStatus = 'Approved')).values_list('withdrawamount', flat=True)
#             print(AllApprovedWithdrawalRequest)
#             totalAllApprovedWithdrawalRequest = 0
#             if AllApprovedWithdrawalRequest:
#                 for i in AllApprovedWithdrawalRequest:
#                     totalAllApprovedWithdrawalRequest = totalAllApprovedWithdrawalRequest + int(i)
#                 totalFretotalAllApprovedWithdrawalRequestMain = totalAllApprovedWithdrawalRequest
#             else:
#                 totalFretotalAllApprovedWithdrawalRequestMain = 0

#             AllPendingWithdrawalRequest = WithdrawalRequest.objects.filter(Q(user=request.user) & Q(withdrawalRequestStatus = 'Pending')).values_list('withdrawamount', flat=True)
#             totalAllPendingWithdrawalRequest = 0
#             if AllPendingWithdrawalRequest:
#                 for i in AllPendingWithdrawalRequest:
#                     totalAllPendingWithdrawalRequest = totalAllPendingWithdrawalRequest + int(i)
#                 totalAllPendingWithdrawalRequestMain = totalAllPendingWithdrawalRequest
#             else:
#                 totalAllPendingWithdrawalRequestMain = 0

#             AllFreeWithdrawalBalance = totalAllPendingWithdrawalRequestMain + totalFretotalAllApprovedWithdrawalRequestMain

#             AllDueForWithdrawalAmount = DueForWithdrawal.objects.filter(user=request.user).values_list('earnedamount', flat=True)
#             totalDueWithdrawal = 0
#             if AllDueForWithdrawalAmount:
#                 for i in AllDueForWithdrawalAmount:
#                     totalDueWithdrawal = totalDueWithdrawal + int(float(i))


#             UserAccountBalance = totalDueWithdrawal - AllFreeWithdrawalBalance
#             # UPDATE ACCOUNT BALANCE BELOW
#             UserAccountBalanceModelForm = UserAccountBalanceModel(user = request.user, useremail = request.user.email, useraccountbalance = UserAccountBalance)
#             print(f'{UserAccountBalance}')
#             UserAccountBalanceModelForm.save()
#             # FIND ACCOUNT BALANCE ENDS ABOVE