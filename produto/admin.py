from django.contrib import admin

from .models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome','created_at','is_published' )
    search_fields = ('nome',) 
    list_editable = ('is_published',)
