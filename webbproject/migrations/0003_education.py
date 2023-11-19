# Generated by Django 4.2.7 on 2023-11-19 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webbproject', '0002_alter_experience_end_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('start_date', models.CharField(max_length=100)),
                ('end_date', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('gpa', models.CharField(max_length=100)),
                ('honors', models.TextField()),
            ],
        ),
    ]
