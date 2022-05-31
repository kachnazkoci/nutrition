from user.models import User
from food.cal_counter_user import *


def protein_calculation(ici, target):
    target_1 = User.TARGET_1
    target_2 = User.TARGET_2
    if target == target_1:
        protein = (0.15*ici)/4
    elif target == target_2:
        protein = (0.13*ici)/4
    else:
        protein = (0.18*ici)/4
    return int(protein)


def carbs_calculation(ici, target):
    target_1 = User.TARGET_1
    target_2 = User.TARGET_2
    if target == target_1:
        carbs = (0.52*ici)/4
    elif target == target_2:
        carbs = (0.55*ici)/4
    else:
        carbs = (0.48*ici)/4
    return int(carbs)


def fats_calculation(ici, target):
    target_1 = User.TARGET_1
    target_2 = User.TARGET_2
    if target == target_1:
        fat = (0.27*ici)/9
    elif target == target_2:
        fat = (0.3*ici)/9
    else:
        fat = (0.3*ici)/9
    return int(fat)

