from django.contrib import admin
from django.urls import path, include
from .views import UserLoginView, UserRegisterView, LogOutView, ContactView, MyProfileView
from .views import TestimonialView

urlpatterns = [
    path('test/', TestimonialView.as_view(), name='test'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('profile/', MyProfileView.as_view(), name='profile'),
]
