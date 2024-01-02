from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.http import urlsafe_base64_encode
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site




# Create your views here.
def UserSignUpFxn(request):
    if request.method == 'POST' and 'fullname' in request.POST:
        fullname = request.POST['fullname']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone'] 
        country = request.POST['country'] 
        password = request.POST['password'] 
        retypepassword = request.POST['retypepassword']       
        
        
        if not request.POST['fullname']:
            messages.error(request, 'Registration Failed: Enter Your Full Name')
            return redirect('UserSignUpFxn')
        
        
        if not request.POST['username']:
            messages.error(request, 'Registration Failed: Enter Your User Name')
            return redirect('UserSignUpFxn')
        
        
        if not request.POST['email']:
            messages.error(request, 'Registration Failed: Enter An Email Address')
            return redirect('UserSignUpFxn')
        
        
        if not request.POST['phone']:
            messages.error(request, 'Registration Failed: Enter Your Phone Number')
            return redirect('UserSignUpFxn')
        
        
        if not request.POST['country']:
            messages.error(request, 'Registration Failed: Select A Country')
            return redirect('UserSignUpFxn')
        
        
        if not request.POST['password']:
            messages.error(request, 'Registration Failed: No Password Entered')
            return redirect('UserSignUpFxn')
        
        
        if not request.POST['retypepassword']:
            messages.error(request, 'Registration Failed: You did not retype your password')
            return redirect('UserSignUpFxn')           


        if (password != retypepassword):
            messages.error(request, 'Password & Retype-Password Do Not Match!')
            return redirect('UserSignUpFxn')
        else:
            errorsection = 'default'


        checkFullName = UserSignUp.objects.filter(fullname=fullname)
        checkEmail = UserSignUp.objects.filter(email=email)
        dataPhoneCheck = UserSignUp.objects.filter(phone=phone)
        datausernameCheck = UserSignUp.objects.filter(username=username)
        UserData = User.objects.filter(username=username)
        UserDataEmail = User.objects.filter(email=email)
        UserDataPhone = User.objects.filter(last_name = phone)

        if checkFullName or UserData:            
            messages.error(request, 'Sorry, User Name Is Already Taken, Please Use Another User Name')
            return redirect('UserSignUpFxn')  

        if checkEmail or UserDataEmail:
            messages.error(request, 'Sorry, Email Address Is Already Taken')
            return redirect('UserSignUpFxn') 

        if dataPhoneCheck or UserDataPhone:
            messages.error(request, 'Sorry, Phone Number Is Already Taken')
            return redirect('UserSignUpFxn')

        form = UserSignUp(fullname=fullname, phone=phone, username=username, email=email,
        password=password, retypepassword=retypepassword, country=country)

        user = User.objects.create_user(password=password, username= username, email=email, first_name=fullname, last_name=phone)
        messages.success(request, 'Registration Successful')
        user = authenticate(request, username=username, password=password)
        print(user)
        print(email)
        # activateEmail(request, user, email)
        # try:
        #     activateEmail(request, user, email)
        # except:
        #     print('Registration mail was not sent successfully')
            
        form.save()
        user.save()
        return redirect('Dashboard')


        # LOGIN FUNCTION STARTS HERE

        
    if request.method == 'POST' and 'userloginemail' in request.POST:        
        next = ""
        if request.GET:  
            next = request.GET['next']

        print('login activated')
        email = request.POST['userloginemail']
        password = request.POST['passwordlogin']
        try:
            user = User.objects.get(email=email)
            if user:
                userEmail = user.email
        except:
            messages.error(request, 'We can not find an account attached to your email address, create an account to continue.')
            return redirect('UserSignUpFxn')
        
        user = authenticate(request, username=user, password=password)

        if user is not None:
            login(request, user)
            # notifyLoginEmail(request, user, email)
            if next == "":
                return redirect('Dashboard')
            else:
                return HttpResponseRedirect(next)

        else:
            # print(error)
            messages.error(request, 'Login Failed: Please Try Again!!')
            return render(request, 'useronboard/signup.html')

        # LOGIN FUNCTION ENDS HERE

    return render(request, 'useronboard/signup.html')



def UserLogin(request):
    if request.method == 'POST' and 'userloginemail' in request.POST:        
        next = ""
        if request.GET:  
            next = request.GET['next']

        print('login activated')
        email = request.POST['userloginemail']
        password = request.POST['passwordlogin']
        try:
            user = User.objects.get(email=email)
            if user:
                userEmail = user.email
        except:
            messages.error(request, 'We can not find an account attached to your email address, create an account to continue.')
            return redirect('UserSignUpFxn')
        
        user = authenticate(request, username=user, password=password)

        if user is not None:
            print('user exit')
            login(request, user)
            notifyLoginEmail(request, user, email)
            if next == "":
                return redirect('Dashboard')
            else:
                return HttpResponseRedirect(next)

        else:
            print(error)
            messages.error(request, 'Login Failed: Please Try Again!!')
            return render(request, 'useronboard/signup.html')

    context = {'errorsection':errorsection}
    return render(request, 'useronboard/signup.html')




def UserLogout(request):
    logout(request)
    messages.success(request, 'Logout Successful')
    return redirect('UserSignUpFxn')





def notifyLoginEmail(request, user, to_email):
    mail_subject = "Someone logged into your Ceness Trade account."
    recipient_list = [to_email, ]
    message = render_to_string("mailouts/account_login_email.html", {
        'user': user.email,
        # 'domain': 'http://127.0.0.1:8000/',
        'domain': 'https://app.ceness-trade.com/' if request.is_secure() else 'http://127.0.0.1:8000/',
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = send_mail(mail_subject, message, 'lucasceness@gmail.com', recipient_list)
    if email:
        print('Email sent')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly')





# SEND EMAIL AFTER REGISTRATION
def activateEmail(request, user, to_email):
    print("Welcome to Ceness Trade.")
    mail_subject = "Welcome to Ceness Trade."
    recipient_list = [to_email, ]
    message = render_to_string("mailouts/account_verification_email.html", {
        'user': user.email,
        'domain': 'https://app.ceness-trade.com/' if request.is_secure() else 'http://127.0.0.1:8000/',
        # 'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
        
    })
    email = send_mail(mail_subject, message, 'lucasceness@gmail.com', recipient_list)
    if email:
        # messages.success(request, 'A confimation email was sent to your inb')
        print('Sent a confirmation email')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly')
