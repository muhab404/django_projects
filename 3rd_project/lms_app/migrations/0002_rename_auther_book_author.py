# Generated by Django 4.0.1 on 2022-01-16 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='auther',
            new_name='author',
        ),
    ]
