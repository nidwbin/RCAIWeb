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
from django.contrib.auth.base_user import BaseUserManager
from API.models import Admin, Image, News, Papers, Student, Project, Fields, Achievements, Teacher
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
        if put or self.__check_pass__(now_time, request):
            if keep:
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
        else:
            self.__set_key__(now_time, 'Visitor', response, request)

    def check_pass(self, request):
        now_time = datetime.datetime.now()
        return self.__check_pass__(now_time, request)

    def get_response(self, request, response, keep=True, put=False):
        self.__check_key__(request, response, keep, put)
        response['Access-Control-Expose-Headers'] = "key,set-cookie"
        return response


class AdminOP:
    def __init__(self):
        password = BaseUserManager().make_random_password(length=20)
        if AdminOP.set_admin('RCAIROOT', password):
            with open('./root_password.txt', 'w') as f:
                f.write(password)

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
        if username != 'RCAIROOT':
            try:
                user = Admin.objects.get(name=username)
                user.delete()
                return True
            except Exception as e:
                print(e)
        return False


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
        return {'title': item.title, 'image': item.image_name, 'date': item.date, 'filename': item.filename,
                'show': item.show, 'overview': item.overview}.copy()

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

    def get_items(self, admin: bool = False, page: int = 1, pages: int = 10):
        try:
            items = self.Obj.objects.filter() if admin else self.Obj.objects.filter(show=True)
            items = items.order_by('-date')[(page - 1) * pages:page * pages]
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


class PapersOP:
    @staticmethod
    def __get_dict__(paper):
        return {'id': paper.id,
                'name': paper.name,
                'link': paper.link}.copy()

    @staticmethod
    def __get_list__(papers):
        ret_list = []
        for i in papers:
            ret_list.append(PapersOP.__get_dict__(i))
        return ret_list.copy()

    @staticmethod
    def count(pages: int):
        try:
            papers = Papers.objects.filter()
            length = math.ceil(len(papers) / pages)
            return length
        except Exception as e:
            print(e)
        return False

    @staticmethod
    def get_lists(page: int = 1, pages: int = 6):
        try:
            papers = Papers.objects.filter()
            return PapersOP.__get_list__(papers[(page - 1) * pages:page * pages])
        except Exception as e:
            print(e)
        return False

    @staticmethod
    def create(name: str, link: str):
        try:
            papers = Papers(name=name, link=link)
            papers.save()
            return True
        except Exception as e:
            print(e)
        return False

    @staticmethod
    def change(id_: int, name: str, link: str):
        try:
            paper = Papers.objects.get(id=id_)
            paper.name = name
            paper.link = link
            paper.save()
            return True
        except Exception as e:
            print(e)
        return False

    @staticmethod
    def delete(id_: int):
        try:
            paper = Papers.objects.get(id=id_)
            paper.delete()
            return True
        except Exception as e:
            print(e)
        return False


class PeopleOP:
    def __init__(self, obj):
        self.Obj = obj

    def change_info(self, id_: int, name: str, homepage: str, email: str, image):
        try:
            people = self.Obj.objects.get(id=id_)
            people.name = name
            people.homepage = homepage
            people.email = email
            if image:
                image_name = str(uuid.uuid4()) + os.path.splitext(image.name)[1]
                people.image.delete()
                people.image_name = image_name
                people.image = image
                people.image.name = image_name
            people.save()
            return True
        except Exception as e:
            print(e)
        return False

    def delete_info(self, id_: int):
        try:
            people = self.Obj.objects.get(id=id_)
            people.image.delete()
            people.delete()
            return True
        except Exception as e:
            print(e)
        return False


