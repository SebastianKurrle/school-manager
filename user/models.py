from django.db import models
from manager.models import School, Class

class TeacherAccount(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

class StudentAccount(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
