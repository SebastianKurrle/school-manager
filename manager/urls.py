from django.urls import path
from .views import home, show_own_schools, SchoolCreateView, ManageSchoolView

urlpatterns = [
    path('', home, name='home'),
    path('school/create/', SchoolCreateView.as_view(), name='school-create'),
    path('school/show', show_own_schools, name='school-show'),
    path('school/<int:pk>', ManageSchoolView.as_view(), name='school-manage')
]