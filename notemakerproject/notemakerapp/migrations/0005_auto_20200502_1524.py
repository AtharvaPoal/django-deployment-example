# Generated by Django 2.2.12 on 2020-05-02 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notemakerapp', '0004_auto_20200502_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]