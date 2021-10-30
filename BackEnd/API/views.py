'''
 * @FileDescription: api views
 * @Author: wenbin
 * @Date: 2021-09-25
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-28
'''

from django.views.generic import View
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.http import JsonResponse
from django.conf import settings
from API.function import Authority, AdminOP, NewsOP, PapersOP, StudentsOP, FieldsOP, ProjectsOP, AchievementsOP, \
    TeachersOP

authority = Authority()
adminOP = AdminOP()
newsOP = NewsOP()
papersOP = PapersOP()
studentsOP = StudentsOP()
fieldsOP = FieldsOP()
projectsOP = ProjectsOP()
achievementsOP = AchievementsOP()
teacherOP = TeachersOP()


# Create your views here.

@ensure_csrf_cookie
def get_csrf(request):
    return authority.get_response(request, JsonResponse({}))


class Admin(View):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if adminOP.check_admin(username, password) or settings.DEBUG:
            username_ = request.POST.get('username_')
            password_ = request.POST.get('password_')
            if adminOP.set_admin(username_, password_):
                return authority.get_response(request, JsonResponse({'message': 'success'}), put=True)
        return authority.get_response(request, JsonResponse({'message': 'error'}), keep=False)

    def delete(self, request):
        username = request.GET.get('username')
        password = request.GET.get('password')
        username_ = request.GET.get('username_')
        password_ = request.GET.get('password_')
        if adminOP.check_admin(username, password) and adminOP.check_admin(username_, password_):
            if adminOP.delete_admin(username_):
                return authority.get_response(request, JsonResponse({'message': 'success'}), put=True)
        return authority.get_response(request, JsonResponse({'message': 'error'}), keep=False)


class Login(View):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if AdminOP.check_admin(username, password) or settings.DEBUG:
            return authority.get_response(request, JsonResponse({'message': 'success'}), put=True)
        return authority.get_response(request, JsonResponse({'message': 'error'}), keep=False)

    def delete(self, request):
        return authority.get_response(request, JsonResponse({'message': 'success'}), keep=False)


