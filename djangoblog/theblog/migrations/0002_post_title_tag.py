# Generated by Django 3.2 on 2021-04-11 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Dark Web', max_length=255),
        ),
    ]