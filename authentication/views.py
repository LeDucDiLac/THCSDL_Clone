from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.contrib import auth



class EmailValidationView(View):
    def post(self,request):
        data=json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is invalid'},status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'email is taken'},status=409)
        return JsonResponse({'email_valid':True})
        

class UsernameValidationView(View):
    def post(self,request):
        data=json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'username should only contain alphanumeric characters'},status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'username is taken'},status=409)
        return JsonResponse({'username_valid':True})
        
        
        
class RegistratrionView(View):
    def get(self,request):
        return render(request,'authentication/register.html')
    
    def post(self,request):
        # messages.success(request,'Success whatsapp')
        # messages.warning(request,'Success whatsapp')
        # messages.info(request,'Success whatsapp')
        # messages.error(request,'Success whatsapp')
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        context={
            'fieldValues':request.POST
        }
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(request,"Password has to contain at least 6 characters!")
                    return render(request,'authentication/register.html',context)
                user = User.objects.create_user(username=username,email=email)
                user.set_password(password)
                # user.is_active=False
                user.save()
                # email_body='test body'
                # email_subject='Activate your account'
                # email = EmailMessage( 
                #     email_subject,
                #     email_body,
                #     "noreply@semicolon.com",
                #     [email],
                # )
                # email.send(fail_silently=False)
                messages.success(request,"Account successfully created")
                return render(request,'authentication/register.html')
        return render(request,'authentication/register.html')


class LoginView(View):
    def get(self,request):
        return render(request,'authentication/login.html')
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        if username and password:
            user=auth.authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    auth.login(request,user)
                    messages.success(request, 'Welcome ' + user.username)
                    return redirect('expenses')
                messages.error(request,'Account is not activated')
                return render(request,'authentication/login.html')
            messages.error(request,'wrong usrename or password')
            return render(request,'authentication/login.html')
        messages.error(request,'Please fill all the fields')
        return render(request,'authentication/login.html')
    
class VerificationView(View):
    def get(self,request):
        return redirect('login')


class LogoutView(View):
    def post(self,request):
        auth.logout(request)
        messages.success(request, 'You have been logged out')
        return redirect('login')

