from django.db import models

# Create your models here.
class Produto(models.Model):
    """Model definition for Produto."""

    nome = models.CharField(verbose_name='Nome', max_length=80)
    quantidade = models.IntegerField(verbose_name='Quantidade')
    preco = models.FloatField(verbose_name='Preço')
    dt = models.DateField(verbose_name='Data de criação', auto_now_add=True)
    
    class Meta:
        """Meta definition for Produto."""

        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        """Unicode representation of Produto."""
        return self.nome
