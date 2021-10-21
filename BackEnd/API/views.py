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
newsOP = NewsOP()
papersOP = PapersOP()


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
        filetype = request.GET.get('filetype')
        ans = False

        if view_type == 'news':
            if filetype == 'pages':
                ans = newsOP.count(admin=request.GET.get('admin') == 'true', pages=int(request.GET.get('per_page')))
            elif filetype == 'lists':
                ans = newsOP.get_items(admin=request.GET.get('admin') == 'true', page=int(request.GET.get('page')))
            elif filetype == 'hots':
                ans = newsOP.get_hots(tops=int(request.GET.get('len')))
            elif filetype == 'item':
                ans = newsOP.get_item(filename=request.GET.get('filename'))
        elif view_type == 'papers':
            if filetype == 'pages':
                ans = papersOP.count(admin=request.GET.get('admin') == 'true', pages=int(request.GET.get('per_page')))
            elif filetype == 'papers':
                ans = papersOP.get_items(admin=request.GET.get('admin') == 'true', page=int(request.GET.get('page')))
            elif filetype == 'books':
                pass

        if ans is not False:
            return authority.get_response(request, JsonResponse({'message': 'success', 'content': ans}))
        else:
            return authority.get_response(request, JsonResponse({'message': 'error'}))

    def post(self, request):
        if authority.check_pass(request) or settings.DEBUG:
            view_type = request.POST.get('type')
            filename = request.POST.get('filename')
            filetype = request.POST.get('filetype')

            ans = False
            if view_type == 'news':
                if filetype == 'item':
                    if filename == 'new':
                        ans = newsOP.create()
                    else:
                        ans = newsOP.set_header(filename, request.POST.get('date'), request.POST.get('title'),
                                                request.POST.get('overview'), request.POST.get('show') == 'true',
                                                request.FILES.get('image'))
            elif view_type == 'papers':
                pass
            if ans:
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
