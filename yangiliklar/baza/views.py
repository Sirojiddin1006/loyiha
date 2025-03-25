from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import news, Kategoriya, chop_etish


class IndexView(View):
    def get(self, request):
        baza = news.objects.all().filter(xolati=chop_etish)
        return render(request, 'indeks.html', {'baza': baza})
    def post(self, request):
        pass


