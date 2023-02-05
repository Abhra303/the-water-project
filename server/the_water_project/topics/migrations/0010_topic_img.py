# Generated by Django 3.2.4 on 2023-02-05 10:54

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0009_topic_no_of_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='img',
            field=cloudinary.models.CloudinaryField(default='localhost:80/media/i.png', max_length=255),
            preserve_default=False,
        ),
    ]
