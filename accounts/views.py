from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid:
            username = request.POST.get("username")
            password = request.POST.get("password1")
            if User.objects.filter(username=username).first():
                messages.error(request, "This username is already taken")
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                )
                user.save()
                login(request, user)
                return redirect("/")

    else:
        form = UserCreationForm(request.POST)
    context = {"form": form}
    return render(request, "registration/signup.html", context)
