from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class School(models.Model):
    school_name = models.CharField(max_length=255)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.school_name
    
    def get_absolute_url(self):
        return reverse('home')

class Class(models.Model):
    class_name = models.CharField(max_length=255)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.class_name

