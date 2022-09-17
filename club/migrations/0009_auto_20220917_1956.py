# Generated by Django 3.2.15 on 2022-09-17 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('club', '0008_alter_event_created_by'),
    ]

    operations = [
        migrations.RunSQL("delete from club_event"),
        migrations.RunSQL("delete from club_event_members"),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=12)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='club.member'),
        ),
        migrations.AlterField(
            model_name='event',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='players_in_event', to='club.Member'),
        ),
    ]
