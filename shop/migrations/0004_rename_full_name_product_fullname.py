# Generated by Django 4.2 on 2023-04-09 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_full_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='full_name',
            new_name='fullname',
        ),
    ]
