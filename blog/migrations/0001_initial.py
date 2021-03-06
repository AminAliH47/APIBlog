# Generated by Django 4.0.1 on 2022-01-20 16:04

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
            name='ArticlesCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_fa', models.CharField(max_length=100, verbose_name='title')),
                ('title_en', models.CharField(max_length=100, verbose_name='title')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': '02. Categories',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_fa', models.CharField(max_length=120, verbose_name='Title')),
                ('title_en', models.CharField(max_length=120, verbose_name='Title')),
                ('slug_fa', models.SlugField(unique=True, verbose_name='Slug')),
                ('slug_en', models.SlugField(unique=True, verbose_name='Slug')),
                ('body_fa', models.TextField(verbose_name='Article content')),
                ('body_en', models.TextField(verbose_name='Article content')),
                ('image', models.ImageField(upload_to='blog/articles', verbose_name='Article Image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.articlescategory', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'article',
                'verbose_name_plural': '01. Articles',
                'ordering': ('created_at',),
            },
        ),
    ]
