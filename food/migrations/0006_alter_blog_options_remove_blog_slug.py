# Generated by Django 4.0.3 on 2022-05-22 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_blogpost'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['timestamp'], 'verbose_name': 'Blog'},
        ),
        migrations.RemoveField(
            model_name='blog',
            name='slug',
        ),
    ]
