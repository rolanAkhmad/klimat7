# Generated by Django 3.1.5 on 2021-06-09 11:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_auto_20210528_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='detail_description',
        ),
        migrations.AddField(
            model_name='product',
            name='specifications',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Характеристики'),
        ),
    ]
