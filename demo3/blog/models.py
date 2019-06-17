from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.
class Tag(models.Model):
    """
    标签表： 与文章表存在多对多
    title： 标签标题
    """
    title = models.CharField(max_length=20,)

    def __str__(self):
        return self.title

class Category(models.Model):
    """
    分类表：与文章表存在一对多
    title: 分类标题
    """
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Article(models.Model):
    """
    文章表： 与标签表多对多  与分类表多对一   与用户表多对一
    title:文章标题
    body：文章正文
    category：文章分类
    create_time：创建时间
    update_time：更新时间
    author：作者 使用DJango自带用户表
    views：阅读数
    """
    title = models.CharField(max_length=30)
    body = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Ads(models.Model):
    """
    轮播图模型类
    pic  字段为图片类型 upload_to 图片上传位置，数据中存储图片路径
    """
    pic = models.ImageField(upload_to="ads")
    desc = models.CharField(max_length=20)
    url = models.CharField(max_length=20)

    def __str__(self):
        return self.desc


class MessageInfo(models.Model):
    """
    联系我们页面内容
    """
    email = models.EmailField()
    # TextField 不具备格式  使用富文本替换
    # info = models.TextField()
    info = HTMLField()

    def __str__(self):
        return self.email
