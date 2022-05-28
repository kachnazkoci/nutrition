from user.models import User


def bmi(weight, height):

    x = weight/((height/100) * (height/100))
    if x <= 18.5:
        return "Underweight", round(x, 1)
    elif 18.5 < x <= 25:
        return "Normal weight", round(x, 1)
    elif 25 < x < 30:
        return "Overweight", round(x, 1)
    else:
        return "Obesity", round(x, 1)
