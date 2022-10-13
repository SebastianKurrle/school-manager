from django.urls import path
from . import views as manager_views

urlpatterns = [
    path('', manager_views.home, name='home'),
    path('school/create/', manager_views.SchoolCreateView.as_view(), name='school-create'),
    path('school/show', manager_views.show_own_schools, name='school-show'),
    path('school/<int:pk>', manager_views.ManageSchoolView.as_view(), name='school-manage'),
    path('school/search', manager_views.search_school, name='school-search'),
    path('searched/school/', manager_views.searched_school, name='searched-school'),
    path('school/<int:pk>/class/create', manager_views.ClassCreateView.as_view(), name='class-create'),
    path('school/<int:pk>/subject/create', manager_views.SubjectCreateView.as_view(), name='subject-create')
]