from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from BackEnd.settings import SECRET_KEY


# Create your views here.

@csrf_exempt
def get_csrf(request):
    return JsonResponse({"csrf": SECRET_KEY})


class test(View):
    def get(self, request):
        return JsonResponse({1: "hello"})

    def post(self, request):
        pass

    def delete(self, request):
        pass
