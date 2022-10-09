from django.db import models
from manager.models import School
from django.urls import reverse

class TeacherAccount(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('school-show')

    def __str__(self):
        return self.username
