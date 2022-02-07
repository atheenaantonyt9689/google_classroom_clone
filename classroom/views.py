from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from classroom.forms import ClassroomCreateForm
from classroom.models import Classrooom
from django.urls import reverse, reverse_lazy

# Create your views here.
class ClassRoomListView(TemplateView):

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
