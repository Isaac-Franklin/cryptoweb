from django.db import models

from django.contrib.auth.models import User

# Create your models here.

DEPOSITE_STATUS = (
    ("Pending", "Pending"),
    ("Declined", "Declined"),
    ("Approved", "Approved"),
)


REFERAL_DEPOSITE_STATUS = (
    ("Pending", "Pending"),
    ("Declined", "Declined"),
    ("Approved", "Approved"),
)


WITHDRAWAL_STATUS = (
    ("Pending", "Pending"),
    ("Declined", "Declined"),
    ("Approved", "Approved"),
)


class AllDeposits(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-edited_at', '-created_at']
        
    def __str__(self):
        return self.user



class PotentialDeposite(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    amount = models.CharField(max_length=200, null=True, blank=True)
    wallet = models.CharField(max_length=200, null=True, blank=True)
    depositeID = models.CharField(max_length=200, null=True, blank=True)
    # planID = models.CharField(max_length=200, null=True, blank=True)
    planexpirytime = models.CharField(max_length=200, null=True, blank=True)
    planSelected = models.CharField(max_length=200, null=True, blank=True)
    depositestatus = models.CharField(max_length= 300,choices = DEPOSITE_STATUS, default = 'Pending', null=True, blank = True)

    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-edited_at', '-created_at']
        
    def __str__(self):
        return self.planSelected



class ReferalData(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    refererUsername = models.CharField(max_length=200, null=True, blank=True)
    refererEmail = models.CharField(max_length=200, null=True, blank=True)
    Referalstatus = models.CharField(max_length= 300,choices = REFERAL_DEPOSITE_STATUS, default = 'Pending', null=True, blank = True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-edited_at', '-created_at']
        
    def __str__(self):
        return self.refererUsername


class ConfrimedOrdersStatuses(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    depositeID = models.CharField(max_length=200, null=True, blank=True)
    depositestatus = models.CharField(max_length= 300,choices = DEPOSITE_STATUS, default = 'Pending', null=True, blank = True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-edited_at', '-created_at']
        
    def __str__(self):
        return self.depositeID



class DueForWithdrawal(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    orderID = models.CharField(max_length=200, null=True, blank=True)
    plan = models.CharField(max_length=200, null=True, blank=True)
    orderamount = models.CharField(max_length=200, null=True, blank=True)
    earnedamount = models.CharField(max_length=200, null=True, blank=True)
    ordercrptocurrency = models.CharField(max_length=200, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-edited_at', '-created_at']
        
    def __str__(self):
        return self.orderID


class WithdrawalRequest(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    withdrawalID = models.CharField(max_length=200, null=True, blank=True)
    withdrawamount = models.CharField(max_length=200, null=True, blank=True)
    withdrawcrptocurrency = models.CharField(max_length=200, null=True, blank=True)
    cryptowalletID = models.CharField(max_length=200, null=True, blank=True)
    withdrawalRequestStatus = models.CharField(max_length= 300,choices = WITHDRAWAL_STATUS, default = 'Pending', null=True, blank = True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-edited_at', '-created_at']
        
        
    def __str__(self):
        return self.withdrawalID



class UserAccountBalanceModel(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    useremail = models.CharField(max_length=200, null=True, blank=True)
    useraccountbalance = models.IntegerField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-edited_at', '-created_at']
        
        
    def __str__(self):
        return self.useremail



class AllAppPlans(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    PlanName = models.CharField(max_length=200, null=True, blank=True)
    minamount = models.CharField(max_length=200, null=True, blank=True)
    maxamount = models.CharField(max_length=200, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-edited_at', '-created_at']
        
        
    def __str__(self):
        return self.PlanName



class AdminWalletIds(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    walletType = models.CharField(max_length=200, null=True, blank=True)
    walletID = models.CharField(max_length=200, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-edited_at', '-created_at']
        
        
    def __str__(self):
        return self.walletType





class UserAccountBalanceModel(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    useremail = models.CharField(max_length=200, null=True, blank=True)
    useraccountbalance = models.IntegerField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-edited_at', '-created_at']
        
        
    def __str__(self):
        return self.useremail


