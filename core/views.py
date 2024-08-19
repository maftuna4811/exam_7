from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import TemplateView
from django.views import View
from servic.models import Category, Services, BlogType, Blog, Features
from users.models import Advisers, Comments, Problems


class IndexView(View):
    def get(self, request):
        blog = Blog.objects.all()
        category = Category.objects.all()
        features = Features.objects.all()
        services = Services.objects.all()
        blog_type = BlogType.objects.all()
        advisers = Advisers.objects.all()
        comment = Comments.objects.all()
        problem = Problems.objects.all()
        search = request.GET.get('search')
        if not search:
            context = {

                'blog': blog,
                'features': features,
                'category': category,
                'services': services,
                'advisers': advisers,
                'blog_type': blog_type,
                'comment': comment,
                'problem': problem,
            }
        else:
            services = Services.objects.filter(short_name__icontains=search)
            category = Category.objects.filter(name__icontains=search)
            features = Features.objects.filter(name__icontains=search)
            blog_type = BlogType.objects.filter(name__icontains=search)
            advisers = Advisers.objects.filter(firstname__icontains=search)
            comment = Comments.objects.filter(comment_title__icontains=search)

            if not services:
                return redirect('error404')
            else:
                context = {
                    'blog': blog,
                    'features': features,
                    'category': category,
                    'services': services,
                    'advisers': advisers,
                    'blog_type': blog_type,
                    'comment': comment,
                    'problem': problem,

                }
                return render(request, 'index.html', context)
        context = {
            'blog': blog,
            'features': features,
            'category': category,
            'services': services,
            'advisers': advisers,
            'blog_type': blog_type,
            'comment': comment,
            'problem': problem,
        }
        return render(request, 'index.html', context)




