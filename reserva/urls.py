from django.conf.urls import url
from django.urls import path
from .views import *

from . import views

urlpatterns = [
    path('', index, name='index'),
    path('available_class_list.html', views.AvailableClassesListView.as_view(), name='my_classes'),
]