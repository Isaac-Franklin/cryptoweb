from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(AllDeposits)
admin.site.register(PotentialDeposite)
admin.site.register(ReferalData)
admin.site.register(DueForWithdrawal)
admin.site.register(WithdrawalRequest)
admin.site.register(UserAccountBalanceModel)
admin.site.register(AllAppPlans)
admin.site.register(AdminWalletIds)
admin.site.register(ConfrimedOrdersStatuses)

