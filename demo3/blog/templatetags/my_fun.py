"""
扩展自定义标签


"""
from ..models import Article,Category,Tag,Ads
from django.template import Library

register = Library()

@register.simple_tag
def  getlatestarticles(num=3):
    """
    得到最新的文章
    :return:
    """
    return Article.objects.all().order_by("-create_time")[:num]


@register.simple_tag
def getarchives():
    # dates 第一个参数为处理的字段  第二个参数为去重的字段
    return Article.objects.dates("create_time","month")

@register.simple_tag
def getcategorys():
    return Category.objects.all()

@register.simple_tag
def gettags():
    return Tag.objects.all()

@register.simple_tag
def getads():
    return Ads.objects.all()
