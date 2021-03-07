from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # path関数：URL、ビュー関数、
    path('post/<int:pk>/',views.post_detail,name='post_detail'),
]