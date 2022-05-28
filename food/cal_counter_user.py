from user.models import User


def basal_metabolic_rate(gender, weight, height, age):
    if gender == 'female':
        bmr = 655.0955+(9.5634*weight)+(1.8496*height)-(4.6756*age)
    else:
        bmr = 66.473+(13.7516*weight)+(5.0033*height)-(6.755*age)
    return bmr


def activity_calorie_input(bmr, activity):
    activity_1 = User.ACTIVITY_1
    activity_2 = User.ACTIVITY_2
    activity_3 = User.ACTIVITY_3
    activity_4 = User.ACTIVITY_4
    activity_5 = User.ACTIVITY_5
    if activity == activity_1:
        aci = (bmr * 1.2) * 1.1
    elif activity == activity_2:
        aci = (bmr * 1.4) * 1.1
    elif activity == activity_3:
        aci = (bmr * 1.6) * 1.1
    elif activity == activity_4:
        aci = (bmr * 1.8) * 1.1
    elif activity == activity_5:
        aci = (bmr * 2) * 1.1
    else:
        aci = (bmr * 2.2) * 1.1
    return aci


def ideal_calories_intake(aci, target):
    target_1 = User.TARGET_1
    target_2 = User.TARGET_2
    if target == target_1:
        ici = aci * 0.8
    elif target == target_2:
        ici = aci * 1
    else:
        ici = aci * 1.2
    return int(ici)




