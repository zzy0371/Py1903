from django.conf.urls import url
from . import views
from .feed import ArticleFeed
app_name = "blog"
urlpatterns = [
    url(r'^$', views.IndexView.as_view(),name="index"),
    url(r'^single/(\d+)/$', views.SingleView.as_view(), name="single"),
    url(r'^archives/(\d+)/(\d+)/$',views.ArchieveView.as_view(),name="archives"),
    url(r'^category/(\d+)/$',views.CategoryView.as_view(),name="category"),
    url(r'^tags/(\d+)/$',views.TagView.as_view(),name="tags"),
    url(r'^rss/$',ArticleFeed(), name="rss"),
]