# Generated by Django 3.2.15 on 2022-09-21 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0011_event_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='position',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]