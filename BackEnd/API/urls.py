'''
 * @FileDescription: api urls
 * @Author: wenbin
 * @Date: 2021-09-25
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-28
'''

from django.views.static import serve

from API import views
from django.urls import path, include, re_path

urlpatterns = [
    path('csrf/', views.get_csrf),
    path('login/', views.Login.as_view()),
    path('file/', views.File.as_view()),
    path('list/', views.List.as_view()),
    path('register/', views.set_admin),
]
