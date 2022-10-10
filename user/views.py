from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, TeacherRegistrationForm
from django.contrib import messages
from django.views.generic import DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import TeacherAccount
from manager.models import School

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

            if check_teacher_name_exitst(form.instance.username, school):
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

def user_info(request):
    return render(request, 'user/user_info.html')

class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    success_url = '/'
    template_name = 'user/user_confirm_delete.html'

    def test_func(self):
        user = self.get_object()
        return self.request.user == user

# extra functions

def check_teacher_name_exitst(name, school):
    school_teacher = TeacherAccount.objects.filter(school=school)

    for teacher in school_teacher:
        if teacher.username == name:
            return True
    
    return False
