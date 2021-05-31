# Generated by Django 3.1.5 on 2021-05-28 11:55

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20210515_1743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='title_category_manufacturer',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='detail_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Детальное описание'),
        ),
        migrations.AlterField(
            model_name='productgalery',
            name='image',
            field=models.ImageField(default='images/banner.jpg', upload_to='media', verbose_name='Изображение'),
        ),
    ]
