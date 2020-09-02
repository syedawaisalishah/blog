from django.shortcuts import render,HttpResponseRedirect
from .forms import Signupform,logins

# Create your views here.

from django.contrib.auth import authenticate,login,logout

def signup(request):
    if request.method=='POST':
       fm=Signupform(request.POST)
       if fm.is_valid():
          fm.save()
          fm.Signupform()
     
    else:
        fm=Signupform()
    context={
        'forms':fm,
    }
    return render(request, 'signup.html',context)

def log(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
           fm=logins(request=request,data=request.POST)
           if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password'] 
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/')
        else:
           fm=logins()
        return render(request,'login.html',{'forms':fm})
    else:
        return HttpResponseRedirect('')        







 #login 

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("""/""")    
