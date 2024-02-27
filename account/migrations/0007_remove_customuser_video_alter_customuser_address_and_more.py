# Generated by Django 4.2.7 on 2024-02-12 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_remove_customuser_website_remove_customuser_youtube'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='video',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='bio',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='bio'),
        ),
    ]