# Generated by Django 4.0.3 on 2022-05-22 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_projection_marathon_alter_cinema_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]