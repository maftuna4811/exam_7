from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from users.forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Category, Features, Services, Blog, BlogType
from users.models import Comments, Problems, Advisers


class AboutView(LoginRequiredMixin, View):
    def get(self, request):
        advisers = Advisers.objects.all()
        comment = Comments.objects.all()
        context = {
            'advisers': advisers,
            'comments': comment,
        }
        return render(request, 'about.html', context)


class AdvisersView(View):
    def get(self, request):
        advisers = Advisers.objects.all()
        context = {
            'advisers': advisers
        }
        return render(request, 'team.html', context)


class ServicesView(View):
    def get(self, request):
        services = Services.objects.all()
        features = Features.objects.all()
        category = Category.objects.all()
        context = {
            'services': services,
            'category': category,
            'features': features,
        }
        return render(request, 'service.html', context)


class BlogView(View):
    def get(self, request):
        blogs = Blog.objects.all()
        blog_type = BlogType.objects.all()
        context = {
            'blogs': blogs,
            'blog_type': blog_type,
        }
        return render(request, 'blog.html', context)


class FeaturesView(View):
    def get(self, request):
        features = Features.objects.all()
        context = {
            'features': features
        }
        return render(request, 'feature.html', context)


class Error404View(View):
    def get(self, request):
        return render(request, '404.html')


class FAQView(View):
    def get(self, request):
        return render(request, 'FAQ.html')


class OfferView(View):
    def get(self, request):
        return render(request, 'offer.html')


class TeamView(View):
    def get(self, request):
        advisers = Advisers.objects.all()
        context = {
            'advisers': advisers
        }
        return render(request, 'team.html', context)




