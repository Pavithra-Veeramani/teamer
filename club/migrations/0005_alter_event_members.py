# Generated by Django 3.2.15 on 2022-09-04 13:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('club', '0004_auto_20220903_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='players_in_event', to=settings.AUTH_USER_MODEL),
        ),
    ]