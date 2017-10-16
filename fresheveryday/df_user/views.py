# coding:utf-8
from django.shortcuts import render, redirect
from models import *
from hashlib import sha1
# from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,'df_user/index.html')


def register(request):
    return render(request,'df_user/register.html')


def register_handle(request):
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    urepwd = post.get('cpwd')
    uemail = post.get('email')

    if uname == "" or upwd == "" or urepwd == "" or upwd !=urepwd:
        return redirect('/user/register')

    # 密码加密
    s1 = sha1()
    s1.update(upwd)
    ffupwd = s1.hexdigest()

    user = UserInfo()
    user.uname = uname
    user.upwd = ffupwd
    user.uemail = uemail
    user.save()
    return redirect('/user/login')


def login(request):
    return render(request,'df_user/login.html')


def login_handle(request):
    # post = request.POST
    # uname = post.get('user_name')
    # upwd = post.get('pwd')
    # print(uname)
    # print(upwd)
    return redirect('/index')