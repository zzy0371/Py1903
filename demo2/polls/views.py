from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,JsonResponse
from django.views.generic import View
from .models import Question,Choice,MyUser
# Create your views here.
from .forms import MyUserLoginForm,MyUserRegistForm
from django.contrib.auth import authenticate,login,logout

"""
视图两种写法  第一种 视图函数  第二种叫做视图类

"""

# def index(req):
#     return render(req,"polls/index.html")

"""
在视图模块声明 视图函数  index，这个函数有系统调用
应为：我们将路由与视图函数绑定了
当我们输入的网址和某一个路由匹配成功，就会调用该路由绑定的视图函数
在调用该函数时 会将请求（req）以及参数列表传给给该函数
"""


def checklogin(fun):
    def check(self,req,*args):
        # if req.COOKIES.get("username"):
        #     return fun(self,req,*args)

        # if req.session.get("username"):
        #     return fun(self,req,*args)

        if req.user and req.user.is_authenticated:
            return fun(self, req, *args)
        else:
            return redirect(reverse("polls:login"))
    return check



class IndexView(View):
    """
    通过重写父类View实现完成通用视图类的功能
    重写get方法代表重写get请求
    """
    @checklogin
    def get(self,req):
        print("----")
        print(req)
        questions = Question.objects.all()
        info = " <h1> <a href='www.baidu.com'> 百度 </a> </h1>"
        info2 = " <h1> <a href='www.baidu.com'> 百度 </a> </h1>  "
        info3 = """
        <script>
            console.log("+++++")
        </script>
        """
        """
        django自带转义
        使用safe 或者 autoescape off 关闭自动转义
        浏览器可以解析
        """


        return render(req, "polls/index.html", locals())

class DetailView(View):
    @checklogin
    def get(self,req,id):
        question = Question.objects.get(pk=id)
        return render(req, "polls/detail.html", locals())

    @checklogin
    def post(self,req,id):
        c_id = req.POST.get("info")
        choice = Choice.objects.get(pk=c_id)
        choice.vites += 1
        choice.save()
        return redirect(reverse("polls:result", args=(id, )))

class ReusltView(View):
    @checklogin
    def get(self,req,id):
        question = Question.objects.get(pk=id)
        return render(req,"polls/result.html",locals())

class LoginView(View):
    def get(self,req):
        lf = MyUserLoginForm()
        rf = MyUserRegistForm()
        return render(req,"polls/login_regist.html", locals())

    def post(self,req):
        username = req.POST.get("username")
        password = req.POST.get("password")

        # MyUser.objects.get(username = username,password = password)
        # 使用django自带授权系统  如果授权成功返回user
        user = authenticate(req, username = username, password = password)
        if user:
            # 在客户端存储cookie
            login(req,user)
            return redirect(reverse("polls:index"))
        else:
            lf = MyUserLoginForm()
            rf = MyUserRegistForm()
            errormessage = "登录失败"
            return render(req, "polls/login_regist.html", locals())



class RegisteView(View):
    def get(self,req):
        pass
    def post(self,req):
        # rf = MyUserRegistForm(req.POST)
        # rf.save()

        try:
            username = req.POST.get("username")
            password = req.POST.get("password")
            email = req.POST.get("email")

            user = MyUser.objects.create_user(username=username, email=email, password=password)
            if user:
                return redirect(reverse("polls:login"))

        except:
            lf = MyUserLoginForm()
            rf = MyUserRegistForm()
            errormessage ="注册失败"
            return render(req, "polls/login_regist.html", locals())


class LogOutView(View):
    def get(self,req):
        logout(req)
        return redirect(reverse("polls:login"))

