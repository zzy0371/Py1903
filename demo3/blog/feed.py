"""
使用django自带模块将最新更新包装成XML
"""
from django.contrib.syndication.views import Feed
from .models import Article
class ArticleFeed(Feed):
    title = "ZZY的个人博客"
    description = "给大家介绍一些Django开发知识点"
    link = "/"

    def items(self):
        return Article.objects.all().order_by("-create_time")[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body[:30]

    def item_link(self, item):
        return "/single/%s"%(item.id,)