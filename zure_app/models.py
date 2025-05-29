from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    titulo_informativo = models.CharField(max_length=100, blank=True, null=True)
    informativo = models.TextField(null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.ImageField(upload_to="image/")
    foto_secundaria = models.ImageField(upload_to="image/", blank=True, null=True)
    modo_de_uso = models.TextField(null=True, blank=True)
    beneficios = models.TextField(null=True, blank=True)
    destaques = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.nome