from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    author_name = models.CharField(max_length=255, verbose_name='Автор')

    def __str__(self):
        return f'id {self.id}: {self.name}'

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
