# Generated by Django 4.2.7 on 2024-02-16 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0005_alter_journalmodel_deadline'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journalmodel',
            old_name='author',
            new_name='created_by',
        ),
    ]