class List(View):
    def get(self, request):
        view_type = request.GET.get('type')
        filetype = request.GET.get('filetype')
        ans = False

        if view_type == 'news':
            if filetype == 'pages':
                ans = newsOP.count(admin=request.GET.get('admin') == 'true', pages=int(request.GET.get('per_page')))
            elif filetype == 'lists':
                ans = newsOP.get_items(admin=request.GET.get('admin') == 'true', page=int(request.GET.get('page')),
                                       pages=int(request.GET.get('per_page')))
            elif filetype == 'hots':
                ans = newsOP.get_hots(tops=int(request.GET.get('len')))
            elif filetype == 'item':
                ans = newsOP.get_item(filename=request.GET.get('filename'))

        elif view_type == 'papers':
            if filetype == 'pages':
                ans = papersOP.count(pages=int(request.GET.get('per_page')))
            elif filetype == 'lists':
                ans = papersOP.get_lists(page=int(request.GET.get('page')), pages=int(request.GET.get('per_page')))
            elif filetype == 'books':
                ans = achievementsOP.get_lists()

        elif view_type == 'teachers':
            if filetype == 'lists':
                ans = teacherOP.get_lists()

        elif view_type == 'master' or view_type == 'doctor':
            if filetype == 'pages':
                ans = studentsOP.count(degree_type=view_type, pages=int(request.GET.get('per_page')))
            elif filetype == 'lists':
                ans = studentsOP.get_lists(degree_type=view_type, page=int(request.GET.get('page')),
                                           pages=int(request.GET.get('per_page')))
        elif view_type == 'directions':
            if filetype == 'pages':
                ans = fieldsOP.count(pages=int(request.GET.get('per_page')))
            elif filetype == 'lists':
                ans = fieldsOP.get_lists(page=int(request.GET.get('page')), pages=int(request.GET.get('per_page')))

        elif view_type == 'projects':
            if filetype == 'pages':
                ans = projectsOP.count(pages=int(request.GET.get('per_page')))
            elif filetype == 'lists':
                ans = projectsOP.get_lists(page=int(request.GET.get('page')), pages=int(request.GET.get('per_page')))
        if ans is not False:
            return authority.get_response(request, JsonResponse({'message': 'success', 'content': ans}))
        else:
            return authority.get_response(request, JsonResponse({'message': 'error'}))

    def post(self, request):
        if authority.check_pass(request) or settings.DEBUG:
            view_type = request.POST.get('type')
            filetype = request.POST.get('filetype')

            ans = False
            if view_type == 'news':
                if filetype == 'item':
                    filename = request.POST.get('filename')
                    if filename == 'new':
                        ans = newsOP.create()
                    else:
                        ans = newsOP.set_header(filename, request.POST.get('date'), request.POST.get('title'),
                                                request.POST.get('overview'), request.POST.get('show') == 'true',
                                                request.FILES.get('image'))

            elif view_type == 'papers':
                id_ = request.POST.get('id')
                if id_ == 'new':
                    if filetype == 'item':
                        ans = papersOP.create(name=request.POST.get('name'), link=request.POST.get('link'))
                    elif filetype == 'book':
                        ans = achievementsOP.create(name=request.POST.get('name'), author=request.POST.get('authors'),
                                                    pub_date=request.POST.get('pub_time'),
                                                    publisher=request.POST.get('press'),
                                                    overview=request.POST.get('desc'))
                else:
                    if filetype == 'item':
                        ans = papersOP.change(id_=id_, name=request.POST.get('name'), link=request.POST.get('link'))
                    elif filetype == 'book':
                        ans = achievementsOP.change(id_=id_, name=request.POST.get('name'),
                                                    author=request.POST.get('authors'),
                                                    pub_date=request.POST.get('pub_time'),
                                                    publisher=request.POST.get('press'),
                                                    overview=request.POST.get('desc'))

            elif view_type == 'teachers':
                id_ = request.POST.get('id')
                if id_ == 'new':
                    ans = teacherOP.create(name=request.POST.get('name'), homepage=request.POST.get('link'),
                                           email=request.POST.get('email'), professional_title=request.POST.get('prof'),
                                           introduction=request.POST.get('desc'), mobile=request.POST.get('tel'),
                                           address=request.POST.get('adress'), image=request.FILES.get('image_file'))
                else:
                    ans = teacherOP.change(id_=id_, name=request.POST.get('name'), homepage=request.POST.get('link'),
                                           email=request.POST.get('email'), professional_title=request.POST.get('prof'),
                                           introduction=request.POST.get('desc'), mobile=request.POST.get('tel'),
                                           address=request.POST.get('adress'), image=request.FILES.get('image_file'))

            elif view_type == 'master' or view_type == 'doctor':
                id_ = request.POST.get('id')
                if id_ == 'new':
                    ans = studentsOP.create(name=request.POST.get('name'), homepage=request.POST.get('link'),
                                            email=request.POST.get('email'), degree_type=view_type,
                                            degree=request.POST.get('class'), overview=request.POST.get('abstract'),
                                            image=request.FILES.get('image_file'))
                else:
                    ans = studentsOP.change(id_=id_, name=request.POST.get('name'), homepage=request.POST.get('link'),
                                            email=request.POST.get('email'), degree_type=view_type,
                                            degree=request.POST.get('class'), overview=request.POST.get('abstract'),
                                            image=request.FILES.get('image_file'))

            elif view_type == 'directions':
                id_ = request.POST.get('id')
                if id_ == 'new':
                    ans = fieldsOP.create(name=request.POST.get('name'), description=request.POST.get('desc'),
                                          image=request.FILES.get('image_file'))
                else:
                    ans = fieldsOP.change(id_=id_, name=request.POST.get('name'), description=request.POST.get('desc'),
                                          image=request.FILES.get('image_file'))

            elif view_type == 'projects':
                id_ = request.POST.get('id')
                if id_ == 'new':
                    ans = projectsOP.create(name=request.POST.get('name'), genre=request.POST.get('class'),
                                            source=request.POST.get('source'), start_date=request.POST.get('bg_time'),
                                            finish_date=request.POST.get('ed_time'), budget=request.POST.get('value'),
                                            role=request.POST.get('principal'), status=request.POST.get('state'),
                                            description=request.POST.get('desc'), image=request.FILES.get('image_file'))
                else:
                    ans = projectsOP.change(id_=id_, name=request.POST.get('name'), genre=request.POST.get('class'),
                                            source=request.POST.get('source'), start_date=request.POST.get('bg_time'),
                                            finish_date=request.POST.get('ed_time'), budget=request.POST.get('value'),
                                            role=request.POST.get('principal'), status=request.POST.get('state'),
                                            description=request.POST.get('desc'), image=request.FILES.get('image_file'))

            if ans is not False:
                return authority.get_response(request, JsonResponse({'message': 'success', 'content': ans}))
        return authority.get_response(request, JsonResponse({'message': 'error'}))

    def delete(self, request):
        if authority.check_pass(request) or settings.DEBUG:
            view_type = request.GET.get('type')
            filetype = request.GET.get('filetype')
            filename = request.GET.get('filename')
            ans = False
            if view_type == 'news':
                if filetype == 'item':
                    ans = newsOP.delete(filename)
            elif view_type == 'papers':
                if filetype == 'item':
                    ans = papersOP.delete(filename)
                elif filetype == 'book':
                    ans = achievementsOP.delete(filename)
            elif view_type == 'master' or view_type == 'doctor':
                if filetype == 'item':
                    ans = studentsOP.delete(filename)
            elif view_type == 'teachers':
                if filetype == 'item':
                    ans = teacherOP.delete(filename)
            elif view_type == 'directions':
                if filetype == 'item':
                    ans = fieldsOP.delete(filename)
            elif view_type == 'projects':
                if filetype == 'item':
                    ans = projectsOP.delete(filename)
            if ans is not False:
                return authority.get_response(request, JsonResponse({'message': 'success'}))
        return authority.get_response(request, JsonResponse({'message': 'error'}))


