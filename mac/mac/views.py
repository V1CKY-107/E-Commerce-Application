from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
   
    return render(request, "index.html")

def handleSignUp(request):
    if request.method == "POST":
        # the post parameters
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for error input
        if len(username) > 10:
            messages.error(request, "username must be under 10 characters ")
            return redirect('home')
        if not username.isalnum():
            messages.error(request, "username must contain letters and numbers")
            return redirect('home')
        if pass1 != pass2:
            messages.error(request, "Password don't match")
            return redirect('home')



        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, " Your MyCart has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")


def handlelogin(request):

    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername,
                            password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")

    return HttpResponse("login")



def handlelogout(request):

        logout(request)
        messages.success(request, "successfully loged out")
        return redirect('home')

        return HttpResponse('handlelogout')