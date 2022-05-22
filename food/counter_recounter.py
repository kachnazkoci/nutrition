from food.models import Recipe, Food


def convert_values(food_choice, new_weight):
    #food_choice =
    conv_kcal, conv_protein, conv_fats, conv_carbs = 0, 0, 0, 0
    if new_weight != 100:
        conv_kcal = (Food.kcal / 100) * Recipe.weight
        conv_protein = (Food.protein / 100) * Recipe.weight
        conv_fats = (Food.fats / 100) * Recipe.weight
        conv_carbs = (Food.carbs / 100) * Recipe.weight
    return conv_kcal, conv_protein, conv_fats, conv_carbs
