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
    chain = {}

    @staticmethod
    def __gen_key__(now_time, delay=15):
        deadline = now_time + datetime.timedelta(minutes=delay)
        key = hashlib.sha256(str(now_time).encode('utf-8')).hexdigest()
        return deadline, key

    @staticmethod
    def __get_key__(request):
        return request.headers['key'] if 'key' in request.headers else 'Visitor'

    def __check_pass__(self, now_time, request):
        if 'key' in request.headers:
            send_key = request.headers['key']
            return send_key in self.deadline and now_time <= self.deadline[send_key]
        else:
            return False

    def __set_key__(self, deadline, key, response, request):
        if key != 'Visitor' and key not in self.chain:
            self.deadline[key] = deadline
            self.chain[self.__get_key__(request)] = key
        response['key'] = key

    def __check_key__(self, request, response, keep=True, put=False):
        now_time = datetime.datetime.now()
        if put or (keep and self.__check_pass__(now_time, request)):
            key = self.__get_key__(request)
            if key in self.chain:
                key = self.chain[key]
                deadline = self.deadline[key]
            else:
                deadline, key = self.__gen_key__(now_time)
            self.__set_key__(deadline, key, response, request)
        else:
            if self.deadline:
                self.deadline.clear()
            if self.chain:
                self.chain.clear()
            self.__set_key__(now_time, 'Visitor', response, request)

    def check_pass(self, request):
        now_time = datetime.datetime.now()
        return self.__check_pass__(now_time, request)

    def get_response(self, request, response, keep=True, put=False):
        self.__check_key__(request, response, keep, put)
        response['Access-Control-Expose-Headers'] = "key,set-cookie"
        return response


class AdminOP:
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
        try:
            password = make_password(password)
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

    @staticmethod
    def delete_admin(username):
        try:
            user = Admin.objects.get(name=username)
            user.delete()
            return True
        except Exception as e:
            print(e)


class ImageOP:
    @staticmethod
    def add_image(image, filename: str):
        try:
            image_name = str(uuid.uuid4()) + os.path.splitext(image.name)[1]
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

    @staticmethod
    def delete_images(filename: str):
        try:
            items = Image.objects.filter(filename=filename)
            for i in items:
                i.image.delete()
                i.delete()
            return True
        except Exception as e:
            print(e)
        return False

    @staticmethod
    def delete_not_in_str(filename: str, string: str):
        try:
            images = Image.objects.filter(filename=filename)
            for i in images:
                image_name = i.image_name
                if image_name not in string:
                    i.image.delete()
                    i.delete()
            return True
        except Exception as e:
            print(e)
        return False


class HeaderOP:

    @staticmethod
    def __get_dict__(item):
        ret_dict = {'title': item.title, 'image': item.image_name, 'date': item.date, 'filename': item.filename,
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

    def create_header(self):
        try:
            filename = str(uuid.uuid4()) + ".md"
            item = self.Obj(filename=filename)
            item.text_file.save(name=filename, content=ContentFile(''))
            return filename
        except Exception as e:
            print(e)
        return False

    def delete_header(self, filename: str):
        try:
            item = self.Obj.objects.get(filename=filename)
            item.image.delete()
            item.text_file.delete()
            item.delete()
            return True
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

    def get_items(self, admin: bool = False, page: int = 1):
        try:
            items = self.Obj.objects.filter() if admin else self.Obj.objects.filter(show=True)
            items = items.order_by('-date')[(page - 1) * 10:page * 10]
            return HeaderOP.__get_list__(items)
        except Exception as e:
            print(e)
        return False

    def get_hots(self, tops: int = 5):
        try:
            items = self.Obj.objects.filter(show=True).order_by('-date')[:tops]
            return HeaderOP.__get_list__(items)
        except Exception as e:
            print(e)
        return False

    def get_item(self, filename: str):
        try:
            item = self.Obj.objects.get(filename=filename)
            return HeaderOP.__get_dict__(item)
        except Exception as e:
            print(e)
        return False

    def set_header(self, filename: str, date: str, title: str, overview: str, show: bool, image):
        try:
            item = self.Obj.objects.get(filename=filename)
            item.show = show
            item.date = date
            item.overview = overview
            item.title = title
            if image:
                image_name = str(uuid.uuid4()) + os.path.splitext(image.name)[1]
                item.image.delete()
                item.image_name = image_name
                item.image = image
                item.image.name = image_name
            else:
                image_name = item.image_name
            item.save()
            return image_name
        except Exception as e:
            print(e)
        return False


class NewsOP(ImageOP, HeaderOP):
    def __init__(self):
        super(NewsOP, self).__init__(obj=News)

    def create(self):
        return super(NewsOP, self).create_header()

    def change_file(self, filename: str, content: str):
        return super(NewsOP, self).delete_not_in_str(filename, content) \
            if super(NewsOP, self).change_file(filename, content) else False

    def delete(self, filename: str):
        return super(NewsOP, self).delete_images(filename) if super(NewsOP, self).delete_header(filename) else False


class PapersOP(ImageOP, HeaderOP):
    def __init__(self):
        super(PapersOP, self).__init__(obj=Papers)

    def create(self):
        return super(PapersOP, self).create_header()

    def change_file(self, filename: str, content: str):
        return super(PapersOP, self).delete_not_in_str(filename, content) \
            if super(PapersOP, self).change_file(filename, content) else False

    def delete(self, filename: str):
        return super(PapersOP, self).delete_images(filename) if super(PapersOP, self).delete_header(filename) else False
