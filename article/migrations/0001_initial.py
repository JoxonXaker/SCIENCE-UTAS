# Generated by Django 4.2.7 on 2024-02-17 07:16

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('journal', '0007_alter_journalmodel_deadline'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('waiting', 'Waiting'), ('confirmed', 'Confirmed'), ('reediting', 'Reediting'), ('canceled', 'Canceled')], default='waiting', max_length=10, verbose_name='status')),
                ('title', models.CharField(blank=True, max_length=256, null=True, verbose_name='title')),
                ('about', models.CharField(blank=True, max_length=512, null=True, verbose_name='about')),
                ('files', models.FileField(blank=True, null=True, upload_to='article/files', verbose_name='files')),
                ('detail', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='detail')),
                ('created', models.DateField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateField(auto_now=True, verbose_name='updated')),
                ('phone', models.CharField(blank=True, max_length=64, null=True, verbose_name='phone_number')),
                ('email', models.EmailField(blank=True, max_length=64, null=True, verbose_name='email')),
                ('video', models.CharField(blank=True, max_length=256, null=True, verbose_name='video')),
                ('facebook', models.CharField(blank=True, max_length=64, null=True, verbose_name='facebook')),
                ('telegram', models.CharField(blank=True, max_length=64, null=True, verbose_name='telegram')),
                ('instagram', models.CharField(blank=True, max_length=64, null=True, verbose_name='instagram')),
                ('youtube', models.CharField(blank=True, max_length=64, null=True, verbose_name='youtube')),
                ('website', models.CharField(blank=True, max_length=64, null=True, verbose_name='website')),
                ('whatsapp', models.CharField(blank=True, max_length=64, null=True, verbose_name='whatsapp')),
                ('is_read_by_admin', models.BooleanField(default=False)),
                ('is_view_by_owner', models.BooleanField(default=False)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('journal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='journal.journalmodel')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='DeadlineModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True, verbose_name='deadline name')),
                ('about', ckeditor.fields.RichTextField(null=True, verbose_name='about')),
                ('date', models.DateField(null=True, verbose_name='date')),
            ],
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=255, null=True, verbose_name='comment')),
                ('created', models.DateField(auto_now_add=True, verbose_name='created')),
                ('is_read', models.BooleanField(default=False)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.articlemodel')),
                ('created_at', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
