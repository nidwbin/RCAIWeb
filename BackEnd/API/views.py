'''
 * @FileDescription: api views
 * @Author: wenbin
 * @Date: 2021-09-25
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-28
'''

import django.middleware.csrf
from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse, JsonResponse

from API.function import Authority

authority = Authority()


# Create your views here.

@ensure_csrf_cookie
def get_csrf(request):
    return authority.get_response(request, JsonResponse({}))


class Login(View):
    def get(self, request):
        pass

    def post(self, request):
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        if name == 'hello' and pwd == '123456':
            return authority.get_response(request, JsonResponse({'message': 'success'}), put=True)
        else:
            return authority.get_response(request, JsonResponse({'message': 'error'}), keep=False)

    def delete(self, request):
        return authority.get_response(request, JsonResponse({}), keep=False)


class File(View):
    def get(self, request):
        type = request.GET.get('type')
        filetype = request.GET.get('filetype')
        filename = request.GET.get('filename')
        return authority.get_response(request, JsonResponse({'message': 'success', 'content': '# ok'}))

    def post(self, request):
        type = request.POST.get('type')
        filetype = request.POST.get('filetype')
        filename = request.POST.get('filename')
        if filetype == 'image':
            content = request.FILES.get('content')
        else:
            content = request.POST.get('content')
            print(content)
        return authority.get_response(request, JsonResponse({'message': 'success', 'content': '/images/logo.png'}))

    def delete(self, request):
        return authority.get_response(request, JsonResponse({'message': 'success', 'content': '/images/logo.png'}))
