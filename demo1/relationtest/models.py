from django.db import models

# Create your models here.

class Account(models.Model):
    name = models.CharField(max_length=20)


class Contact(models.Model):
    addr = models.CharField(max_length=30)
    # 定义一对一关系
    acc = models.OneToOneField(Account,on_delete=models.CASCADE)


class Host(models.Model):
    name = models.CharField(max_length=20)


class Application(models.Model):
    name = models.CharField(max_length=20)
    h = models.ManyToManyField(Host)

class TempManage(models.Manager):
    "self 代表本类实例 比如Manager实例拥有first方法  "
    "通过这种方法可以给每一个模型类封装管理器"
    def getfirstobject(self, _title):
        return self.first()



class Temp(models.Model):
    title = models.CharField(max_length=20)
    addr = models.CharField(verbose_name="地址", db_column="address", max_length=30, default="dongsanjie")
    age = models.IntegerField()

    # 自定义objects管理器
    # 一旦定义管理器字段 objects失效了
    # myobjects = models.Manager()
    objects = TempManage()

    class Meta():
        db_table = "temp"
        ordering = ["title","-addr","age"]
        verbose_name = "临时表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class AreaInfo(models.Model):
    title = models.CharField(max_length=15)
    parent = models.ForeignKey("self",on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title




