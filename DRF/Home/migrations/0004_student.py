# Generated by Django 5.1.4 on 2024-12-26 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_rename_ias_subscritions_licence_keys'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
