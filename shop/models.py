from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=250, verbose_name='Title')
    slug = models.SlugField(max_length=250, verbose_name='Slug', unique=True)
    sku = models.CharField(max_length=50, verbose_name='Sku', blank=True,
                           null=True)
    body = models.TextField(verbose_name='Description', blank=True,
                                   null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title
