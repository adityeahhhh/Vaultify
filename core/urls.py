# core/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('create/', views.create_capsule, name='create'),
    path('public/', views.public_messages, name='public'),
    path('your_capsules/', views.your_capsules, name='your_capsules'),
    path('profile/', views.profile, name='profile'),
    path('public_map/', views.public_map, name='public_map'),

]
