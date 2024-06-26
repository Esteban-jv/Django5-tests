from django.contrib import admin
from .models import Comment

# Personalizar opciones de consulta en django admin
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text') # Campos que se muestran en la tabla
    search_fields = ('id', 'text') # Filtros de búsqueda
    date_hierarchy = 'posted' # Prioridad de filtros
    ordering = ('posted',) # Se puede ordenaar por más de 1 elemento en la tabla
    list_filter = ('id', 'posted') # Columna lateral de filtros
    # list_editable = ('text',) # Para editar fuera de la tabla

    fields = ('text',) # para modificar unicamente estos campos
    # exclude = ('emenet',) # Opposite of fields
    save_as=True # Mensaje "Save as"
    save_on_top=True # Save options on the top of the screen

    class Media:
        css = {
            "all": ['my_style.css']
        }

    def delete_queryset(self, request, queryset):
        print(("*"*45)+" - DELETING - "+("*"*45))
        super().delete_queryset(request, queryset)

    def save_model(self, request, obj, form, change):
        print(("*"*45)+" Saving "+("*"*45))
        super().save_model(request, obj, form, change)

# Register your models here.
# admin.site.register(Comment, CommentAdmin) # Se puede hacer así o bien con el decorador de clase
