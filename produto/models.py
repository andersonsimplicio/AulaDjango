from django.db import models
import os

def get_upload_path(instance, filename):
    # Obtém o nome do objeto
    nome_objeto = instance.nome
    # Obtém a extensão do arquivo
    extensao = os.path.splitext(filename)[1]
    # Define o caminho de upload como "fotos/nome_objeto.extensao"
    return f"produtos/{nome_objeto}/{nome_objeto}{extensao}"

class Produto(models.Model):
    nome = models.CharField(max_length=65)
    descricao = models.TextField(blank=True,null=True)
    preco = models.DecimalField(max_digits=8,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    quantidade = models.IntegerField(default=0)
    imagem = models.ImageField(upload_to=get_upload_path,blank=True,null=True)

    class Meta:
        verbose_name = 'Produto' 
        verbose_name_plural = 'Produtos'
    
    def __str__(self) -> str:
        return self.nome