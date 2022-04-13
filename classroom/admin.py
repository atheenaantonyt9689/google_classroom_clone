from django.contrib import admin

# Register your models here.
from .models import Assignment, Classrooom, FeedFile

admin.site.register(Classrooom)
admin.site.register(Assignment)
admin.site.register(FeedFile)
