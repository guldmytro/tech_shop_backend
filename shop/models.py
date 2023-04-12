from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Name',
                            db_index=True)
    slug = models.SlugField(max_length=250, verbose_name='Slug', unique=True,
                            db_index=True)
    fullname = models.CharField(max_length=250, verbose_name='Full Name',
                                blank=True, null=True)
    sku = models.CharField(max_length=50, verbose_name='Sku', blank=True,
                           null=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True,
                              verbose_name='Image')
    description = models.TextField(verbose_name='Description', blank=True,
                                   null=True)
    price = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-available', '-created',)

    def __str__(self):
        return self.name
