from django.contrib import admin

# Register your models here.
from .models import Student,schooldetails,StdPresent

admin.site.register(Student)
admin.site.register(schooldetails)
admin.site.register(StdPresent)