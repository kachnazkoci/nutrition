from user.models import User


def bmi(weight, height):

    x = weight/((height/100) * (height/100))
    if x <= 18.5:
        return "Underweight", x
    elif 18.5 < x <= 25:
        return "Normal weight", x
    elif 25 < x < 30:
        return "Overweight", x
    else:
        return "Obesity", x
