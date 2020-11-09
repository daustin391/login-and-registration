import bcrypt
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User


def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == "POST":
        errors = User.objects.validate(request.POST)
        if errors:
            for msg in errors.values():
                messages.error(request, msg)
        else:
            password = request.POST["password"]
            hashword = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            User.objects.create(
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
                email=request.POST["email"],
                password=hashword,
            )
    return redirect("/")
