from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.views.generic import View
from .models import Question,Choice
# Create your views here.

"""
视图两种写法  第一种 视图函数  第二种叫做视图类

"""

# def index(req):
#     return render(req,"polls/index.html")

class IndexView(View):
    """
    通过重写父类View实现完成通用视图类的功能
    重写get方法代表重写get请求
    """
    def get(self,req):
        questions = Question.objects.all()
        return render(req,"polls/index.html",locals())

class DetailView(View):
    def get(self,req,id):
        question = Question.objects.get(pk=id)
        return render(req,"polls/detail.html",locals())

    def post(self,req,id):
        c_id = req.POST.get("info")
        choice = Choice.objects.get(pk=c_id)
        choice.vites += 1
        choice.save()
        return redirect(reverse("polls:result", args=(id, )))

class ReusltView(View):
    def get(self,req,id):
        question = Question.objects.get(pk=id)
        return render(req,"polls/result.html",locals())


