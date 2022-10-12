from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, TeacherRegistrationForm, StudentRegistrationForm
from django.contrib import messages
from django.views.generic import DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import TeacherAccount, StudentAccount
from manager.models import School
from django.core import serializers

#views

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account {username} has been created! You are now able to login')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'user/register.html', {'form' : form})

def teacher_register(request, pk):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            school = School.objects.filter(id=pk).first()
            form.instance.school = school

            if check_teacher_name_exists(form.instance.username, school):
                context = {
                    'form' : TeacherRegistrationForm()
                }
                messages.warning(request, f'The username already exists')
                return render(request, 'user/teacheraccount_form.html', context)

            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'The teacher {username} has been created!')
            return redirect('school-manage', pk=pk)
    else:
        form = TeacherRegistrationForm()
        
    return render(request, 'user/teacheraccount_form.html', {'form' : form})

def student_register(request, pk):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            school = School.objects.filter(id=pk).first()
    else:
        form = StudentRegistrationForm()
    
    return render(request, 'user/studentaccount_form.html', {'form' : form})

def user_info(request):
    return render(request, 'user/user_info.html')

def teacher_login(request, pk):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        school = School.objects.filter(id=pk).first()
        check_login = check_teacher_login(username, password, school)

        if check_login:
            messages.success(request, f'You are logged in successfuly as {username}')
            request.session['teacher_acc'] = serializers.serialize('json', TeacherAccount.objects.filter(school=school, username=username))
            return redirect('home')
        
        messages.warning(request, f'The username or the password is incorrect')


    return render(request, 'user/teacher_login.html')

def teacher_logout(request):
    request.session['teacher_acc'] = None
    return redirect('home')

def teacher_profile(request):
    is_teacher = request.session['teacher_acc'] != None
    if is_teacher == False:
        messages.warning(request, f'You are not loged in as an teacher!')
        return redirect('home')

    teacher_json = list(serializers.deserialize('json', request.session['teacher_acc']))

    context = {
        'teacher' : teacher_json[0].object,
        'is_teacher' : is_teacher
    }

    return render(request, 'user/teacher_profile.html', context)

class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    success_url = '/'
    template_name = 'user/user_confirm_delete.html'

    def test_func(self):
        user = self.get_object()
        return self.request.user == user

# extra functions

def check_teacher_name_exists(name, school):
    school_teacher = TeacherAccount.objects.filter(school=school)

    for teacher in school_teacher:
        if teacher.username == name:
            return True
    
    return False

def check_student_name_exists(name, school):
    school_students = StudentAccount.objects.filter(school=school)

    for student in school_students:
        if student.username == name:
            return True
    
    return False

def check_teacher_login(username, password, school):
    if check_teacher_name_exists(username, school):
        teacher_account = TeacherAccount.objects.filter(school=school, username=username).first()

        return teacher_account.password == password
    
    return False
