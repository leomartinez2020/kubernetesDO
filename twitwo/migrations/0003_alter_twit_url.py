# Generated by Django 3.2.9 on 2021-12-02 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitwo', '0002_alter_twit_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twit',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
