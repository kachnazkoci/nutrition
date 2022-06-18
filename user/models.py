from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date
import datetime
from django.shortcuts import resolve_url

from user.check import calcul_age


# class User(AbstractUser):
#     pass

class UserManager(BaseUserManager):
    def create_user(self, email, username=None, password=None, first_name=None, last_name=None, **extra_fields):
        if not email:
            raise ValueError('Enter an email address')
        if not first_name:
            raise ValueError('Enter a first name')
        if not last_name:
            raise ValueError('Enter a last name')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email, username=username, password=password, first_name='A', last_name='B',
                                title=User.MS, birth_date=datetime.date(1970, 1, 1),
                                gender=User.GENDER_FEMALE)

        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractUser):
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

    title = models.CharField(choices=TITLE_CHOICES, max_length=5)
    birth_date = models.DateField()
    created_date = models.DateField(auto_now_add=True)

    # gender = gender_check(title)

    gender = models.CharField(choices=GENDER_CHOICES, max_length=100)
    height = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    activity = models.CharField(help_text='How active are you?', choices=ACTIVITY_CHOICES, max_length=255,
                                default='office job, no activities')
    target = models.CharField(help_text='What is your target?', choices=TARGET_CHOICES, max_length=255,
                              default='I would like lose weight')
    objects = UserManager()

    def __str__(self):
        return f'{self.first_name} : {self.id}'

    def get_absolute_url(self):
        return resolve_url('user_detail', pk=self.id)

    def get_age(self):
        return calcul_age(self.birth_date)




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
