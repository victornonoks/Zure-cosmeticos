from django.contrib import admin
from django.utils.html import format_html 
from .models import Produto

#Registra o modelo Produto no admin do Django
admin.site.register(Produto)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao_formatada', 'preco', 'destaques')

    def descricao_formatada(self, obj):
        # converte cada quebra de linha em <br>
        return format_html(obj.descricao.replace('\n', '<br>'))
    descricao_formatada.short_description = 'Descrição'