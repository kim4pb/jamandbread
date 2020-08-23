from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('question1/', views.question1, name='question1'),
    path('question2/', views.question2, name='question2'),
    path('question3/', views.question3, name='question3'),
    path('question4/', views.question4, name='question4'),
    path('result/', views.result, name='result'),
    path('info_detail/', views.info_detail, name='info_detail'),
]
