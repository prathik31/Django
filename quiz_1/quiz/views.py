from django.shortcuts import *
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login')
def index(request):
    if request.user.is_authenticated:
        x = User.objects.get(username=request.user)

    PROFILE=profile.objects.all()
    
    contexts={'PROFILE':PROFILE,'x':x}
    return render(request,'index.html',contexts)

@login_required(login_url='login')
def view_profile(request, username):
    
    PROFILE=profile.objects.get(username=username)
    
    contexts={'PROFILE':PROFILE}
    return render(request,'profile.html',contexts)


def profile_edit(request,username):
    PROFILE=profile.objects.get(username=username)
    if request.method=='POST':
        PROFILE.username=request.POST['username']
        PROFILE.email=request.POST['email']
        PROFILE.fullname=request.POST['fullname']
        PROFILE.location=request.POST['location']
        PROFILE.bio=request.POST['bio']
        
        PROFILE.save()
        return redirect('/')

    contexts={'PROFILE':PROFILE,}
    return render(request,'profile_edit.html',contexts)

def delete_profile(request,username):
    PROFILE=profile.objects.get(username=username)
    User.objects.get(username=username).delete()
    PROFILE.delete()
    return redirect('/')


def view_quiz(request):
    if request.user.is_authenticated:
        x = User.objects.get(username=request.user)
    QUIZ=quiz.objects.order_by('-created_at')
    cat=categories.objects.all()

    contexts={'QUIZ':QUIZ,'cat':cat,'x':x}
    return render(request,'all-quiz.html',contexts)


def take_quiz(request, id):
    if request.user.is_authenticated:
        x = User.objects.get(username=request.user)
    
    Q=quiz.objects.filter(id=id).first()
    
    print(Q)
    if Q!=None:
        contexts={'x':x,'quiz':Q}
    else:
        return redirect('/view_quiz')
    contexts={'x':x,'quiz':Q}
    return render(request,'take_quiz.html',contexts)

def search_quiz(request,category):

    
    if category !='':
        QUIZ= quiz.objects.filter(category__name=category)
    
    else:
        QUIZ=quiz.objects.order_by('-created_at')

    cat=categories.objects.all()

    contexts={'QUIZ':QUIZ,'cat':cat}
    return render(request,'all-quiz.html',contexts)

def login(request):
    
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect (f'/view_profile/{username}',username)
        else:
            messages.info(request,'invalid-credentials')
    return render(request,'login.html')
    

def register(request):

    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        repeat_pass=request.POST['repeat_pass']

        if password== repeat_pass:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'USername already exits')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exits, try to login')
                return redirect('/register')
            else:
                user= User.objects.create_user(username=username,email=email,password=password)
                user.save()

                user_login=auth.authenticate(username=username,password=password)
                auth.login(request, user_login)
                
                new_profile=profile.objects.create(username=username,email=email)
                new_profile.save()
                return redirect('/login')
        
    return render(request,'register.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('/login')