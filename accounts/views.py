from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from multiprocessing import AuthenticationError
from django import forms
from django.views.generic import TemplateView, CreateView
from accounts.forms import StudentSignUpForm
from .models import Student, User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


# Create your views here.


class Front_pageView(TemplateView):

    template_name = "accounts/login.html"


class StudentRegisterView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = "accounts/student_register.html"

    def form_valid(self, form):

        user = form.save()

        return redirect("/")
