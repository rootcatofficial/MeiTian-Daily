# Generated by Django 5.0 on 2023-12-27 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_review'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
