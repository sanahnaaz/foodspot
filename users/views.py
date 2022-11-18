from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout 
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User

from users.forms import UserForm
from main.functions import generate_form_errors
from posts.models import Students


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password= request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request,user)

                return HttpResponseRedirect("/")
            
        context={
            "title" : "Login",
            "error" : True,
            "message" : "Invalid username or password"
        }
        return render(request, "users/login.html", context=context)
    else:
        context={
            "title" : "Login"
        }
        return render(request, "users/login.html",context=context)


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse("web:index"))


def create_student(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)

            user = User.objects.create_user(
                username=instance.username,
                password=instance.password,
                email=instance.email,
                first_name=instance.first_name,
                last_name=instance.last_name
            )
            
            Students.objects.create(
                first_name = instance.first_name,
                last_name = instance.last_name,
                email = instance.email,
                password = instance.password,
                user = user
            )

            # user = authenticate(request, username=instance.username, password=instance.password)
            # auth_login(request,user)

            return HttpResponseRedirect(reverse("web:index"))

        else:
            message = generate_form_errors(form)

            form = UserForm()
            context={
                "title" : "Create Student",
                "error" : True,
                "message" : message,
                "form" : form,
            }
            return render(request, "users/signup.html", context=context)

    else:
        form = UserForm()
        context = {
            "title" : "Signup",
            "form" : form,
        }
        return render(request, "users/signup.html", context=context)