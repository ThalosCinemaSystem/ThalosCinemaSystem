# Generated by Django 4.0.3 on 2022-05-26 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_movie_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='is_durning_reservation',
            field=models.BooleanField(default=False),
        ),
    ]
