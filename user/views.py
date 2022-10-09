from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, TeacherRegistrationForm
from django.contrib import messages
from django.views.generic import DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import TeacherAccount
from manager.models import School

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


def user_info(request):
    return render(request, 'user/user_info.html')

class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    success_url = '/'
    template_name = 'user/user_confirm_delete.html'

    def test_func(self):
        user = self.get_object()
        return self.request.user == user

class CreateTeacherAccount(LoginRequiredMixin, CreateView):
    model = TeacherAccount
    fields = ['username', 'password']

    def form_valid(self, form):
        school = School.objects.filter(id=self.kwargs['pk']).first()
        form.instance.school = school
        return super().form_valid(form)
