from django.contrib import admin
from .models import Kategoriya,news


@admin.register(Kategoriya)
class Kategoriya(admin.ModelAdmin):
    list_display = ['name']

@admin.register(news)
class News(admin.ModelAdmin):
    list_display = ['title','pub_date','kategoriya','xolati']
    list_filter = ['pub_date', 'kategoriya']
    search_fields = ['title']