class StudentsOP(PeopleOP):
    def __init__(self):
        super(StudentsOP, self).__init__(Student)

    @staticmethod
    def __get_dict__(student):
        return {'id': student.id,
                'name': student.name,
                'image': student.image_name,
                'class': student.degree,
                'email': student.email,
                'link': student.homepage,
                'abstract': student.overview}.copy()

    @staticmethod
    def __get_list__(students):
        ret_list = []
        for i in students:
            ret_list.append(StudentsOP.__get_dict__(i))
        return ret_list.copy()

    @staticmethod
    def count(degree_type: str, pages: int):
        try:
            students = Student.objects.filter(degree_type=degree_type)
            length = math.ceil(len(students) / pages)
            return length
        except Exception as e:
            print(e)
        return False

    @staticmethod
    def get_lists(degree_type: str, page: int = 1, pages: int = 6):
        try:
            students = Student.objects.filter(degree_type=degree_type)
            return StudentsOP.__get_list__(students[(page - 1) * pages:page * pages])
        except Exception as e:
            print(e)
        return False

    @staticmethod
    def create(name: str, homepage: str, email: str, degree_type: str, degree: str, overview: str, image):
        try:
            if image:
                image_name = str(uuid.uuid4()) + os.path.splitext(image.name)[1]
            else:
                image_name = ''
            student = Student(name=name, homepage=homepage, email=email, degree_type=degree_type, degree=degree,
                              overview=overview, image_name=image_name)
            if image:
                student.image = image
                student.image.name = image_name
            student.save()
            return True
        except Exception as e:
            print(e)
        return False

    def change(self, id_: int, name: str, homepage: str, email: str, degree_type: str, degree: str, overview: str,
               image):
        try:
            student = Student.objects.get(id=id_, degree_type=degree_type)
            student.degree = degree
            student.overview = overview
            student.save()
            return self.change_info(id_, name, homepage, email, image)
        except Exception as e:
            print(e)
        return False

    def delete(self, id_: int):
        return self.delete_info(id_)


class TeachersOP(PeopleOP):
    def __init__(self):
        super(TeachersOP, self).__init__(Teacher)

    @staticmethod
    def __get_dict__(teacher):
        return {'id': teacher.id,
                'name': teacher.name,
                'image': teacher.image_name,
                'prof': teacher.professional_title,
                'email': teacher.email,
                'link': teacher.homepage,
                'tel': teacher.mobile,
                'adress': teacher.address,
                'desc': teacher.introduction}.copy()

    @staticmethod
    def __get_list__(teachers):
        ret_list = []
        for i in teachers:
            ret_list.append(TeachersOP.__get_dict__(i))
        return ret_list.copy()

    @staticmethod
    def get_lists():
        try:
            teachers = Teacher.objects.all()
            return TeachersOP.__get_list__(teachers)
        except Exception as e:
            print(e)
        return False

    @staticmethod
    def create(name: str, homepage: str, email: str, professional_title: str, introduction: str, mobile: str,
               address: str, image):
        try:
            if image:
                image_name = str(uuid.uuid4()) + os.path.splitext(image.name)[1]
            else:
                image_name = ''
            teacher = Teacher(name=name, homepage=homepage, email=email, professional_title=professional_title,
                              introduction=introduction, mobile=mobile, address=address, image_name=image_name)
            if image:
                teacher.image = image
                teacher.image.name = image_name
            teacher.save()
            return True
        except Exception as e:
            print(e)
        return False

    def change(self, id_: int, name: str, homepage: str, email: str, professional_title: str, introduction: str,
               mobile: str, address: str, image):
        try:
            teacher = Teacher.objects.get(id=id_)
            teacher.professional_title = professional_title
            teacher.introduction = introduction
            teacher.mobile = mobile
            teacher.address = address
            teacher.save()
            return self.change_info(id_, name, homepage, email, image)
        except Exception as e:
            print(e)
        return False

    def delete(self, id_: int):
        return self.delete_info(id_)


class ProjectsOP:
    @staticmethod
    def __get_dict__(project):
        return {'id': project.id,
                'name': project.name,
                'class': project.genre,
                'source': project.source,
                'bg_time': project.start_date,
                'ed_time': project.finish_date,
                'value': project.budget,
                'principal': project.role,
                'status': project.status,
                'desc': project.description,
                'image': project.image_name}.copy()

    @staticmethod
    def __get_list__(projects):
        ret_list = []
        for i in projects:
            ret_list.append(ProjectsOP.__get_dict__(i))
        return ret_list.copy()

    @staticmethod
    def count(pages: int):
        try:
            projects = Project.objects.filter()
            length = math.ceil(len(projects) / pages)
            return length
        except Exception as e:
            print(e)
        return False

    @staticmethod
    def get_lists(page: int = 1, pages: int = 6):
        try:
            projects = Project.objects.filter()
            return ProjectsOP.__get_list__(projects[(page - 1) * pages:page * pages])
        except Exception as e:
            print(e)
        return False

    @staticmethod
    def create(name: str, genre: str, source: str, start_date: str, finish_date: str, budget: str, role: str,
               status: str, description: str, image):
        try:
            if image:
                image_name = str(uuid.uuid4()) + os.path.splitext(image.name)[1]
            else:
                image_name = ''
            project = Project(name=name, genre=genre, source=source, start_date=start_date, finish_date=finish_date,
                              budget=budget, role=role, status=status, description=description, image_name=image_name)
            if image:
                project.image = image
                project.image.name = image_name
            project.save()
            return True
        except Exception as e:
            print(e)
        return False

    @staticmethod
    def change(id_: int, name: str, genre: str, source: str, start_date: str, finish_date: str, budget: str, role: str,
               status: str, description: str, image):
        try:
            project = Project.objects.get(id=id_)
            project.name = name
            project.genre = genre
            project.source = source
            project.start_date = start_date
            project.finish_date = finish_date
            project.budget = budget
            project.role = role
            project.status = status
            project.description = description
            if image:
                image_name = str(uuid.uuid4()) + os.path.splitext(image.name)[1]
                project.image.delete()
                project.image_name = image_name
                project.image = image
                project.image.name = image_name
            project.save()
            return True
        except Exception as e:
            print(e)
        return False

    @staticmethod
    def delete(id_: int):
        try:
            project = Project.objects.get(id=id_)
            project.image.delete()
            project.delete()
            return True
        except Exception as e:
            print(e)
        return False


