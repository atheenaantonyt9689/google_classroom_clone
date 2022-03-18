from django import views
from django.urls import path
from accounts.views import Front_pageView


urlpatterns = [
    path('', Front_pageView.as_view() ,name ='front_register_page'),


]
