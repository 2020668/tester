from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from datetime import date
from booktest.models import BookInfo

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




