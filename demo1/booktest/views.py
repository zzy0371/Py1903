from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo,HeroInfo
from django.template import loader
"""
MVT 中的 V 编写视图
"""
# Create your views here.
# 视图函数由系统调用， 系统调用时给req赋值
def index(req):
    # print(req.headers["User-Agent"])
    # return HttpResponse("这里是首页")

    # 1获取模板
    temp = loader.get_template("booktest/index.html")
    # 2使用模板渲染动态数据
    res = temp.render({})
    # 3返回渲染结果
    return HttpResponse(res)

def list(req):

    books = BookInfo.objects.all()
    print(books)

    temp = loader.get_template("booktest/list.html")
    res = temp.render({})
    return HttpResponse(res)

def detail(req,id):
    book = BookInfo.objects.get(pk=id)

    temp = loader.get_template("booktest/detail.html")
    res = temp.render({})
    return HttpResponse(res)


