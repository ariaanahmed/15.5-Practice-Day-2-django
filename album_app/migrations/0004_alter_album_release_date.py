# Generated by Django 5.0.6 on 2024-06-02 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album_app', '0003_alter_album_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.DateField(),
        ),
    ]