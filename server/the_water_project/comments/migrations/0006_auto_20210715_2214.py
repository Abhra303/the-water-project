# Generated by Django 3.2.4 on 2021-07-15 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("comments", "0005_auto_20210715_2141"),
    ]

    operations = [
        migrations.RenameField(
            model_name="issuecommentlike",
            old_name="user",
            new_name="users",
        ),
        migrations.RenameField(
            model_name="startingcommentlike",
            old_name="user",
            new_name="users",
        ),
        migrations.RenameField(
            model_name="topiccommentlike",
            old_name="user",
            new_name="users",
        ),
    ]
