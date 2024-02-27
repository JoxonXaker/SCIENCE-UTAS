# Generated by Django 4.2.7 on 2023-12-03 13:37

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank='', max_length=150, null='', verbose_name='title')),
                ('title_uz', models.CharField(blank='', max_length=150, null=True, verbose_name='title')),
                ('title_ru', models.CharField(blank='', max_length=150, null=True, verbose_name='title')),
                ('title_en', models.CharField(blank='', max_length=150, null=True, verbose_name='title')),
                ('detail', ckeditor.fields.RichTextField(blank='', null='', verbose_name='detail')),
                ('detail_uz', ckeditor.fields.RichTextField(blank='', null=True, verbose_name='detail')),
                ('detail_ru', ckeditor.fields.RichTextField(blank='', null=True, verbose_name='detail')),
                ('detail_en', ckeditor.fields.RichTextField(blank='', null=True, verbose_name='detail')),
            ],
        ),
    ]
