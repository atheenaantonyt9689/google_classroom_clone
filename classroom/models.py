import datetime
from django.db import models
from accounts.models import Student
from django.utils import timezone

# Create your models here.
class Classrooom(models.Model):

    classname = models.CharField(max_length=30)
    section = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    room = models.CharField(max_length=30)
    teacher = models.CharField(max_length=50)
    class_code = models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(upload_to="classroom_gallery/", null=True, blank=True)

    def __str__(self):
        return self.classname

    @property
    def get_assignment_count(self):
        return FeedFile.objects.count()


class Assignment(models.Model):
    classroom = models.ForeignKey(Classrooom, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    instructions = models.TextField(max_length=250)
    student = models.ManyToManyField(Student)
    points = models.IntegerField(default=10)
    due_date = models.DateTimeField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.topic)

    # def save(self, *args, **kwargs):
    #     ''' On save, update timestamps '''
    #     if not self.id:
    #         self.created = timezone.now()
    #     # self.modified = timezone.now()
    #     return super(Assignment, self).save(*args, **kwargs)


class FeedFile(models.Model):
    files = models.FileField(upload_to="assignment_files/", null=True, blank=True)
    assignment = models.ForeignKey(
        Assignment, on_delete=models.CASCADE, null=True, default=None
    )

    def __str__(self):
        return "Assignment:{} - File:{}".format(self.assignment, self.id)
