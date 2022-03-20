from pyexpat import model
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView,DeleteView,DetailView
from classroom.forms import ClassroomCreateForm, ClassroomEditForm
from classroom.models import Classrooom
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class ClassRoomListView(LoginRequiredMixin,ListView):

    model = Classrooom
    template_name = "classroom/classroom_list.html"
    login_url = 'login'


class ClassRoomCreateView(LoginRequiredMixin,CreateView):

    template_name = "classroom/new_classroom_create.html"
    model = "Classroom"
    form_class = ClassroomCreateForm
    success_url = reverse_lazy("classroom_list")
    login_url = 'login'

    def form_valid(self, form):

        print("form validdd")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("form invalidddd   ")
        return super().form_invalid(form)


class ClassRoomEditView(LoginRequiredMixin,UpdateView):

    template_name = "classroom/classroom_edit.html"
    model = Classrooom
    form_class = ClassroomEditForm
    success_url = reverse_lazy("classroom_list")
    login_url = 'login'

    def form_valid(self, form):

        print("form validdd")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("form invalidddd   ")
        return super().form_invalid(form)


class ClassroomDeleteView(LoginRequiredMixin,DeleteView):

    model = Classrooom
    template_name = 'classroom/classroom_delete.html'
    success_url = reverse_lazy('classroom_list')
    login_url = 'login'


class ClassrooomDetailview(LoginRequiredMixin,DetailView):

    model = Classrooom
    template_name = 'classroom/teacher_dashboard.html'
    login_url = 'login'




