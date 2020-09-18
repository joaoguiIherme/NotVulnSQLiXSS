from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post
from django.utils import timezone


def login_user(request):
    return render(request, 'login.html')

@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('/login/')


@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário e senha inválido. SQLi não funciona!')
    return redirect('/login/')


@login_required(login_url='/login/')
def create_post(request):
    text = request.POST.get('text')
    Post.objects.create(user=request.user,  text=text)
    return redirect('/')

@login_required(login_url='/login/')
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'index.html', {'posts': posts})
