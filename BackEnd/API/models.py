from django.db import models

# Create your models here.
from django.db import models


class Admin(models.Model):
    name = models.CharField(max_length=50, verbose_name="用户名")
    password = models.CharField(max_length=20, verbose_name="密码")


class Header(models.Model):
    title = models.CharField(max_length=50, verbose_name="标题", default="")
    overview = models.CharField(max_length=100, verbose_name="简述", default="")
    filename = models.CharField(max_length=50, null=True, blank=True, verbose_name="文件名")
    image = models.ImageField(upload_to='images/header', default='')  # 封面图片
    image_name = models.CharField(max_length=50, verbose_name="图片名", default='')
    date = models.CharField(max_length=50, verbose_name="日期", default='XXXX-XX-XX')  # 日期
    show = models.BooleanField(blank=True, default=False)

    class Meta:
        abstract = True


class News(Header):
    text_file = models.FileField(upload_to='markdown/news')  # 文件


class Papers(models.Model):
    name = models.CharField(max_length=100, verbose_name="内容")
    link = models.CharField(max_length=50, verbose_name="链接")


class Image(models.Model):
    filename = models.CharField(max_length=50, verbose_name="文件名")
    image_name = models.CharField(max_length=50, verbose_name="图片名")
    image = models.ImageField(upload_to='images/body')  # 图片


class Fields(models.Model):  # 研究方向
    name = models.CharField(max_length=50, verbose_name="名称")
    description = models.CharField(max_length=50, verbose_name="描述")
    image_name = models.CharField(max_length=50, verbose_name="图片名")
    image = models.ImageField(upload_to='images/fields')  # 图片


class Achievements(models.Model):
    name = models.CharField(max_length=50, verbose_name="名称")
    genre = models.CharField(max_length=30, verbose_name="类别")
    author = models.CharField(max_length=30, verbose_name="作者")
    pub_date = models.CharField(max_length=50, null=True, blank=True, verbose_name="出版时间")
    publisher = models.CharField(max_length=30, verbose_name="出版社")
    overview = models.TextField(verbose_name="简介")


class Project(models.Model):
    name = models.CharField(max_length=50, verbose_name="名称")
    genre = models.CharField(max_length=30, verbose_name="类别")
    source = models.CharField(max_length=50, verbose_name="来源")
    start_date = models.CharField(max_length=50, null=True, blank=True, verbose_name="开始时间")
    finish_date = models.CharField(max_length=50, null=True, blank=True, verbose_name="完成时间")
    budget = models.CharField(max_length=50, verbose_name="项目经费")
    role = models.CharField(max_length=30, verbose_name="担任角色")
    status = models.CharField(max_length=50, verbose_name="项目状态")
    description = models.CharField(max_length=50, verbose_name="描述",default='')
    image = models.ImageField(upload_to='images/projects')
    image_name = models.CharField(max_length=50, verbose_name="图片名")


class People(models.Model):
    name = models.CharField(max_length=30, verbose_name="姓名")
    homepage = models.CharField(max_length=50, null=True, blank=True, verbose_name="主页地址")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")
    image = models.ImageField(upload_to='images/people')
    image_name = models.CharField(max_length=50, verbose_name="图片名")

    class Meta:
        abstract = True


class Teacher(People):
    professional_title = models.CharField(max_length=30, verbose_name="职称")
    introduction = models.TextField(null=True, blank=True, verbose_name="基本信息")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")


class Student(People):
    degree_type = models.CharField(max_length=30, verbose_name="学位类型")
    degree = models.CharField(max_length=30, verbose_name="学位")
    overview = models.TextField(verbose_name="简介")


class BasicInformation(models.Model):
    name = models.CharField(max_length=50, verbose_name="实验室名称")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    address = models.CharField(max_length=50, verbose_name="地址")
    overview = models.TextField(verbose_name="简介")
    history = models.TextField(verbose_name="发展历史")
