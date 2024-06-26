from django.contrib import admin
from django.utils.text import slugify
from .models import Category, Type, Element

# Register your models here.

class ElementInline(admin.TabularInline): # Esto junto con inlines = [ ... ] sirve para crear y editar modelos relacionados
    model = Element

@admin.register(Category, Type)
class BaseAdmin(admin.ModelAdmin): #Se puede registrar todo en la misma clase!
    list_display = ('id', 'title')
    search_fields = ('title', 'slug')
    # inlines = [
    #     ElementInline
    # ]

@admin.display(description="Id + título")
def upper_title(self):
    return f"{self.id} - {self.title}".upper()

@admin.register(Element)
class ElementAdmin(admin.ModelAdmin): #Se puede registrar todo en la misma clase!
    list_display = ('id', 'title', 'type', upper_title, 'cheap')
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

    # TODO: Investigar que es change en este método
    def save_model(self, request, obj, form, change): # Este método crea un slug en caso de no haber
        if not(change) and obj.slug == '':
            obj.change = slugify(obj.title)

        if obj.slug == '':
            obj.slug = slugify(obj.title)

        super().save_model(request, obj, form, change)
'''
@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', 'slug')
'''