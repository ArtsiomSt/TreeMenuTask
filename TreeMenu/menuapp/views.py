from django.shortcuts import render
from django.views import View
from .models import Menu


class MainPageView(View):
    def get(self, request):
        return render(request, 'menuapp/index.html')


class TestPageView(View):
    def get(self, request, slug=None):
        return render(request, 'menuapp/menutest.html')
