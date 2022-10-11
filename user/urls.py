from django.urls import path, include
from user import views as user_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('user/info', user_views.user_info, name='user-info'),
    path('user/delete/<int:pk>', user_views.UserDeleteView.as_view(), name='user-delete'),
    path('school/<int:pk>/create/teacher/', user_views.teacher_register, name='teacher-create'),
    path('school/<int:pk>/teacher/login', user_views.teacher_login, name='teacher-login'),
    path('teacher/logout', user_views.teacher_logout, name='teacher-logout'),
    path('teacher/profile', user_views.teacher_profile, name='teacher-profile')
]