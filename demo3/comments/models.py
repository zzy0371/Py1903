from django.db import models
from blog.models import Article
# Create your models here.
class Comment(models.Model):
    """
    评论表：与文章表存在多对一关系
    name：评论人
    create_time ：评论时间
    content：评论内容
    article：文章
    """
    name = models.CharField(max_length=30,verbose_name="名字")
    create_time = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=500,verbose_name="正文")
    email = models.EmailField(blank=True,null=True,verbose_name="邮箱")
    url = models.URLField(blank=True,null=True,verbose_name="个人主页")
    article = models.ForeignKey(Article,on_delete=models.CASCADE)

    def __str__(self):
        return self.name