from tkinter import CASCADE
from django.db import models
from accounts.models import Student

# Create your models here.
class Classrooom(models.Model):

    classname = models.CharField(max_length=30)
    section = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    room = models.CharField(max_length=30)
    teacher = models.CharField(max_length=50)
    class_code = models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(upload_to='classroom_gallery/',null=True, blank=True)

    def __str__(self):
        return self.classname


class Assignment(models.Model):

    classroom = models.ForeignKey(Classrooom,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    instructions = models.CharField(max_length=250)
    # files = models.ManyToManyField(FeedFiles)
    student = models.ManyToManyField(Student)
    points = models.IntegerField()
    due_date =models.DateField()
    topic = models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now=True)

class FeedFiles(models.Model): 

    title = models.CharField(max_length=100)
    files = models.FileField()
    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE)



