# Generated by Django 4.0.3 on 2022-05-21 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_cinema_address_alter_cinema_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinema',
            name='address',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='city',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='country',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='street',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='marathon',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='url_trailer',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='projection',
            name='type_projection',
            field=models.CharField(choices=[('Lektor', 'Lektor'), ('Napisy', 'Napisy'), ('Dubbing', 'Dubbing')], max_length=200, null=True),
        ),
    ]
