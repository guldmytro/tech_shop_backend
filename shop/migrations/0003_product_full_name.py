# Generated by Django 4.2 on 2023-04-09 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_body_product_description_remove_product_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='full_name',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Full Name'),
        ),
    ]