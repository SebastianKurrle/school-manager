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
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.class_name
    
    def get_absolute_url(self):
        return reverse('school-show')

class Subject(models.Model):
    name = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Lesson(models.Model):
    day = models.IntegerField(default=1)
    timefrom = models.TimeField()
    timeto = models.TimeField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    s_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey('user.TeacherAccount', on_delete=models.CASCADE)

    def __str__(self):
        return self.s_class.class_name + ' ' + self.subject.name
