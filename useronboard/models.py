from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserSignUp(models.Model):
    # user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=200, null=True, blank=True)
    retypepassword = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-edited_at', '-created_at']
        
    def __str__(self):
        return self.fullname




