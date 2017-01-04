#coding= utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404

def hello(request): #参数必须是request,包含外部请求的对象
    return HttpResponse('Hello world')

def hello1(request, num):
    try:
        num = int(num)
    except ValueError:
        raise Http404()