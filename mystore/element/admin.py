from django.contrib import admin
from .models import Category, Type, Element

# Register your models here.
@admin.register(Category, Type, Element)
class BaseAdmin(admin.ModelAdmin): #Se puede registrar todo en la misma clase!
    list_display = ('id', 'title')
    search_fields = ('title', 'slug')
'''
@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', 'slug')

@admin.register(Element)
class ElementAdminAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', 'slug')
'''