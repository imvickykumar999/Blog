# Generated by Django 5.0.4 on 2024-08-08 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_contactbanner'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogsBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blogs_banners/')),
            ],
        ),
    ]
