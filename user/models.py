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
    )
    TITLE_CHOICES = (
        ('0', 'Mr.'),
        ('1', 'Mrs.'),
        ('2', 'Ms.'),
    )

    ACTIVITY_1 = 'office job, no activities'
    ACTIVITY_2 = 'office job, training twice per week'
    ACTIVITY_3 = 'office job, training 3-4 times per week'
    ACTIVITY_4 = 'office job, training 6 times per week'
    ACTIVITY_5 = 'manual job, training 3-4 times per week'
    ACTIVITY_6 = 'manual job, training 6 times per week'

    ACTIVITY_CHOICES = (
        (ACTIVITY_1, 'office job, no activities'),
        (ACTIVITY_2, 'office job, training twice per week'),
        (ACTIVITY_3, 'office job, training 3-4 times per week'),
        (ACTIVITY_4, 'office job, training 6 times per week'),
        (ACTIVITY_5, 'manual job, training 3-4 times per week'),
        (ACTIVITY_6, 'manual job, training 6 times per week'),
    )

    TARGET_1 = 'I would like lose weight'
    TARGET_2 = 'I just want be as fit as I am'
    TARGET_3 = 'I want gain muscles/weight'

    TARGET_CHOICES = (
        (TARGET_1, 'I would like lose weight'),
        (TARGET_2, 'I just want be as fit as I am'),
        (TARGET_3, 'I want gain muscles/weight'),
    )

    name = models.CharField(max_length=256)
    title = models.CharField(choices=TITLE_CHOICES, max_length=5)
    birth_date = models.DateField()
    age = models.IntegerField()
    created_date = models.DateField()

    # gender = gender_check(title)

    gender = models.CharField(choices=GENDER_CHOICES, max_length=100)
    height = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    activity = models.CharField(help_text='How active are you?', choices=ACTIVITY_CHOICES, max_length=255,
                                default='office job, no activities')
    target = models.CharField(help_text='What is your target?', choices=TARGET_CHOICES, max_length=255,
                              default='I would like lose weight')

    def __str__(self):
        return f'{self.name} : {self.id}'

    def get_absolute_url(self):
        return resolve_url('user_detail', pk=self.id)

# class BasalMetabolism(models.Model):
#     ACTIVITY_1 = 'office job, no activities'
#     ACTIVITY_2 = 'office job, training twice per week'
#     ACTIVITY_3 = 'office job, training 3-4 times per week'
#     ACTIVITY_4 = 'office job, training 6 times per week'
#     ACTIVITY_5 = 'manual job, training 3-4 times per week'
#     ACTIVITY_6 = 'manual job, training 6 times per week'
#
#     ACTIVITY_CHOICES = (
#         (ACTIVITY_1, 'office job, no activities'),
#         (ACTIVITY_2, 'office job, training twice per week'),
#         (ACTIVITY_3, 'office job, training 3-4 times per week'),
#         (ACTIVITY_4, 'office job, training 6 times per week'),
#         (ACTIVITY_5, 'manual job, training 3-4 times per week'),
#         (ACTIVITY_6, 'manual job, training 6 times per week'),
#     )
#
#     TARGET_1 = 'I would like lose weight'
#     TARGET_2 = 'I just want be as fit as I am'
#     TARGET_3 = 'I want gain muscles/weight'
#
#     TARGET_CHOICES = (
#         (TARGET_1, 'I would like lose weight'),
#         (TARGET_2, 'I just want be as fit as I am'),
#         (TARGET_3, 'I want gain muscles/weight'),
#     )
#
#     weight = User.weight
#     height = User.height
#     gender = User.gender
#     activity = models.CharField(help_text='How active are you?', choices=ACTIVITY_CHOICES, max_length=255)
#     target = models.CharField(help_text='What is your target?', choices=TARGET_CHOICES, max_length=255)
