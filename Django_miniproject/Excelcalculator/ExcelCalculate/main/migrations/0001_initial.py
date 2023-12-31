# Generated by Django 4.2.3 on 2023-08-01 13:56

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
                ('user_name', models.CharField(max_length=20)),
                ('user_email', models.EmailField(max_length=254, unique=True)),
                ('user_password', models.CharField(max_length=100)),
                ('user_validate', models.BooleanField(default=False)),
            ],
        ),
    ]
