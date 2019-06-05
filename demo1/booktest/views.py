from django.shortcuts import render
from django.http import HttpResponse
"""
MVT 中的 V 编写视图
"""
# Create your views here.

def index(req):

    return HttpResponse("这里是首页")

def list(req):
    return HttpResponse("这里是列表页")