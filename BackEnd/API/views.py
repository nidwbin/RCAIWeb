import django.middleware.csrf
from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse, JsonResponse
from BackEnd.settings import SECRET_KEY


# Create your views here.

def check_key(request, response, set=False):
    if set or request.headers['Key'] == 'Admin':
        response['Key'] = 'Admin'


def set_key(request, response, next=True, set=False):
    if set or (next and 'Key' in request.headers):
        check_key(request,response,set)
    else:
        response['Key'] = 'Visitor'
    # response['Access-Control-Allow-Origin'] = "192.168.11.233:8000"
    # response['Access-Control-Allow-Credentials'] = True
    response['Access-Control-Allow-Header'] = 'key, set-cookie'
    # response['Access-Control-Allow-Method'] = 'PUT,POST,PATCH,DELETE'
    return response


@ensure_csrf_cookie
def get_csrf(request):
    return set_key(request, JsonResponse({}))


class Test(View):
    def get(self, request):
        return JsonResponse({1: "hello"})

    def post(self, request):
        name = request.POST.get('username', '')
        print(name)
        pwd = request.POST.get('password', '')
        print(pwd)

    def delete(self, request):
        pass


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
        pass

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