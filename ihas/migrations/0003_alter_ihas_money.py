# Generated by Django 4.1.2 on 2022-11-06 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ihas', '0002_ihas_iha_image_alter_ihas_brand_alter_ihas_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ihas',
            name='money',
            field=models.IntegerField(verbose_name='Fiyat'),
        ),
    ]
