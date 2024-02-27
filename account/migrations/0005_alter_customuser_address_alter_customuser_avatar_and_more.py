# Generated by Django 4.2.7 on 2024-02-12 09:16

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_customuser_age_customuser_facebook_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar', verbose_name='avatar'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='bio',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='bio'),
        ),
    ]