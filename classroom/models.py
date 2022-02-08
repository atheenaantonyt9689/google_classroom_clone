from django.db import models

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
