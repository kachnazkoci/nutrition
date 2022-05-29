from datetime import date
#from .models import User


def calcul_age(born):
    age = 0
    month = born.month
    day = born.day
    year = born.year
    m_valid, d_valid = False, False
    if 1 <= month <= 12:
        m_valid = True
    if 1 <= day <= 31:
        d_valid = True
    if m_valid and d_valid:
        today = date.today()
        d = today.day
        m = today.month
        y = today.year
        if m >= month and d >= day:
            age = y - year
        else:
            age = y - year - 1
    else:
        print("Birth date is invalid!")
    return age


# born_at = User.birth_date
# calculate_age(born_at)

def gender_check(title_asked):
    gender = 'male'
    if title_asked == 0:
        gender = 'male'
    elif title_asked == 1 or title_asked == 2:
        gender = 'female'
    return gender


# title = User.title
# gender_check(title)
