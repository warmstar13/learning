from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = 'account'

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('leaderboard/<int:page>', views.leaderboard, name='leaderboard'),
]
