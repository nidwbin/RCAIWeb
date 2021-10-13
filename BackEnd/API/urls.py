'''
 * @FileDescription: api urls
 * @Author: wenbin
 * @Date: 2021-09-25
 * @LastEditors: wenbin
 * @LastEditTime: 2021-09-28
'''

from API import views
from django.urls import path, include

urlpatterns = [
    path('csrf/', views.get_csrf),
    path('login/', views.Login.as_view()),
    path('file/', views.File.as_view()),
    path('file/', views.File.as_view()),
]
