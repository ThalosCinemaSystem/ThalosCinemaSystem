# Generated by Django 4.0.3 on 2022-05-28 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_projection_marathon'),
    ]

    operations = [
        migrations.AddField(
            model_name='projection',
            name='is_cyclic',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
