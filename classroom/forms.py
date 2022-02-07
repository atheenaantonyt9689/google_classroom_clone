# from curses import meta
from unittest import TestCase
from django import forms

from classroom.models import Classrooom


class ClassroomCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClassroomCreateForm, self).__init__(*args, **kwargs)

        self.fields["classname"].widget.attrs["placeholder"] = "classroom name"
        self.fields["section"].widget.attrs["placeholder"] = "Section"
        self.fields["subject"].widget.attrs["placeholder"] = "Subject"
        self.fields["room"].widget.attrs["placeholder"] = "Room"
        self.fields["teacher"].widget.attrs["placeholder"] = "Teacher"
        self.fields["class_code"].widget.attrs["placeholder"] = "class code"

    class Meta:
        model = Classrooom
        fields = "__all__"

    # def save(self,commit=True):

    #     instance = super().save(False)
    #     if commit:
    #         classname = self.cleaned_data['classname']
    #         section = self.cleaned_data['section']
    #         subject = self.cleaned_data['subject']
    #         room = self.cleaned_data['room']
    #         teacher = self.cleaned_data['teacher']
    #         class_code = self.cleaned_data['class_code']
    #     objectss = Classrooom.objects.create(classname=classname,section=section,subject=subject,room=room,teacher=teacher,class_code=class_code)
    #     objectss.save()

    # return instance


class ClassroomEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClassroomEditForm, self).__init__(*args, **kwargs)

        self.fields["classname"].widget.attrs["placeholder"] = "classroom name"
        self.fields["section"].widget.attrs["placeholder"] = "Section"
        self.fields["subject"].widget.attrs["placeholder"] = "Subject"
        self.fields["room"].widget.attrs["placeholder"] = "Room"
        self.fields["teacher"].widget.attrs["placeholder"] = "Teacher"
        self.fields["class_code"].widget.attrs["placeholder"] = "class code"

    class Meta:
        model = Classrooom
        fields = "__all__"

    # def save(self,commit=True):

    #     instance = super().save(False)
    #     if commit:
    #         classname = self.cleaned_data['classname']
    #         section = self.cleaned_data['section']
    #         subject = self.cleaned_data['subject']
    #         room = self.cleaned_data['room']
    #         teacher = self.cleaned_data['teacher']
    #         class_code = self.cleaned_data['class_code']
    #     objectss = Classrooom.objects.create(classname=classname,section=section,subject=subject,room=room,teacher=teacher,class_code=class_code)
    #     objectss.save()

    # return instance
