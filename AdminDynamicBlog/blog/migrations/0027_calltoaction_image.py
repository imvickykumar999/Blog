# Generated by Django 5.0.4 on 2024-08-08 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_blogsbanner'),
    ]

    operations = [
        migrations.AddField(
            model_name='calltoaction',
            name='image',
            field=models.ImageField(default='call_to_action_images/default.jpg', upload_to='call_to_action_images/'),
        ),
    ]
