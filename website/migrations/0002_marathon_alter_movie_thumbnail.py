# Generated by Django 4.0.3 on 2022-04-26 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marathon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('description', models.CharField(max_length=1024, null=True)),
                ('price', models.FloatField(null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='movie',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
