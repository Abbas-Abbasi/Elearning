from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from pyexpat.errors import messages
from django.contrib.auth.forms import PasswordResetForm
from .models import Course
from .forms import CommentForm
from marketing.models import Signup


def index(request):
    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
    return render(request, 'index.html')


def courses(request):
    return render(request, 'courses.html')


def english(request):
    course_list = Course.objects.filter(categories__title='English')
    context = {
        'course_list': course_list,
    }
    return render(request, 'english.html', context)


def math(request):
    course_list = Course.objects.filter(categories__title='Math')
    context = {
        'course_list': course_list,
    }
    return render(request, 'math.html', context)


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.course = course
            form.save()
            return redirect('course_detail', course_id=course_id)
    context = {
        'course': course,
        'form': form,
    }
    return render(request, 'course_detail.html', context)


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally, you can automatically log in the user after registration
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')


def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            # You can customize the password reset email logic here
            return redirect('index')
    else:
        form = PasswordResetForm()
    return render(request, 'password_reset.html', {'form': form})


def email_change(request):
    return render(request, 'email_change.html')
