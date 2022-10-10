from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import School

@login_required
def home(request):
    return render(request, 'manager/home.html')

@login_required
def show_own_schools(request):
    schools = School.objects.filter(creator=request.user)
    context = {
        'schools' : schools
    }

    return render(request, 'manager/show_schools.html', context)

def search_school(request):
    return render(request, 'manager/search_school.html')

def searched_school(request):
    if request.method == 'POST':
        searched_school = request.POST['searched_school']

        context = {
            'searched_school' : searched_school,
            'results' : School.objects.filter(school_name__startswith=searched_school).all()
        }

        return render(request, 'manager/searched_schools.html', context)
    
    return render(request, 'manager/searched_schools.html')

class SchoolCreateView(LoginRequiredMixin, CreateView):
    model = School
    fields = ['school_name']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class ManageSchoolView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = School
    template_name = 'manager/manage_school.html'

    def test_func(self):
        school = self.get_object()
        return self.request.user == school.creator
