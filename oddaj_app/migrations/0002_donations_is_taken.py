# Generated by Django 2.2.8 on 2020-01-02 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oddaj_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donations',
            name='is_taken',
            field=models.BooleanField(default=False),
        ),
    ]