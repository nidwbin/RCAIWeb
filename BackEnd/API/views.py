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

from API.function import Authority, LoginOP, NewsOP, ResearchOP

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
        return authority.get_response(request, JsonResponse({}), keep=False)


class List(View):
    def get(self, request):
        view_type = request.GET.get('type')
        filename = request.GET.get('filename')
        filetype = request.GET.get('filetype')
        content = request.GET.get('content')
        ans = [{'title': "这是一条新闻", 'image': "/images/logo.png", 'date': "2021/9/10", 'filename': "1",
                'overview': "这是一条新闻"},
               {'title': "这是一条新闻", 'image': "/images/logo.png", 'date': "2021/9/10", 'filename': "1",
                'overview': "这是一条新闻"},
               {'title': "这是一条新闻", 'image': "/images/logo.png", 'date': "2021/9/10", 'filename': "1",
                'overview': "这是一条新闻"},
               {'title': "这是一条新闻", 'image': "/images/logo.png", 'date': "2021/9/10", 'filename': "1",
                'overview': "这是一条新闻"},
               {'title': "这是一条新闻", 'image': "/images/logo.png", 'date': "2021/9/10", 'filename': "1",
                'overview': "这是一条新闻"},
               {'title': "这是一条新闻", 'image': "/images/logo.png", 'date': "2021/9/10", 'filename': "1",
                'overview': "这是一条新闻"},
               {'title': "这是一条新闻", 'image': "/images/logo.png", 'date': "2021/9/10", 'filename': "1",
                'overview': "这是一条新闻"},
               {'title': "这是一条新闻", 'image': "/images/logo.png", 'date': "2021/9/10", 'filename': "1",
                'overview': "这是一条新闻"}, ]
        if view_type == 'news':
            if filename == 'pages':
                return authority.get_response(request, JsonResponse({'message': 'success', 'content': 10}))
            elif filename == 'lists':
                return authority.get_response(request, JsonResponse({'message': 'success', 'content': ans}))
            elif filename == 'hots':
                return authority.get_response(request, JsonResponse({'message': 'success', 'content': ans}))
        elif view_type == 'papers':
            if filename == 'pages':
                pass
            elif filename == 'papers':
                pass
            elif filename == 'books':
                pass
        elif view_type == '':
            pass
        return authority.get_response(request, JsonResponse({'message': 'error'}))

    def post(self, request):
        pass

    def delete(self, request):
        pass


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
        if authority.check_pass(request):
            view_type = request.POST.get('type')
            filetype = request.POST.get('filetype')
            filename = request.POST.get('filename')
            if filetype == 'image':
                content = request.FILES.get('content')
            else:
                content = request.POST.get('content')

            if view_type == 'news':
                if filetype == 'image':
                    image_name = NewsOP.add_image(content, filename)
                    if image_name:
                        return authority.get_response(request,
                                                      JsonResponse({'message': 'success', 'content': image_name}))
                elif filetype == 'markdown':
                    pass
            elif view_type == 'papers':
                if filetype == 'image':
                    NewsOP.add_image(content, filename)
                elif filetype == 'markdown':
                    pass
        return authority.get_response(request, JsonResponse({'message': 'error'}))

    def delete(self, request):
        image_name = request.DELETE.get('filename')
        if NewsOP.delete_image(image_name):
            return authority.get_response(request, JsonResponse({'message': 'success'}))
        return authority.get_response(request, JsonResponse({'message': 'error'}))
