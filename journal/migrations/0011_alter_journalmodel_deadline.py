# Generated by Django 4.2.7 on 2024-02-18 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0010_alter_journalmodel_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalmodel',
            name='deadline',
            field=models.DateTimeField(null=True, verbose_name='deadline'),
        ),
    ]
