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

from function import set_key

# Create your views here.

@ensure_csrf_cookie
def get_csrf(request):
    return set_key(request, JsonResponse({}))


class Login(View):
    def get(self, request):
        return JsonResponse({1: "hello"})

    def post(self, request):
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        if name == 'hello' and pwd == '123456':
            return set_key(request, JsonResponse({'message': 'success'}), set=True)
        else:
            return set_key(request, JsonResponse({'message': 'error'}), next=False)

    def delete(self, request):
        return set_key(request,JsonResponse({}),next=False)


class File(View):
    def get(self, request):
        type = request.GET.get('type')
        filename = request.GET.get('filename')
        return JsonResponse({'data': '# ok'})

    def post(self, request):
        type = request.POST.get('type')
        filename = request.POST.get('filename')
        file = request.POST.get('file')
        return JsonResponse({'message':'success', 'url':'/images/logo.png'})

    def delete(self, request):
        pass