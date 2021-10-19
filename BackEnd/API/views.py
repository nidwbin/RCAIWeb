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

from API.function import Authority, LoginOP, NewsOP, PapersOP

authority = Authority()


# Create your views here.

@ensure_csrf_cookie
def get_csrf(request):
    return authority.get_response(request, JsonResponse({}))


@csrf_exempt
def set_admin(request):
    if settings.DEBUG and request.method == 'PUT':
        username = request.GET.get('username')
        password = request.GET.get('password')
        if LoginOP.set_admin(username, password):
            return JsonResponse({'message': 'success'})
    return JsonResponse({'message': 'error'})


class Login(View):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if LoginOP.check_admin(username, password):
            return authority.get_response(request, JsonResponse({'message': 'success'}), put=True)
        else:
            return authority.get_response(request, JsonResponse({'message': 'error'}), keep=False)

    def delete(self, request):
        return authority.get_response(request, JsonResponse({'message': 'success'}), keep=False)


class List(View):
    def get(self, request):
        view_type = request.GET.get('type')
        filename = request.GET.get('filename')
        filetype = request.GET.get('filetype')
        content = request.GET.get('content')
        ans = [{'title': "这是一条新闻", 'image': "/static/images/logo.png", 'date': "2021-09-10", 'filename': "1",
                'show': True, 'overview': "这是一条新闻"},
               {'title': "这是一条新闻1", 'image': "/static/images/logo.png", 'date': "2021-09-11", 'filename': "2",
                'show': True, 'overview': "这是一条新闻"},
               {'title': "这是一条新闻2", 'image': "/static/images/logo.png", 'date': "2021-09-12", 'filename': "3",
                'show': True, 'overview': "这是一条新闻"},
               {'title': "这是一条新闻3", 'image': "/static/images/logo.png", 'date': "2021-09-13", 'filename': "4",
                'show': True, 'overview': "这是一条新闻"}, ]
        if view_type == 'news':
            if filetype == 'pages':
                return authority.get_response(request, JsonResponse({'message': 'success', 'content': 10}))
            elif filetype == 'lists':
                return authority.get_response(request, JsonResponse({'message': 'success', 'content': ans}))
            elif filetype == 'hots':
                return authority.get_response(request, JsonResponse({'message': 'success', 'content': ans}))
            elif filetype == 'item':

                return authority.get_response(request, JsonResponse({'message': 'success', 'content': ans[0]}))
        elif view_type == 'papers':
            if filetype == 'pages':
                pass
            elif filetype == 'papers':
                pass
            elif filetype == 'books':
                pass
        elif view_type == '':
            pass
        return authority.get_response(request, JsonResponse({'message': 'error'}))

    def post(self, request):
        if authority.check_pass(request) or settings.DEBUG:
            view_type = request.POST.get('type')
            filename = request.POST.get('filename')
            filetype = request.POST.get('filetype')
            content = request.POST.get('content')
            if view_type == 'news':
                if filetype == 'item':
                    if filename == 'new':
                        return authority.get_response(request, JsonResponse({'message': 'success', 'content': '1'}))
                    else:
                        pass
            elif view_type == 'papers':
                pass
        return authority.get_response(request, JsonResponse({'message': 'error'}))

    def delete(self, request):
        if authority.check_pass(request) or settings.DEBUG:
            pass
        return authority.get_response(request, JsonResponse({'message': 'error'}))


class File(View):
    def get(self, request):
        view_type = request.GET.get('type')
        filetype = request.GET.get('filetype')
        filename = request.GET.get('filename')
        if view_type == 'news':
            pass
            return authority.get_response(request, JsonResponse({'message': 'success', 'content': '# ok'}))
        elif view_type == 'papers':
            pass
            return authority.get_response(request, JsonResponse({'message': 'success', 'content': '# ok'}))
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
                OP = NewsOP if view_type == 'news' else PapersOP
                if filetype == 'image':
                    image_name = OP.add_image(content, filename)
                    if image_name:
                        return authority.get_response(request,
                                                      JsonResponse({'message': 'success', 'content': image_name}))
                elif filetype == 'markdown':
                    return authority.get_response(request,
                                                  JsonResponse({'message': 'success' if OP.change_file(filename, content) else 'error'}))
        return authority.get_response(request, JsonResponse({'message': 'error'}))

    def delete(self, request):
        if authority.check_pass(request) or settings.DEBUG:
            view_type = request.GET.get('type')
            filetype = request.GET.get('filetype')
            image_name = request.GET.get('filename')
            if view_type == 'news' or view_type == 'papers':
                OP = NewsOP if view_type == 'news' else PapersOP
                if filetype == 'image':
                    return authority.get_response(request,
                                                  JsonResponse({'message': 'success' if OP.delete_image(image_name) else 'error'}))
        return authority.get_response(request, JsonResponse({'message': 'error'}))
