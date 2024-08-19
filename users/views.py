from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserLoginForm, UserRegisterForm, UserProblemForm
from .models import Problems, Comments


class ContactView(LoginRequiredMixin, View):
    def get(self, request):
        form = UserProblemForm()
        context = {'form': form}
        return render(request, 'contact.html', context)

    def post(self, request):
        first_name = request.POST['name']
        email = request.POST['email']
        problem = request.POST['subject']
        problem_t = request.POST['message']

        a = Problems.objects.create(firstname=first_name, problem_description=problem_t,
                                    problem_name=problem, email=email)
        a.save()
        return redirect('thank')


class TestimonialView(LoginRequiredMixin, View):
    def get(self, request):
        context = {'testimonial': Comments.objects.all()}

        return render(request, 'testimonial.html', context)


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        context = {'form': form}
        return render(request, 'users/login.html', context)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        data = {
            "username": username,
            "password": password
        }
        login_form = AuthenticationForm(data=data)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)

            return redirect("index")
        else:

            context = {
                "form": login_form,
            }
            return render(request, "users/login.html", context)


class UserRegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        context = {'form': form}
        return render(request, 'users/register.html', context)


    def post(self, request):
        create_form = UserRegisterForm(data=request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('login')

        else:
            context = {'form': create_form}
            return render(request, 'users/register.html', context)


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')


class MyProfileView(View):
    def get(self, request):
        user = User.objects.get(username=request.user.username)

        context = {
                'user': user,
            }
        return render(request, 'my_profile.html', context)
