from food.models import weight, height


def BMI(weight, height):
    x = weight/(height * height)
    if x <= 18.5:
        return "Underweight"
    elif 18.5 < x <= 25:
        return "Normal weight"
    elif 25 < x < 30:
        return "Overweight"
    else:
        return "Obesity"