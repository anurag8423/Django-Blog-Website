# Generated by Django 4.2 on 2023-05-26 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='shortDesc',
            field=models.CharField(default='', max_length=350),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.CharField(default='', max_length=100),
        ),
    ]
