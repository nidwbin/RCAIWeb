from django.db import models

# Create your models here.
from django.db import models


class Users(models.Model):
    """
    用户
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    password = models.CharField(max_length=30, null=True, blank=True, verbose_name="密码")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    gender = models.CharField(max_length=6, choices=(("male", "男"), ("female", "女")), default="female", verbose_name="性别")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name


class News(models.Model):

    title = models.CharField(max_length=30, null=True, blank=True, verbose_name="标题")
    content = models.CharField(max_length=500, null=True, blank=True, verbose_name="内容")
    img = models.ImageField(upload_to='img')
    date = models.DateTimeField(auto_now=True)


class Teachers(models.Model):

    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    introduction = models.CharField(max_length=500, null=True, blank=True, verbose_name="简介")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    gender = models.CharField(max_length=6, choices=(("male", "男"), ("female", "女")), default="female", verbose_name="性别")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")