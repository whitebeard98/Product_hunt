from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
def signup(request):
    if request.method=="POST":
        #Submit the form
        if request.POST["password1"]== request.POST["password2"]:
            try:
                #check if username already exists
                user=User.objects.get(username = request.POST['username'])
                return render(request,'accounts/signup.html', {'error':'error->Username already taken'})
            
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            #password doesn't match
            return render(request,'accounts/signup.html', {'error':'error-> passwords must match'})
    return render(request,('accounts/signup.html'))

def login(request):
    if request.method=="POST":
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/login.html',{'error':'error->Username or password is incorrect'})
    return render(request,('accounts/login.html'))

def logout(request):
    print('why are you loging out lah')
    if request.method=="POST":
        print("it's taking it as POST req? Nani?")
        auth.logout(request)
        return render(request,('accounts/logout.html'))