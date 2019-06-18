from django.conf.urls import url
from . import views
from .feed import ArticleFeed
from haystack.views import SearchView
app_name = "blog"
urlpatterns = [
    # url(r'^$', views.IndexView.as_view(),name="index"),
    url(r'^$', views.index,name="index"),
    url(r'^single/(\d+)/$', views.SingleView.as_view(), name="single"),
    url(r'^archives/(\d+)/(\d+)/$',views.ArchieveView.as_view(),name="archives"),
    url(r'^category/(\d+)/$',views.CategoryView.as_view(),name="category"),
    url(r'^tags/(\d+)/$',views.TagView.as_view(),name="tags"),
    url(r'^contact/$',views.ContactView.as_view(),name="contact"),
    url(r'^rss/$',ArticleFeed(), name="rss"),

    url(r'sendmail',views.SendMailView.as_view(),name="sendmail"),
    url(r'^search/$',SearchView(),name="search")
]