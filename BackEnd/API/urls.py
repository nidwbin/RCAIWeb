from API import views
from django.urls import path, include

urlpatterns = [
    path('test/', views.test.as_view()),
    path('', views.get_csrf),
]
