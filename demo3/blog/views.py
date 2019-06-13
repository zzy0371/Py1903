from django.shortcuts import render,get_object_or_404
from django.views.generic import View,ListView,DetailView
from .models import *
# Create your views here.

class IndexView(View):
    """
    文章列表页视图类
    """
    def get(self,req):
        """
        重写get请求
        :param req:
        :return:
        """
        articles = Article.objects.all()
        return render(req,"blog/index.html",locals())

class SingleView(View):
    """
    文章详情页视图
    """
    def get(self,req,id):
        """
        重写get请求
        :param req:
        :param id:  文章id
        :return:
        """
        article = get_object_or_404(Article, pk=id)
        return render(req, "blog/single.html",locals())
