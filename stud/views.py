from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .models import *
from .form import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(reguest):
    return render(reguest, 'index.html')


def login(reguest):
    return render(reguest, "login.html")


@login_required()
def register(reguest):
    if reguest.method == 'POST':
        print('post')
        form = stud_details(reguest.POST, reguest.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('adminpage')
        else:
            form = stud_details()
            print("fall")

    return render(reguest, "registration.html")


@login_required()
def studregister(reguest):
    if reguest.method == 'POST':
        print('post')
        form = stud_details(reguest.POST, reguest.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('studentpage')
        else:
            print("fall")
            form = stud_details()

    return render(reguest, "stud_registration.html")


def studlogin(reguest):
    if reguest.method == 'POST':
        return redirect('studentpage')
    else:
        form = CustomerUserCreationForm()
        print("fall")

    return render(reguest, "stud_login.html")


@login_required()
def adminpage(reguest):
    return render(reguest, "adminpage.html")


@login_required()
def admindashboard(reguest):
    instance = stud.objects.all()
    context = {
        'obj_list': instance
    }

    return render(reguest, "admin_dashboard.html", context)


@login_required()
def adminprofile(reguest):
    items = stud.objects.all()
    context = {
        'obj_list': items
    }

    return render(reguest, "admin_profile.html", context)


@login_required()
def studentpage(reguest):
    return render(reguest, "studentpage.html")


@login_required()
def studdashboard(reguest):
    instance = stud.objects.all()
    context = {
        'obj_list': instance
    }
    return render(reguest, "student_dashboard.html", context)


@login_required()
def studprofile(reguest):
    instance = stud.objects.all()
    context = {
        'obj_list': instance
    }

    return render(reguest, "student_profile.html", context)


def signup(reguest):
    if reguest.method == 'POST':
        print("post")
        form = CustomerUserCreationForm(reguest.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('studregister')
    else:
        print("else")
        form = CustomerUserCreationForm()

    return render(reguest, "signup.html")
