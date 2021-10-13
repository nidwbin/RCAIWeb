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

from API.models import Admin, Image
from BackEnd.settings import MEDIA_ROOT


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


def check_admin_authority(username, password):
    user = Admin.objects.filter(name=username).first()
    if user:
        db_password = user.password
        if password == db_password:
            return True
        else:
            return False
    else:
        return False


def add_Image(img, filename):
    imagename = str(uuid.uuid4()) + os.path.splitext(img.name)[1]
    save_path = os.path.join(MEDIA_ROOT, 'images')
    try:
        with open(os.path.join(save_path, imagename), "ab") as f:
            for chunk in img.chunks():
                f.write(chunk)
        i = Image()
        i.filename = filename
        i.imagename = imagename
        i.save()
        return imagename
    except Exception as e:
        print(e)
    return False


def delete_Image(imagename):
    image = Image.objects.get(imagename=imagename)
    if image.delete():
        return True
    return False
