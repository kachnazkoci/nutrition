# Generated by Django 4.0.4 on 2022-05-29 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0011_remove_recipe_food_alter_recipe_ingredients'),
    ]

    operations = [
        migrations.RenameField(
            model_name='amount',
            old_name='recipe_weight_food',
            new_name='food',
        ),
        migrations.RenameField(
            model_name='amount',
            old_name='food_choice_id',
            new_name='recipe',
        ),
    ]
