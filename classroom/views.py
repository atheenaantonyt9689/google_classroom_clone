from pyexpat import model
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView,DeleteView,DetailView
from classroom.forms import ClassroomCreateForm, ClassroomEditForm
from classroom.models import Classrooom
from django.urls import reverse, reverse_lazy

# Create your views here.
class ClassRoomListView(ListView):

    model = Classrooom
    template_name = "classroom/classroom_list.html"


class ClassRoomCreateView(CreateView):

    template_name = "classroom/classroom_create.html"
    model = "Classroom"
    form_class = ClassroomCreateForm
    success_url = reverse_lazy("classroom_create")

    def form_valid(self, form):

        print("form validdd")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("form invalidddd   ")
        return super().form_invalid(form)


class ClassRoomEditView(UpdateView):

    template_name = "classroom/classroom_edit_page.html"
    model = Classrooom
    form_class = ClassroomEditForm
    success_url = reverse_lazy("classroom_list")

    def form_valid(self, form):

        print("form validdd")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("form invalidddd   ")
        return super().form_invalid(form)


class ClassroomDeleteView(DeleteView):

    model = Classrooom
    template_name = 'classroom/classroom_delete.html'
    success_url = reverse_lazy('classroom_list')


class ClassrooomDetailview(DetailView):

    model = Classrooom
    template_name = 'classroom/teacher_dashboard.html'




