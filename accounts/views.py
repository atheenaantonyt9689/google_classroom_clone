from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from django import forms
from django.views.generic import TemplateView, CreateView
from accounts.forms import LoginForm, StudentSignUpForm, TeacherSignUpForm
from .models import Student, User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.views.generic import View


# Create your views here.


class Front_pageView(TemplateView):

    template_name = "accounts/login.html"


class StudentRegisterView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = "accounts/student_register.html"

    def form_valid(self, form):

        user = form.save()
        login(self.request, user)

        return redirect("/")


class TeacherRegisterView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = "accounts/teacher_register.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("/")


class LoginPageView(View):
    template_name = "accounts/login.html"
    form_class = LoginForm


    def get(self, request):
        form = self.form_class()
        message = ""
        return render(
            request, self.template_name, context={"form": form, "message": message}
        )

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect("/")
        message = "username or password not correct!"
        return render(
            request, self.template_name, context={"form": form, "message": message}
        )

def logout_view(request):
    logout(request)
    return redirect('login')