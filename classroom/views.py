from django.contrib import messages
from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from classroom.forms import (
    AssignmentCreateForm,
    AssignmentEditForm,
    ClassroomCreateForm,
    ClassroomEditForm,
)
from classroom.models import Assignment, Classrooom, FeedFile
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import AccessMixin

# class StudentRequiredMixin(AccessMixin):

#     def dispatch( self,request,*args,**kwargs):
#         if not request.user.is_student:
#             return self.handle_no_permission()
#         return super().dispatch(request,*args,**kwargs)


class TeacherRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_teacher:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


# Create your views here.


class ClassRoomListView(LoginRequiredMixin, ListView):

    model = Classrooom
    template_name = "classroom/classroom_list.html"
    login_url = "login"


class ClassRoomCreateView(LoginRequiredMixin, TeacherRequiredMixin, CreateView):

    template_name = "classroom/new_classroom_create.html"
    model = "Classroom"
    form_class = ClassroomCreateForm
    success_url = reverse_lazy("classroom_list")
    login_url = "login"

    def form_valid(self, form):

        print("form validdd")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("form invalidddd   ")
        return super().form_invalid(form)


class ClassRoomEditView(LoginRequiredMixin, TeacherRequiredMixin, UpdateView):

    template_name = "classroom/classroom_edit.html"
    model = Classrooom
    form_class = ClassroomEditForm
    success_url = reverse_lazy("classroom_list")
    login_url = "login"

    def form_valid(self, form):

        print("form validdd")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("form invalidddd   ")
        return super().form_invalid(form)


class ClassroomDeleteView(LoginRequiredMixin, TeacherRequiredMixin, DeleteView):

    model = Classrooom
    template_name = "classroom/classroom_delete.html"
    success_url = reverse_lazy("classroom_list")
    login_url = "login"


class ClassrooomDetailview(LoginRequiredMixin, DetailView):

    model = Classrooom
    template_name = "classroom/teacher_dashboard.html"
    login_url = "login"


class AssignmentCreateView(LoginRequiredMixin, TeacherRequiredMixin, CreateView):

    template_name = "classroom/assignment/assignment_create.html"
    model = Assignment
    form_class = AssignmentCreateForm
    success_url = reverse_lazy("classroom_list")
    login_url = "login"

    def form_valid(self, form):

        print("form validdd")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("form invalid  ")
        return super().form_invalid(form)


class AssignmentEditView(LoginRequiredMixin, TeacherRequiredMixin, UpdateView):

    template_name = "classroom/assignment/assignment_edit.html"
    model = Assignment
    form_class = AssignmentEditForm
    success_url = reverse_lazy("assignment_list")
    login_url = "login"

    def get_initial(self):
        initial = super().get_initial()
        assignmnet_obj = Assignment.objects.all()
        feedfile_obj = FeedFile.objects.all()
        for feed_obj in feedfile_obj:
            initial["title"] = feed_obj.title
            initial["assignment"] = feed_obj.assignment
            initial["files"] = feed_obj.files
        return initial

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        print("form invalid  ")
        return super().form_invalid(form)


class AssignmentListView(LoginRequiredMixin, ListView):

    model = Classrooom
    template_name = "classroom/assignment/assignment_list.html"
    login_url = "login"

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["classroom"] = self.get_queryset()
        context["classroom_user"] = self.request.user
        # context['assignemnt_list'] = Assignment.objects.all()
        context["assignemnt_list"] = FeedFile.objects.all()
        return context
