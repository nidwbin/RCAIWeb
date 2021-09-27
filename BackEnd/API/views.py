import django.middleware.csrf
from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse, JsonResponse
from BackEnd.settings import SECRET_KEY


# Create your views here.

def set_key(request, response, admin):
    error = "Visitor"
    if admin == 'next':
        response['Key'] = 'Admin'
    elif admin == 'first':
        response['Key'] = 'Admin'
    else:
        response['Key'] = error
    # response['Access-Control-Allow-Origin'] = "192.168.11.233:8000"
    # response['Access-Control-Allow-Credentials'] = True
    # response['Access-Control-Allow-Header'] = 'Content-Type, X-Requested-With,X-CSRFToken,COOKIES'
    # response['Access-Control-Allow-Method'] = 'PUT,POST,PATCH,DELETE'
    return response


@ensure_csrf_cookie
def get_csrf(request):
    csrf = django.middleware.csrf.get_token(request)
    request.session['_csrftoken'] = csrf
    return set_key(request, JsonResponse({'csrf': csrf}), 'none')


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
            return set_key(request, JsonResponse({'message': 'success'}), 'first')
        else:
            return set_key(request, JsonResponse({'message': 'error'}), 'none')

    def delete(self, request):
        pass
