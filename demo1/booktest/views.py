from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
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

    # # 1获取模板
    # temp = loader.get_template("booktest/index.html")
    # # 2使用模板渲染动态数据
    # res = temp.render({"username":"zzy"  })
    # # 3返回渲染结果
    # return HttpResponse(res)

    return render(req,"booktest/index.html",{"username":"zzy" })

def list(req):

    books = BookInfo.objects.all()
    # temp = loader.get_template("booktest/list.html")
    # res = temp.render({"books":books, "username":"zzy" })
    # return HttpResponse(res)

    return render(req,"booktest/list.html",{"books":books, "username":"zzy" })

def detail(req,id):
    book = BookInfo.objects.get(pk=id)

    # temp = loader.get_template("booktest/detail.html")
    # res = temp.render({"book":book})
    # return HttpResponse(res)
    return render(req,"booktest/detail.html",{"book":book})

def deletehero(req,id):
    hero = HeroInfo.objects.get(pk=id)
    hero.delete()

    return redirect(reverse("booktest:detail", args=(hero.book.id, ) ))
    # return HttpResponseRedirect("/detail/%s/"%(hero.book.id,))

def deletebook(req,id):
    book = BookInfo.objects.get(pk=id)
    book.delete()
    return redirect( reverse("booktest:list") )
    # return HttpResponseRedirect("/list/")

def addhero(req,id):
    book = BookInfo.objects.get(pk=id)
    # return HttpResponse("添加成功%s"%(id,))
    if req.method == "GET":
        return render(req,"booktest/addhero.html",{"book":book})
    elif req.method == "POST":
        hero = HeroInfo()
        hero.name = req.POST.get("heroname")
        hero.content = req.POST.get("herocontent")
        hero.gender = req.POST.get("sex")
        hero.book = book
        hero.save()
        return redirect( reverse("booktest:detail", args=(id,) ) )

        # return HttpResponseRedirect("/detail/%s/" % (id,))

def addbook(req):
    if req.method == "GET":
        return render(req,"booktest/addbook.html")
    elif req.method == "POST":
        book = BookInfo()
        book.title = req.POST.get("title")
        book.pub_date = req.POST.get("pub_date")
        book.save()



        return redirect(reverse("booktest:list"))

        # return HttpResponseRedirect("/list/")

        # return HttpResponse("添加成功")