import mailbox
from telnetlib import LOGOUT
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def login_request(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST": #if some button clicked and taken post 
        username = request.POST["username"] #take login page inputs (with in login.html side input NAMES)
        password = request.POST["password"] #take login page inputs (with in login.html side input NAMES)

        #return something if we dont have like this user return none otherwise return smthng
        user = authenticate(request, username = username, password = password) #chechk system have same username / password user

        if user is not None: #if we have matching username and password we have not none user 
            login(request, user) #send session information to the database
            return redirect("home")

        else:
            return render(request, "account/login.html",{
                "error": "username or password is wrong"
            })
    return render(request, "account/login.html")


def register_request(request):
    if request.user.is_authenticated:
        return redirect("home")
        
    if request.method == "POST":
        username = request.POST["username"] 
        email = request.POST["email"] 
        firstname = request.POST["firstname"] 
        lastname = request.POST["lastname"] 
        password = request.POST["password"] 
        repassword = request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username = username).exists():
                return render(request, "account/register.html", {"error": "This username already be taken"})
            
            else:
                if User.objects.filter(email = email).exists():
                    return render(request, "account/register.html", {"error": "This email already be taken"})

                else:
                    user = User.objects.create_user(username = username, email = email, first_name = firstname, 
                    last_name = lastname, password = password)
                    user.save()
                    return redirect("login")
            

        else:
            return render(request, "account/register.html", {"error":  "Passwords not same"})
    return render(request, "account/register.html")


def logout_request(request):
    logout(request) 
    return redirect("home")