class FieldsOP:
    @staticmethod
    def __get_dict__(field):
        return {'id': field.id,
                'name': field.name,
                'desc': field.description,
                'image': field.image_name}.copy()

    @staticmethod
    def __get_list__(fields):
        ret_list = []
        for i in fields:
            ret_list.append(FieldsOP.__get_dict__(i))
        return ret_list.copy()

    @staticmethod
    def count(pages: int):
        try:
            fields = Fields.objects.filter()
            length = math.ceil(len(fields) / pages)
            return length
        except Exception as e:
            print(e)
        return False

    @staticmethod
    def get_lists(page: int = 1, pages: int = 6):
        try:
            fields = Fields.objects.filter()
            return FieldsOP.__get_list__(fields[(page - 1) * pages:page * pages])
        except Exception as e:
            print(e)
        return False

    @staticmethod
    def create(name: str, description: str, image):
        try:
            if image:
                image_name = str(uuid.uuid4()) + os.path.splitext(image.name)[1]
            else:
                image_name = ''
            fields = Fields(name=name, description=description, image_name=image_name)
            if image:
                fields.image = image
                fields.image.name = image_name
            fields.save()
            return True
        except Exception as e:
            print(e)
        return False

    @staticmethod
    def change(id_: int, name: str, description: str, image):
        try:
            fields = Fields.objects.get(id=id_)
            fields.name = name
            fields.description = description
            if image:
                image_name = str(uuid.uuid4()) + os.path.splitext(image.name)[1]
                fields.image.delete()
                fields.image_name = image_name
                fields.image = image
                fields.image.name = image_name
            fields.save()
            return True
        except Exception as e:
            print(e)
        return False

    @staticmethod
    def delete(id_: int):
        try:
            fields = Fields.objects.get(id=id_)
            fields.image.delete()
            fields.delete()
            return True
        except Exception as e:
            print(e)
        return False


class AchievementsOP:
    @staticmethod
    def __get_dict__(achievement):
        return {'id': achievement.id,
                'name': achievement.name,
                'authors': achievement.author,
                'pub_time': achievement.pub_date,
                'press': achievement.publisher,
                'desc': achievement.overview}.copy()

    @staticmethod
    def __get_list__(achievements):
        ret_list = []
        for i in achievements:
            ret_list.append(AchievementsOP.__get_dict__(i))
        return ret_list.copy()

    @staticmethod
    def get_lists():
        try:
            achievements = Achievements.objects.all()
            return AchievementsOP.__get_list__(achievements)
        except Exception as e:
            print(e)
        return False

    @staticmethod
    def create(name: str, author: str, pub_date: str, publisher: str, overview: str):
        try:
            achievement = Achievements(name=name, author=author, pub_date=pub_date, publisher=publisher,
                                       overview=overview)
            achievement.save()
            return True
        except Exception as e:
            print(e)
        return False

    @staticmethod
    def change(id_: int, name: str, author: str, pub_date: str, publisher: str, overview: str):
        try:
            achievement = Achievements.objects.get(id=id_)
            achievement.name = name
            achievement.author = author
            achievement.pub_date = pub_date
            achievement.publisher = publisher
            achievement.overview = overview
            achievement.save()
            return True
        except Exception as e:
            print(e)
        return False

    @staticmethod
    def delete(id_: int):
        try:
            achievements = Achievements.objects.get(id=id_)
            achievements.delete()
            return True
        except Exception as e:
            print(e)
        return False
