# Generated by Django 4.2.7 on 2023-11-19 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webbproject', '0003_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('skills', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='project_images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webbproject.category')),
            ],
        ),
    ]