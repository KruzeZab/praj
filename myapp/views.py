from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

from .models import Course, Teacher, Student

# Create your views here.
def index(request):
  courses = Course.objects.all()
  teachers = Teacher.objects.all()
  students = Student.objects.all()

  context = {
    'courses': courses,
    'teachers': teachers,
    'students': students
  }

  return render(request, 'myapp/index.html', context)
  

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('index')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('login')
  else:
    return render(request, 'myapp/login.html')

def signup(request):
  if request.method == 'POST':
    # Get form values
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if passwords match
    if password == password2:
      # Check username
      if User.objects.filter(username=username).exists():
        messages.error(request, 'That username is taken')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'That email is being used')
          return redirect('register')
        else:
          # Looks good
          user = User.objects.create_user(username=username, password=password,email=email)
          # Login after register
          auth.login(request, user)
          messages.success(request, 'You are now logged in')
          return redirect('index')
          # user.save()
          # messages.success(request, 'You are now registered and can log in')
          # return redirect('login')
    else:
      messages.error(request, 'Passwords do not match')
      return redirect('signup')
  else:
    return render(request, 'myapp/signup.html')
  

def logout(request):
  auth.logout(request)
  messages.success(request, 'You are now logged out')
  return redirect('index')


def all_students(request):
  teachers = Teacher.objects.all()

  context = {
    'teachers': teachers,
  }
  return render(request, 'myapp/students.html', context)


def all_teachers(request):
  teachers = Teacher.objects.all()

  context = {
    'teachers': teachers,
  }
  return render(request, 'myapp/teachers.html', context)


def faq(request):
  return render(request, 'myapp/faq.html')

def grade_prediction(request):
  return render(request, 'myapp/grade-predict.html')

def result(request):
  context = {}
  if request.method == 'GET':
    hours_study = request.GET['hours']

    # predict and return value as context

  return render(request, 'myapp/result.html', context)


