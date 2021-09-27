from API import views
from django.urls import path, include

urlpatterns = [
    path('test/', views.Test.as_view()),
    path('login/', views.Login.as_view()),
    path('csrf/', views.get_csrf),
]
