from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.views.generic import View,ListView,DetailView
from .models import *
from comments.forms import CommentForm
from comments.models import Comment
from django.http import HttpResponse
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
        # 向详情页面传递一个 评论表单
        cf = CommentForm()
        return render(req, "blog/single.html",locals())

    def post(self,req,id):
        # 通过req。POST初始化一个有数据的cf对象
        cf = CommentForm(req.POST)
        # 如果表单数据有效
        if cf.is_valid():
            # 通过cf的save方法得到模型类（Comment的实例）
            c = cf.save(commit=False)
            # 给模型类实例赋值
            c.article = get_object_or_404(Article,pk = id)
            # 保存数据库
            c.save()


        # 原始方式太麻烦
        # name = req.POST.get("name")
        # url = req.POST.get("url")
        # email = req.POST.get("email")
        # content = req.POST.get("content")
        #
        # comment = Comment()
        # comment.name = name
        # comment.url = url
        # comment.email = email
        # comment.content = content
        # comment.article = get_object_or_404(Article,pk=id)
        #
        # comment.save()
            return redirect(reverse("blog:single", args=(id,)))
