from django.urls import path
from .views import home, show_own_schools, SchoolCreateView, ManageSchoolView, search_school, searched_school, ClassCreateView

urlpatterns = [
    path('', home, name='home'),
    path('school/create/', SchoolCreateView.as_view(), name='school-create'),
    path('school/show', show_own_schools, name='school-show'),
    path('school/<int:pk>', ManageSchoolView.as_view(), name='school-manage'),
    path('school/search', search_school, name='school-search'),
    path('searched/school/', searched_school, name='searched-school'),
    path('school/<int:pk>/class/create', ClassCreateView.as_view(), name='class-create')
]