from django.db import models

# Create your models here.
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=50, verbose_name="标题")
    overview = models.CharField(max_length=100, verbose_name="简述")
    content = models.TextField(null=True, blank=True, verbose_name="内容")
    img = models.ImageField(upload_to='img')  # 封面图片
    date = models.DateTimeField()  # 日期
    text_file = models.FileField(upload_to='news')  # 文件


class ResearchField(models.Model):
    name = models.CharField(max_length=50, verbose_name="名称")
    text_file = models.FileField(upload_to='research')  # 文件


class Achievements(models.Model):
    name = models.CharField(max_length=50, verbose_name="名称")
    genre = models.CharField(max_length=30, verbose_name="类别")
    author = models.CharField(max_length=30, verbose_name="作者")
    pub_date = models.DateField(null=True, blank=True, verbose_name="出版时间")
    finish_date = models.DateField(null=True, blank=True, verbose_name="完成时间")
    publisher = models.CharField(max_length=30, verbose_name="出版社")
    overview = models.TextField(verbose_name="简介")


class Project(models.Model):
    name = models.CharField(max_length=50, verbose_name="名称")
    genre = models.CharField(max_length=30, verbose_name="类别")
    source = models.CharField(max_length=50, verbose_name="来源")
    start_date = models.DateField(null=True, blank=True, verbose_name="开始时间")
    finish_date = models.DateField(null=True, blank=True, verbose_name="完成时间")
    budget = models.FloatField(verbose_name="项目经费")
    role = models.CharField(max_length=30, verbose_name="担任角色")
    status = models.CharField(max_length=50, verbose_name="项目状态")


class Teacher(models.Model):
    name = models.CharField(max_length=30, verbose_name="姓名")
    professional_title = models.CharField(max_length=30, verbose_name="职称")
    introduction = models.TextField(null=True, blank=True, verbose_name="基本信息")
    homepage = models.CharField(max_length=50, null=True, blank=True, verbose_name="主页地址")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")
    photo = models.ImageField(upload_to='photo')


class Student(models.Model):
    name = models.CharField(max_length=50, verbose_name="名称")
    degree = models.CharField(max_length=30, verbose_name="学位")
    overview = models.TextField(verbose_name="简介")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")
    homepage = models.CharField(max_length=50, null=True, blank=True, verbose_name="主页地址")
    photo = models.ImageField(upload_to='photo')


class BasicInformation(models.Model):
    name = models.CharField(max_length=50, verbose_name="实验室名称")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    address = models.CharField(max_length=50, verbose_name="地址")
    overview = models.TextField(verbose_name="简介")
    history = models.TextField(verbose_name="发展历史")
