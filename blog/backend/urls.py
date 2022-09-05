from django.urls import path
from .. import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.addblog, name='addblog'),
    path('login/', views.login, name='login'),
    path('getblogs/', views.getblogs, name='getblogs'),
    path('delete/', views.deleteblog, name='deleteblog'),
    path('update/', views.updateblog, name='updateblog'),
]