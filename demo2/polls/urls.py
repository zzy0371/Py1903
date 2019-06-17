from django.conf.urls import url
from . import views

app_name = "polls"
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^detail/(\d+)/$', views.DetailView.as_view(), name="detail"),
    url(r'^result/(\d+)/$',views.ReusltView.as_view(), name="result"),
    url(r'^login/$',views.LoginView.as_view(), name="login"),
    url(r'^regist/$',views.RegisteView.as_view(),name="regist"),
    url(r'^logout/$',views.LogOutView.as_view(),name="logout"),
    url(r'^active/(.*?)/$',views.ActiveView.as_view(),name="logout"),
    url(r'^checkusername/$', views.CheckUserNameView.as_view(), name="checkusername"),
    url(r'^verify/$',views.VerifyView.as_view(), name="verify"),
]