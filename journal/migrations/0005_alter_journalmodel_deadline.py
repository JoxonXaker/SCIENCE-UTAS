# Generated by Django 4.2.7 on 2024-02-16 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0004_remove_journalcommentmodel_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalmodel',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True, verbose_name='deadline'),
        ),
    ]
