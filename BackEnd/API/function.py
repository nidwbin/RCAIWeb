'''
 * @FileDescription: functions for api views
 * @Author: wenbin
 * @Date: 2021-09-25
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-28
'''
import datetime
import hashlib
import os
import uuid
import math

from django.contrib.auth.hashers import make_password, check_password
from API.models import Admin, Image, News, Papers
from django.conf import settings


class Authority:
    deadline = {}
    visitor = 'Visitor'

    @staticmethod
    def __gen_key__(now_time, delay=15):
        deadline = now_time + datetime.timedelta(minutes=delay)
        key = hashlib.sha256(str(now_time).encode('utf-8')).hexdigest()
        return deadline, key

    def __check_pass__(self, now_time, request):
        if 'key' in request.headers:
            send_key = request.headers['key']
            return send_key in self.deadline and now_time <= self.deadline[send_key]
        else:
            return False

    def __set_key__(self, deadline, key, response):
        if key != self.visitor:
            self.deadline[key] = deadline
        response['key'] = key

    def __check_key__(self, request, response, keep=True, put=False):
        now_time = datetime.datetime.now()
        if put or (keep and self.__check_pass__(now_time, request)):
            deadline, key = self.__gen_key__(now_time)
            self.__set_key__(deadline, key, response)
        else:
            if self.deadline:
                self.deadline.clear()
            self.__set_key__(now_time, self.visitor, response)

    def check_pass(self, request):
        now_time = datetime.datetime.now()
        return self.__check_pass__(now_time, request)

    def get_response(self, request, response, keep=True, put=False):
        self.__check_key__(request, response, keep, put)
        response['Access-Control-Expose-Headers'] = "key,set-cookie"
        return response


class LoginOP:
    @staticmethod
    def check_admin(username, password):
        user = Admin.objects.filter(name=username).first()
        if user:
            return check_password(password, user.password)
        else:
            return False

    @staticmethod
    def set_admin(username, password):
        password = make_password(password)
        try:
            user = Admin.objects.filter(name=username).first()
            if user:
                user.password = password
                user.save()
            else:
                Admin.objects.create(name=username, password=password)
            return True
        except Exception as e:
            print(e)
        return False


class ImageOP:
    @staticmethod
    def add_image(image, filename):
        image_name = str(uuid.uuid4()) + os.path.splitext(image.name)[1]
        try:
            i = Image(filename=filename, image_name=image_name, image=image)
            i.save()
            return image_name
        except Exception as e:
            print(e)
        return False

    @staticmethod
    def delete_image(name):
        image = Image.objects.get(image_name=name)
        try:
            image.image.delete()
            image.delete()
            return True
        except Exception as e:
            print(e)
        return False


class NewsOP(ImageOP):
    @staticmethod
    def change_file(filename, content):
        try:
            news = News.objects.get(filename = filename)
            news.text_file = content
            news.save()
            return True
        except Exception as e:
            print(e)
        return False

    @staticmethod
    def create():
        try:
            news = News(title="新建条目", date="xxxx-xx-xx", overview="点击开始新建条目", filename=str(uuid.uuid4()) + ".md")
            news.save()
            return news.filename
        except Exception as e:
            print(e)
        return False

    @staticmethod
    def count(show,pages):
        try:
            news = News.objects.filter(show=True) if show else News.objects.filter()
            len = math.ceil(len(news)/pages)
            return len
        except Exception as e:
            print(e)
        return False

    @staticmethod
    def search_news(show,page):
        try:
            news = News.objects.filter(show=True).order_by('-date')[(page-1)*10:page*10] if show else News.objects.filter()
            list = []
            dict = {}
            for i in news:
                dict['title'] = i.title
                dict['image'] = i.img
                dict['date'] = i.date
                dict['filename'] = i.filename
                dict['show'] = i.show
                dict['overview'] = i.overview
                list.append(dict)
            return list
        except Exception as e:
            print(e)
        return False

    @staticmethod
    def search_hots(num):
        try:
            news = News.objects.filter(show=True).order_by('-date')[:num]
            list = []
            dict = {}
            for i in news:
                dict['title'] = i.title
                dict['image'] = i.img
                dict['date'] = i.date
                dict['filename'] = i.filename
                dict['show'] = i.show
                dict['overview'] = i.overview
                list.append(dict)
            return list
        except Exception as e:
            print(e)
        return False

    def search_item(filename):
        try:
            news = News.objects.get(filename=filename)
            list = []
            dict = {}
            dict['title'] = news.title
            dict['image'] = news.img
            dict['date'] = news.date
            dict['filename'] = news.filename
            dict['show'] = news.show
            dict['overview'] = news.overview
            list.append(dict)
            return list
        except Exception as e:
            print(e)
        return False

class PapersOP(ImageOP):
    @staticmethod
    def change_file(filename, content):
        try:
            papers = Papers.objects.get(filename=filename)
            papers.text_file = content
            papers.save()
            return True
        except Exception as e:
            print(e)
        return False
