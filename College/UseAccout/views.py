from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

def signup_page(request):
    return render(request, "signup.html")


# Create your views here.
def regster(request):
    if request.method == "POST":
        Email = request.POST.get('Email')
        UserName = request.POST.get('Uname')
        FirstName = request.POST.get('Fname')
        LastName =  request.POST.get('Lname')
        password1 = request.POST.get('Password1')
        password2 =  request.POST.get('Password2')

        if password1 == password2:
            if User.objects.filter(username=UserName).exists():
                messages.info(request, "Username already taken")
                #print("Username already taken")
                return render(request, "signup.html")
            elif User.objects.filter(email=Email).exists():
                #print("Email already takem")
                messages.info(request, "Email already takem")
                return render(request, "signup.html")
            else:
                user =  User.objects.create_user(username=UserName, email=Email, password=password1)
                user.save()

                print("User is created")
                return redirect("/")
        else:
            messages.info(request, "Both Password aren't similar")
            return render(request, "signup.html")

    else:
        return render(request, "signup.html")


def logout(request):
    auth.logout(request)
    return redirect("/")



def login(request):
    if request.method=="POST":
        username =  request.POST.get("Uname")
        password = request.POST.get("password")

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")

        else:
            messages.info(request, "Wrong UserName and Credentials ")
            return render(request, "login.html")
    else:
        return render(request, "login.html")
