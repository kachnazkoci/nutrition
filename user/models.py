from django.db import models
from datetime import date
import datetime
from django.shortcuts import resolve_url


class User(models.Model):
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'

    GENDER_CHOICES = (
        (GENDER_MALE, 'male'),
        (GENDER_FEMALE, 'female')
    )

    MR = 'Mr.'
    MRS = 'Mrs.'
    MS = 'Ms.'

    TITLE_CHOICES = (
        (MR, 'Mr.'),
        (MRS, 'Mrs.'),
        (MS, 'Ms.'),
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
    created_date = models.DateField()

    # gender = gender_check(title)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=100)
    height = models.IntegerField(null=True, blank=True, help_text='[cm]')
    weight = models.IntegerField(null=True, blank=True, help_text='[kg]')
    activity = models.CharField(choices=ACTIVITY_CHOICES, max_length=255,
                                default='office job, no activities') # How active are you?:
    target = models.CharField(choices=TARGET_CHOICES, max_length=255,
                              default='I would like lose weight') # help_text='What is your target?'

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
