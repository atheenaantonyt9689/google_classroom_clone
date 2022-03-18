from django import forms
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from accounts.models import Student, User


class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(StudentSignUpForm, self).__init__(*args, **kwargs)

        self.fields["first_name"].widget.attrs["placeholder"] = "first_name"
        self.fields["last_name"].widget.attrs["placeholder"] = "last_name"
        self.fields["email"].widget.attrs["placeholder"] = "email"
        self.fields["phone_number"].widget.attrs["placeholder"] = "phone_number"
        self.fields["username"].widget.attrs["placeholder"] = "username"
        # self.fields["password"].widget.attrs["placeholder"] = "password"
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))

    class Meta:

        model = User
        fields = [
            "username",
            "first_name",
            "last_name",            
            "email",
            "phone_number",
        ]

    def clean_email(self):

        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).first():
            raise forms.ValidationError("Email already exists")
        return email

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.email = self.cleaned_data.get("email")

        user.save()
        student_obj = Student.objects.create(user=user)
        student_obj.phone_number = self.cleaned_data.get("phone_number")
        student_obj.save()
        return user
