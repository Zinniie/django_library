# Generated by Django 4.0.6 on 2022-07-09 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='authour',
            new_name='author',
        ),
    ]