class File(View):
    def get(self, request):
        view_type = request.GET.get('type')
        filetype = request.GET.get('filetype')
        filename = request.GET.get('filename')
        ans = False
        if view_type == 'news':
            if filetype == 'markdown':
                ans = newsOP.read_file(filename)
        elif view_type == 'papers':
            pass
            return authority.get_response(request, JsonResponse({'message': 'success', 'content': '# ok'}))
        if ans is not False:
            return authority.get_response(request, JsonResponse({'message': 'success', 'content': ans}))
        else:
            return authority.get_response(request, JsonResponse({'message': 'error'}))

    def post(self, request):
        if authority.check_pass(request) or settings.DEBUG:
            view_type = request.POST.get('type')
            filetype = request.POST.get('filetype')
            filename = request.POST.get('filename')
            if filetype == 'image':
                content = request.FILES.get('content')
            else:
                content = request.POST.get('content')

            if view_type == 'news' or view_type == 'papers':
                OP = newsOP if view_type == 'news' else papersOP
                if filetype == 'image':
                    image_name = OP.add_image(content, filename)
                    if image_name:
                        return authority.get_response(request,
                                                      JsonResponse({'message': 'success', 'content': image_name}))
                elif filetype == 'markdown':
                    return authority.get_response(request, JsonResponse(
                        {'message': 'success' if OP.change_file(filename, content) else 'error'}))
        return authority.get_response(request, JsonResponse({'message': 'error'}))

    def delete(self, request):
        if authority.check_pass(request) or settings.DEBUG:
            view_type = request.GET.get('type')
            filetype = request.GET.get('filetype')
            image_name = request.GET.get('filename')
            if view_type == 'news' or view_type == 'papers':
                OP = NewsOP if view_type == 'news' else PapersOP
                if filetype == 'image':
                    return authority.get_response(request, JsonResponse(
                        {'message': 'success' if OP.delete_image(image_name) else 'error'}))
        return authority.get_response(request, JsonResponse({'message': 'error'}))
