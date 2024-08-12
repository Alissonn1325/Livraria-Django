from django.db import models
from .editora import Editora
from .categoria import Categoria
from .autor import Autor


class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    quantidade = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="livros", null=True, blank=True)
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name="livros", null=True, blank=True)
    autores = models.ManyToManyField(Autor, related_name="livros")
    # coautor = models.ForeignKey(Autor, on_delete=models.PROTECT, related_name="livros_coautor", blank=True, null=True)

    autores = models.ManyToManyField(Autor, related_name="livros")

    def __str__(self):
        return f"{self.titulo} | ({self.quantidade}) | {self.preco}"
