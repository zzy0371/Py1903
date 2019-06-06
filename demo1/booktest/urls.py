from django.conf.urls import url
from .views import index,list,detail
app_name = "booktest"
urlpatterns = [

    url(r'^list/$',list,name="list"),
    # 通过正则分组 传递参数   通过（）传参  视图函数需要有形参
    url(r'^detail/(\d+)/$',detail,name="detail"),
    url(r'^$',index,name="index"),
]