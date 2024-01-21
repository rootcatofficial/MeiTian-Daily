# Generated by Django 5.0 on 2024-01-05 15:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('todo', '0003_delete_review_delete_task'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('content', models.CharField(blank=True, max_length=1000, null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(max_length=10, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
