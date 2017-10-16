# coding:utf-8
from django.db import models
# Create your models here.


# 创建一个模型
class UserInfo(models.Model):
    uname=models.CharField(max_length=20)
    upwd=models.CharField(max_length=40)
    uemail=models.CharField(max_length=30)
    urecieve=models.CharField(max_length=20, default="")
    uaddress=models.CharField(max_length=100, default="")
    upostcode=models.CharField(max_length=10, default="")