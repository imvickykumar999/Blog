# Generated by Django 5.0.8 on 2024-08-08 11:24

import ckeditor.fields
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_title', models.CharField(max_length=255)),
                ('meta_description', models.TextField()),
                ('meta_keywords', models.TextField()),
                ('article_slug', models.SlugField(max_length=255, unique=True)),
                ('author_name', models.CharField(max_length=255)),
                ('article_title_h1', models.CharField(max_length=255)),
                ('article_short_description', models.CharField(max_length=200)),
                ('article_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('thoughts', models.TextField()),
                ('description', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='article_images/')),
            ],
        ),
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CallToAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calltoaction', models.CharField(max_length=255)),
                ('calltoaction_p', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactQueries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('mailid', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_content', models.TextField(default='')),
                ('location', models.CharField(default='', max_length=255)),
                ('email', models.EmailField(default='', max_length=255)),
                ('call', models.CharField(default='', max_length=255)),
                ('twitter_url', models.URLField(default='', max_length=255)),
                ('facebook_url', models.URLField(default='', max_length=255)),
                ('instagram_url', models.URLField(default='', max_length=255)),
                ('linkedin_url', models.URLField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('twitter_link', models.URLField(blank=True, null=True)),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('instagram_link', models.URLField(blank=True, null=True)),
                ('linkedin_link', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='team_images/')),
            ],
        ),
        migrations.CreateModel(
            name='SEOmeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('keywords', models.TextField()),
                ('og_title', models.CharField(max_length=255)),
                ('og_url', models.CharField(max_length=255)),
                ('og_image', models.CharField(max_length=255)),
                ('og_image_type', models.CharField(max_length=255)),
                ('og_image_width', models.CharField(max_length=255)),
                ('og_image_height', models.CharField(max_length=255)),
                ('og_type', models.CharField(max_length=255)),
                ('og_locale', models.CharField(max_length=255)),
                ('og_image_url', models.CharField(max_length=255)),
                ('og_image_secure_url', models.CharField(max_length=255)),
                ('og_site_name', models.CharField(max_length=255)),
                ('og_see_also', models.CharField(max_length=255)),
                ('article_author', models.CharField(max_length=255)),
                ('format_detection', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StaticContentAbout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=500)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='StaticContentContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('call', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StaticContentHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=500)),
                ('content_p1', models.TextField()),
                ('content_p2', models.TextField()),
                ('youtube_url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WhyChooseMeSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('subtitle', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ArticleDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='article_images/')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.article')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blogcategory'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.article')),
            ],
        ),
    ]
