# Generated by Django 3.2.4 on 2021-06-26 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=30)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('mail', models.CharField(max_length=60)),
                ('admin', models.BooleanField()),
                ('hashed_password', models.CharField(max_length=40)),
            ],
        ),
    ]