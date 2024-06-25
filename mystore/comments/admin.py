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

# Register your models here.
# admin.site.register(Comment, CommentAdmin) # Se puede hacer así o bien con el decorador de clase
