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

from django.core.files.base import ContentFile
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
        try:
            user = Admin.objects.filter(name=username).first()
            return check_password(password, user.password) if user else False
        except Exception as e:
            print(e)
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
            image = Image(filename=filename, image_name=image_name, image=image)
            image.image.name = image_name
            image.save()
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


class HeaderOP:

    @staticmethod
    def __get_dict__(item):
        ret_dict = {'title': item.title, 'image': item.img_name, 'date': item.date, 'filename': item.filename,
                    'show': item.show, 'overview': item.overview}
        return ret_dict.copy()

    @staticmethod
    def __get_list__(items):
        ret_list = []
        for i in items:
            ret_list.append(HeaderOP.__get_dict__(i))
        return ret_list.copy()

    def __init__(self, obj):
        self.Obj = obj

    def change_file(self, filename: str, content: str):
        try:
            items = self.Obj.objects.get(filename=filename)
            with items.text_file.open(mode='w') as file:
                file.write(content)
            images = Image.objects.filter(filename=filename)
            for i in images:
                image_name = i.image_name
                if image_name not in content:
                    i.image.delete()
                    i.delete()
            return True
        except Exception as e:
            print(e)
        return False

    def read_file(self, filename: str):
        try:
            news = self.Obj.objects.get(filename=filename)
            with news.text_file.open(mode='r') as file:
                content = file.read()
            return content
        except Exception as e:
            print(e)
        return False

    def create(self):
        try:
            filename = str(uuid.uuid4()) + ".md"
            item = self.Obj(filename=filename)
            item.text_file.save(name=filename, content=ContentFile(''))
            return filename
        except Exception as e:
            print(e)
        return False

    def count(self, admin: bool = False, pages: int = 10):
        try:
            items = self.Obj.objects.filter() if admin else self.Obj.objects.filter(show=True)
            length = math.ceil(len(items) / pages)
            return length
        except Exception as e:
            print(e)
        return False

    def search_items(self, admin: bool = False, page: int = 1):
        try:
            items = self.Obj.objects.filter() if admin else self.Obj.objects.filter(show=True)
            items = items.order_by('-date')[(page - 1) * 10:page * 10]
            return HeaderOP.__get_list__(items)
        except Exception as e:
            print(e)
        return False

    def search_hots(self, tops: int = 5):
        try:
            items = self.Obj.objects.filter(show=True).order_by('-date')[:tops]
            return HeaderOP.__get_list__(items)
        except Exception as e:
            print(e)
        return False

    def search_item(self, filename: str):
        try:
            item = self.Obj.objects.get(filename=filename)
            return HeaderOP.__get_dict__(item)
        except Exception as e:
            print(e)
        return False


class NewsOP(ImageOP, HeaderOP):
    def __init__(self):
        super(NewsOP, self).__init__(obj=News)


class PapersOP(ImageOP, HeaderOP):
    def __init__(self):
        super(PapersOP, self).__init__(obj=Papers)
