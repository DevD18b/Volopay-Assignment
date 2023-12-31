# Generated by Django 4.2.1 on 2023-06-17 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('user', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('software', models.CharField(max_length=100)),
                ('seats', models.IntegerField()),
                ('amount', models.FloatField()),
            ],
        ),
    ]
