from django.shortcuts import render , redirect
from django.contrib.auth.models import User, auth
from .models import  Destination
from .models import  Testimonial
from .models import  Gallery_pics
from django.contrib import messages
from .models import  MyForm
from .models import  Package
from .models import  Gallery








# Create your views here.

def index(request):
    dests= Destination.objects.all()
    tests=Testimonial.objects.all()     
    gallery_pics=Gallery_pics.objects.all()
    gallerys=Gallery.objects.all()

    return render(request,"index.html",{'dests':dests,'tests':tests,'gallery_pics':gallery_pics,'gallerys':gallerys}) 

def book(request):
    return render(request, 'book.html')

#added login function

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')

        else:
            messages.info(request, 'password not matching..')
            return redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = auth.authenticate(username=username, password=password)

#         if user is not None:
#             auth.login(request, user)
#             return redirect("/")
#         else:
#             messages.info(request, 'invalid credentials')
#             return redirect('login')

#     else:
#         return render(request, 'login.html')


# def register(request):

#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         email = request.POST['email']

#         if password1 == password2:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, 'Username Taken')
#                 return redirect('register')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request, 'Email Taken')
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user(
#                     username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
#                 user.save()
#                 print('user created')
#                 return redirect('login')

#         else:
#             messages.info(request, 'password not matching..')
#             return redirect('register')
#         return redirect('/')

#     else:
#         return render(request, 'register.html')


# def logout(request):
#     auth.logout(request)
#     return redirect('/')




        # adds from form to database

def add(request):
    if request.method == "POST" or None:
        form = MyForm(request.POST or None)
        if  form.is_valid():
            form.save()
            return render(request,'add.html',{'form':form})
        else:
            form = MyForm()
            return render(request, 'add.html',{'form':form})
    else:
        form = MyForm()
        return render(request, 'add.html')

def package(request):
    packages= Package.objects.all()

    return render(request, 'package.html',{'packages':packages})