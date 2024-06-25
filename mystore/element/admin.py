from django.contrib import admin
from .models import Category, Type, Element

# Register your models here.
@admin.register(Category, Type)
class BaseAdmin(admin.ModelAdmin): #Se puede registrar todo en la misma clase!
    list_display = ('id', 'title')
    search_fields = ('title', 'slug')

@admin.register(Element)
class ElementAdmin(admin.ModelAdmin): #Se puede registrar todo en la misma clase!
    list_display = ('id', 'title', 'type')
    search_fields = ('title', 'description', 'price', 'type')
    # fields = (('title','slug', 'price'), 'description', ('type', 'category')) # Para agrupar por renglones
    fieldsets = [
        (
            "Bloque principal",
            {
                "fields": (('title', 'slug', 'price'),)
            },
        ),
        (
            "Bloque secundario",
            {
                "fields": ('description', ('type', 'category')),
                # "classes": ["collapse"] # Esto sirve para colapsar
            },
        )
    ]
'''
@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', 'slug')
'''