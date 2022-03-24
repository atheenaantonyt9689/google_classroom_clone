from django import views
from django.urls import path
from accounts.views import FrontPageView, LoginPageView, StudentRegisterView, TeacherRegisterView, logout_view


urlpatterns = [
    # path("", FrontPageView.as_view(), name="front_register_page"),
    path("student_register", StudentRegisterView.as_view(), name="student_register"),
    path("teacher_register", TeacherRegisterView.as_view(), name="teacher_register"),
    path("",  LoginPageView.as_view(), name="login"),
    path('logout/',logout_view, name='logout'),
]
