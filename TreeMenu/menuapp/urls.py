from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path("", MainPageView.as_view(), name='home'),
    path("test/", MainPageView.as_view(), name='test'),
    path("menu/<slug:slug>", TestPageView.as_view(), name='menuitems'),
    path("menu/",  TestPageView.as_view())
]
