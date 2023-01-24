from django.urls import path, include
from . import views


urlpatterns=[
    path('', views.index),
    path('todo',views.get_api),
    path('todo/', views.post_api),
    path('todo/<int:id>/', views.sum_api),
]