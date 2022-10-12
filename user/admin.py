from django.contrib import admin
from .models import TeacherAccount, StudentAccount

admin.site.register(TeacherAccount)
admin.site.register(StudentAccount)
