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



