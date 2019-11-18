from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from datetime import date
from booktest.models import BookInfo
from django.http import HttpResponse

# Create your views here.


def index(request):

    books = BookInfo.objects.all()
    return render(request, 'booktest/index.html', {'books': books})


def create(request):
    b = BookInfo()
    b.btitle = '流星蝴蝶剑'
    b.bpub_date = date(1990, 1, 1)
    b.save()
    # 让浏览器再次访问index,重定向
    return redirect('/index')


def delete(request, bid):
    # 删除点击的图书
    b = BookInfo.objects.get(id=bid)
    b.delete()
    return redirect('/index')


def show_arg(request, num):
    return HttpResponse(num)


# 显示登录页面
def login(request):
    return render(request, 'booktest/login.html')


# 登录校验视图
def login_check(request):
    # 提交的参数保存在request对象中
    # request.POST保存post提交的参数　QueryDict类型　　
    # 存入数据　q = QueryDict('a=1&b=2&c=3')  取值　q['a']-->1　q.get('a')没有不抛错　q.get('d',5)没有d就返回5
    # 一个key可存多个值　q = QueryDict('a=1&a=2&a=3')  默认取最后一个值,q.getlist('a')返回 ['1','2','3']
    # request.GET保存get提交的参数
    # 获取提交的参数
    username = request.POST.get('username')
    password = request.POST.get('password')
    # 进行登录校验,查询数据库
    if username == 'admin' and password == "123456":
        return redirect('/index')
    else:
        return redirect('/login')






