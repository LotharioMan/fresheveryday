# coding:utf-8
from django.shortcuts import render, redirect
from models import *
from hashlib import sha1
from django.http import JsonResponse
from django.http import HttpResponseRedirect


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
    # redirect = HttpResponseRedirect('/user/login/')
    # redirect.set_cookie("uname", uname)
    return redirect('/user/login')


def register_exist(request):
    uname = request.GET.get("user_name")
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({"count":count})


def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {'title': '用户登录', 'error_name': '0', 'error_pwd': '0', 'uname': uname}
    return render(request, 'df_user/login.html', context)


def logout(request):
    request.session['user_id'] = ''
    request.session['user_name'] = ''
    redirect = HttpResponseRedirect('/user/login/')
    if redirect.get_cookie("uname") != '':
        redirect.set_cookie("uname", "", max_age=-1)
        return redirect
    context = {'title': '用户登录', 'error_name': '0', 'error_pwd': '0'}
    return render(request, 'df_user/login.html', context)


def login_handle(request):
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    urememberme = post.get('rememberme', 0)
    user = UserInfo.objects.filter(uname=uname)
    if len(user) == 1:
        s1 = sha1()
        s1.update(upwd)
        if s1.hexdigest() == user[0].upwd:
            redirect = HttpResponseRedirect('/user/info/')
            if urememberme != 0:
                redirect.set_cookie("uname", uname)
            else:
                redirect.set_cookie("uname", "", max_age=-1)
            request.session['user_id'] = user[0].id
            request.session['user_name'] = uname
            return redirect
        else:
            context = {'title':'用户登陆', 'error_name':'0' , 'error_pwd':'1', 'uname':uname}
            return render(request, 'df_user/login.html', context)
    else:
        context = {'title': '用户登陆', 'error_name': '1', 'error_pwd': '0'}
        return render(request, 'df_user/login.html', context)


def info(request):
    user_email = UserInfo.objects.get(id=request.session['user_id']).uemail
    context = {'title': '用户中心',
               'user_email': user_email,
               'user_name': request.session['user_name']
    }
    return render(request, 'df_user/user_center_info.html', context)


def order(request):
	context = {'title':'用户中心'}
	return render(request, 'df_user/user_center_order.html',context)


def site(request):
	user = UserInfo.objects.get(id=request.session['user_id'])
	# post =request.POST
	# user.urecieve = post.get('urecieve')
	# user.uaddress = post.get('uaddress')
	# user.upostcode = post.get('upostcode')
	# user.uphone = post.get('uphone')
	# user.save()
	context={'title':'用户中心','user':user}
	return render(request, 'df_user/user_center_site.html',context)


