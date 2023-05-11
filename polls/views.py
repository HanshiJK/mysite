from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from polls import models
from .models import *


# Create your views here.


def index(request):
    pass
    return render(request, 'index.html')


def tologin(request):
    return render(request, 'login.html')


def login(request):
    u = request.POST.get('user', '')
    p = request.POST.get('pwd', '')

    # 与数据库匹配
    c = User.objects.filter(name=u, password=p).count()
    if c >= 1:
        messages.error(request, "登陆成功！")
        return render(request, "index.html")
    else:
        messages.error(request, "账号密码错误！")
        return redirect('/polls')


def toregister(request):
    return render(request, "register.html")


def register(request):
    u = request.POST.get('user', '')
    p = request.POST.get('pwd', '')

    if User.objects.filter(name=u).count() == 1:
        messages.error(request, "用户名已存在！")
        return redirect('/polls/toregister')
    else:
        if u and p:
            user = User(name=u, password=p)
            user.save()
            messages.error(request, "注册成功！")
            return redirect('/polls')
        else:
            return HttpResponse("请输入正确的账号密码！")


def logout(request):
    pass
    return redirect('/index')
