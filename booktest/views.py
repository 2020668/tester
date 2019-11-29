from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from datetime import date, datetime, timedelta
from booktest.models import BookInfo
from django.http import HttpResponse, JsonResponse

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
    # 获取cookie username
    if 'username' in request.COOKIES:
        username = request.COOKIES['username']
    else:
        username = ''
    return render(request, 'booktest/login.html', {'username': username})


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
    remember = request.POST.get('remember')
    # 进行登录校验,查询数据库
    if username == 'admin' and password == "123456":
        response = redirect('/index')
        # 判断是否勾选了记住用户名
        if remember == 'on':
            # response.set_cookie('username', username, 'password', password, max_age=7*24*3600)
            response.set_cookie('username', username, max_age=7 * 24 * 3600)
        return response

    else:
        return redirect('/login')


def ajax_test(request):
    '''显示ajax页面'''
    return render(request, 'booktest/test_ajax.html')


def ajax_handle(request):
    return JsonResponse({'res': 'ajax请求发送成功'})


def login_ajax(request):
    return render(request, 'booktest/login_ajax.html')


def login_ajax_check(request):
    '''ajax登录校验'''
    # 获取用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    # 进行校验　返回json
    if username == 'admin' and password == '123456':
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': 0})


# 设置cookie  /set_cookie
def set_cookie(request):

    response = HttpResponse('设置cookie')
    # 设置一个cookie信息，字段num, 值为１
    response.set_cookie('num', 1, max_age=14 * 24 * 3600)   # 两周后过期
    # response.set_cookie('num', 1, expires=datetime.now()+timedelta(days=14))    # 两周后过期
    # 返回response给浏览器
    return response


# 获取cookie  /get_cookie
def get_cookie(request):

    num = request.COOKIES['num']
    return HttpResponse(num)



