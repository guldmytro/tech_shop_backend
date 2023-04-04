from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=250, verbose_name='Назва товару')

    def __str__(self):
        return self.title
