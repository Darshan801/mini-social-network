from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
import re

# Create your views here.
def home(request):
    return render(request,'base.html')
    
def signup(request):
    if(request.method=='POST'):
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        # password validation
        if(
            len(password) < 8 or 
            not re.search(r"[A-Za-z]",password) or
            not re.search(r"[0-9]",password) or
            not re.search(r"[!@#$%^&*(),.?\":{}|<>]",password)
        ):
            messages.warning(request,"Password must be at least 8 characters long and contain a letter, a number, and a special character")
            return render(request,'signup.html')
        # password match check
        if password != confirm_password:
            messages.warning(request,"password don't  match")
            # return HttpResponse("password dont match")
            return render(request,'signup.html')
        try:
            if User.objects.get(username=email):
                # return HttpResponse("email already exitsts")
                messages.warning(request,"email is taken")
                return render(request,'signup.html')
        except User.DoesNotExist:
            pass
        user=User.objects.create_user(username=email , email=email , password=password)
        user.is_active=False
        user.save()
    return render(request,'signup.html')