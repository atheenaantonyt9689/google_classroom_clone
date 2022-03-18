from django import views
from django.urls import path
from accounts.views import Front_pageView,StudentRegisterView


urlpatterns = [
    path('', Front_pageView.as_view() ,name ='front_register_page'),
    path('student_register', StudentRegisterView.as_view() ,name ='student_register'),


]
