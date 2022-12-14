# encoding: utf-8 
"""
@version: v1.0
@author: ligui
@contact: 1947346653@qq.com
@software: PyCharm
@file: urls.py
@time: 2022/11/18 21:55
"""
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

urlpatterns = [
    # path('classes/<pk>/students', ClassesViewSet.as_view({'post': 'add_student'}))
]

router = DefaultRouter()
router.register('classes', ClassesViewSet)
urlpatterns += router.urls
