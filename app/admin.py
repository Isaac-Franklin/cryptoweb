from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(AllDeposits)
admin.site.register(PotentialDeposite)
admin.site.register(ReferalData)
admin.site.register(ConfrimedOrdersStatuses)

