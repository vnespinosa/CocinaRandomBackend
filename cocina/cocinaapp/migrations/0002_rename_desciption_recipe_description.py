# Generated by Django 3.2.6 on 2021-08-06 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocinaapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='desciption',
            new_name='description',
        ),
    ]