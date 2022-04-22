from unittest import TestCase
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from accounts.models import Student

from classroom.models import Assignment, Classrooom, FeedFile


class ClassroomCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClassroomCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Create"))
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
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Update"))

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


class AssignmentCreateForm(forms.ModelForm):

    title = forms.CharField(max_length=100, required=False)
    files = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}), required=False
    )
    assignment = forms.ModelChoiceField(
        queryset=Assignment.objects.all(), required=False
    )

    def __init__(self, *args, **kwargs):
        super(AssignmentCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Create"))
        self.fields["topic"].widget.attrs["placeholder"] = "Topic"
        self.fields["instructions"].widget.attrs["placeholder"] = "Instructions"
        self.fields["classroom"].queryset = Classrooom.objects.all()
        self.fields["student"].queryset = Student.objects.all()
        self.fields["assignment"].queryset = Assignment.objects.all()
        self.fields["points"].widget.attrs["placeholder"] = "Points"
        self.fields["title"].widget.attrs["placeholder"] = "Title"

    class Meta:
        model = Assignment
        fields = [
            "files",
            "title",
            "instructions",
            "classroom",
            "student",
            "points",
            "topic",
            "due_date",
        ]

    def save(self, commit=True):
        instance = super().save(False)
        # print("first instance ",instance)
        if commit:
            instance.save()
            title = self.cleaned_data["title"]
            file = self.cleaned_data["files"]
            assignment = self.cleaned_data["assignment"]
        feedfile_obj = FeedFile.objects.create(
            files=file, assignment=assignment, title=title
        )
        # print("objectsss  ",feedfile_obj)
        feedfile_obj.save()
        return instance


class AssignmentEditForm(forms.ModelForm):

    title = forms.CharField(max_length=100, required=False)
    files = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}), required=False
    )
    assignment = forms.ModelChoiceField(
        queryset=Assignment.objects.all(), required=False
    )

    def __init__(self, *args, **kwargs):
        super(AssignmentEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Update"))
        self.fields["topic"].widget.attrs["placeholder"] = "Topic"
        self.fields["instructions"].widget.attrs["placeholder"] = "Instructions"
        self.fields["classroom"].queryset = Classrooom.objects.all()
        self.fields["student"].queryset = Student.objects.all()
        self.fields["assignment"].queryset = Assignment.objects.all()
        self.fields["points"].widget.attrs["placeholder"] = "Points"
        self.fields["title"].widget.attrs["placeholder"] = "Title"

    class Meta:
        model = Assignment
        fields = [
            "files",
            "title",
            "instructions",
            "classroom",
            "student",
            "points",
            "topic",
            "due_date",
            "assignment",
        ]

    def save(self, commit=True):
        instance = super().save(False)
        if commit:
            instance.save()
            title = self.cleaned_data["title"]
            files = self.cleaned_data["files"]
            assignment = self.cleaned_data["assignment"]

            objj, created = FeedFile.objects.update_or_create(
                assignment=assignment, defaults={"title": title, "files": files}
            )
            # print("objj, created ",objj, created)
            objj.save()

        return instance
