# Generated by Django 4.2.7 on 2024-01-17 13:33

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('position', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='image')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='name')),
                ('name_uz', models.CharField(blank=True, max_length=255, null=True, verbose_name='name')),
                ('name_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='name')),
                ('name_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='name')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='phone')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
                ('address', models.CharField(blank=True, max_length=500, null=True, verbose_name='address')),
                ('address_uz', models.CharField(blank=True, max_length=500, null=True, verbose_name='address')),
                ('address_ru', models.CharField(blank=True, max_length=500, null=True, verbose_name='address')),
                ('address_en', models.CharField(blank=True, max_length=500, null=True, verbose_name='address')),
                ('detail', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='detail')),
                ('detail_uz', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='detail')),
                ('detail_ru', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='detail')),
                ('detail_en', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='detail')),
            ],
        ),
        migrations.CreateModel(
            name='JournalModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, null=True, verbose_name='title')),
                ('title_uz', models.CharField(max_length=500, null=True, verbose_name='title')),
                ('title_ru', models.CharField(max_length=500, null=True, verbose_name='title')),
                ('title_en', models.CharField(max_length=500, null=True, verbose_name='title')),
                ('valume', models.CharField(max_length=55, null=True, verbose_name='valume')),
                ('published', models.DateField(blank=True, null=True, verbose_name='published')),
                ('image', models.ImageField(blank=True, null=True, upload_to='article/photos', verbose_name='image')),
                ('files', models.FileField(blank=True, null=True, upload_to='article/files', verbose_name='files')),
                ('detail', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='detail')),
                ('detail_uz', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='detail')),
                ('detail_ru', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='detail')),
                ('detail_en', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='detail')),
                ('director', models.CharField(blank=True, max_length=200, null=True, verbose_name='director')),
                ('director_uz', models.CharField(blank=True, max_length=200, null=True, verbose_name='director')),
                ('director_ru', models.CharField(blank=True, max_length=200, null=True, verbose_name='director')),
                ('director_en', models.CharField(blank=True, max_length=200, null=True, verbose_name='director')),
                ('lead_editor', models.CharField(blank=True, max_length=200, null=True, verbose_name='lead_editor')),
                ('lead_editor_uz', models.CharField(blank=True, max_length=200, null=True, verbose_name='lead_editor')),
                ('lead_editor_ru', models.CharField(blank=True, max_length=200, null=True, verbose_name='lead_editor')),
                ('lead_editor_en', models.CharField(blank=True, max_length=200, null=True, verbose_name='lead_editor')),
                ('created', models.DateField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateField(auto_now=True, verbose_name='updated')),
                ('slug', models.CharField(blank=True, default='slug-problem', max_length=55, null=True, verbose_name='slug')),
                ('is_staf', models.BooleanField(default=False, verbose_name='is_staf')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('organ', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='organization', to='journal.organizationmodel')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=150, null=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='journal.journalmodel')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='detail')),
                ('files', models.FileField(blank=True, null=True, upload_to='article/files', verbose_name='files')),
                ('created', models.DateField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateField(auto_now=True, verbose_name='updated')),
                ('is_staf', models.BooleanField(default=False, verbose_name='is_staf')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
