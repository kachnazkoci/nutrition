# Generated by Django 4.0.3 on 2022-05-29 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_user_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.AlterField(
            model_name='user',
            name='title',
            field=models.CharField(choices=[('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.')], max_length=5),
        ),
    ]