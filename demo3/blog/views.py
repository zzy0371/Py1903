from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.views.generic import View,ListView,DetailView
from .models import *
from comments.forms import CommentForm
from comments.models import Comment
from django.http import HttpResponse
from django.core.paginator import Paginator
import markdown
from django.core.mail import send_mail,EmailMultiAlternatives
from demo3 import settings
from django.views.decorators.cache import cache_page
# Create your views here.

def getpageinfo(request, queryset, perpage, path):
    """
    返回页面
    :param request:请求
    :param queryset:分页对象列表
    :param perpage:每页显示个数
    :param path:路径
    :return:
    """
    paginator = Paginator(queryset, perpage)
    pagenum = request.GET.get("page")
    pagenum = 1 if pagenum == None else pagenum
    page = paginator.get_page(pagenum)
    page.path = path
    return page

class IndexView(View):
    """
    文章列表页视图类
    """

    @cache_page(60*5)
    def get(self,req):
        """
        重写get请求
        :param req:
        :return:
        """
        articles = Article.objects.all()
        page = getpageinfo(req,articles,2,"/")
        return render(req,"blog/index.html",{"page":page})

# @cache_page(60*5)
def index(req):
    articles = Article.objects.all()
    page = getpageinfo(req, articles, 2, "/")
    return render(req, "blog/index.html", {"page": page})

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

        # 1获取markdown实例
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        # 2 使用markdown实例渲染指定字段
        article.body = md.convert(article.body)
        # 3将md的目录对象赋予 article
        article.toc = md.toc

        # 向详情页面传递一个 评论表单
        cf = CommentForm()
        # latestarticles = Article.objects.all().order_by("-create_time")[:3]
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
            return redirect(reverse("blog:single", args=(id,)))

class ArchieveView(View):
    """
    归档视图
    """
    def get(self,req,year,month):
        articles = Article.objects.filter(create_time__year = year, create_time__month = month )
        page = getpageinfo(req, articles, 1, "/archives/%s/%s/"%(year,month))
        return render(req, "blog/index.html", {"page":page})

class CategoryView(View):
    """
    分类视图
    """
    def get(self,req,id):
        articles = get_object_or_404(Category, pk =id).article_set.all()
        page = getpageinfo(req, articles, 1, "/category/%s/"%(id,))
        return render(req, "blog/index.html", locals())

class TagView(View):
    """
    标签云视图
    """
    def get(self,req,id):
        tag = get_object_or_404(Tag,pk = id)
        articles = tag.article_set.all()
        page = getpageinfo(req, articles, 1, "/tags/%s/"%(id,))
        return render(req, "blog/index.html", locals())

class ContactView(View):
    def get(self,req):
        return render(req,"blog/contact.html")

    def post(self,req):
        email = req.POST.get("email")
        message = req.POST.get("message")

        info = MessageInfo()
        info.email = email
        info.info = message
        info.save()

        return HttpResponse("建议成功")

class SendMailView(View):
    def get(self,req):
        "发送邮件"

        try:
            mail = EmailMultiAlternatives(subject="测试邮件html格式",body="<h1>  <a href = 'http://www.baidu.com'> 百度 </a>  </h1>", from_email=settings.DEFAULT_FROM_EMAIL,to= ["18137128152@163.com", "zhangzhaoyu@qikux.com"])
            mail.content_subtype = "html"
            mail.send()
            # send_mail("测试邮件", "  <h1>  <a href = 'http://www.baidu.com'> 百度 </a>  </h1> ", settings.DEFAULT_FROM_EMAIL, ["18137128152@163.com", "zhangzhaoyu@qikux.com"])
            return HttpResponse("发送成功")
        except:
            return HttpResponse("发送失败")
