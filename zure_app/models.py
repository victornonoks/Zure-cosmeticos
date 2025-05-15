from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.ImageField(upload_to="image/")
    destaques = models.BooleanField(default=False)
    # categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, related_name='produtos')

    def __str__(self):
        return self.nome