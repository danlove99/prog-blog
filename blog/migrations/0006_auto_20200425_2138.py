# Generated by Django 3.0 on 2020-04-25 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_project_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='img_link',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.CharField(default='null', max_length=50),
        ),
    ]
