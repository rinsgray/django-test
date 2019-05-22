from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('login/',views.index, name='index'),
    path('cb/', views.callback, name='callback'),
    path('rd/',views.redirect, name='redirect'),
]
