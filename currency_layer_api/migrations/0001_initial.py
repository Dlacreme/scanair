# Generated by Django 2.1.3 on 2019-11-09 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=256)),
            ],
        ),
    ]
