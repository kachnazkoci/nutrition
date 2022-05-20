from django.db import models
from datetime import date
import datetime
from django.shortcuts import resolve_url


# def calculate_age(born):
#     month = int(born[:2])
#     day = int(born[3:5])
#     year = int(born[6:])
#     m_valid, d_valid = False
#     if 1 <= month <= 12:
#         m_valid = True
#         return m_valid
#     if 1 <= day <= 31:
#         d_valid = True
#         return d_valid
#     if m_valid and d_valid:
#         today = date.today()
#         d = today.day
#         m = today.month
#         y = today.year
#         if m >= month and d >= day:
#             age = y - year
#         else:
#             age = y - year - 1
#     else:
#         print("Birth date is invalid!")
#     return age


# def gender_check(title_asked):
#     if User.title == 0:
#         gender = 'male'
#     elif User.title == 1 or User.title == 2:
#         gender = 'female'
#     return gender


class User(models.Model):
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'

    GENDER_CHOICES = (
        (GENDER_MALE, 'male'),
        (GENDER_FEMALE, 'female')
    )

    TITLE_SELECT = (
        ('0', 'Mr.'),
        ('1', 'Mrs.'),
        ('2', 'Ms.'),
        ('3', 'Mast.'),
    )

    name = models.CharField(max_length=256)
    title = models.CharField(choices=TITLE_SELECT, max_length=5)
    birth_date = models.DateField()
    # age = calculate_age(birth_date)
    created_date = models.DateField()

    #gender = gender_check(title)

    gender = models.CharField(choices=GENDER_CHOICES, max_length=100)

    def __str__(self):
        return f'{self.name} : {self.id}'

    def get_absolute_url(self):
        return resolve_url('user_detail', pk=self.id)



