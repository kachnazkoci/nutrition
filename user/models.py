from django.db import models
import datetime
from datetime import date
from django.shortcuts import resolve_url


# def calculate_age(born):
#     rtd = datetime.datetime.now().date()
#     bd = datetime.date(born)
#     age_years = int((rtd-bd).days / 365.25)
#     return age_years

class User(models.Model):
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'

    GENDER_CHOICES = (
        (GENDER_MALE, 'male'),
        (GENDER_FEMALE, 'female')
    )
    TITLE_CHOICES = [
        ('MR', 'Mr.'),
        ('MRS', 'Mrs.'),
        ('MS', 'Ms.'),
    ]
    name = models.CharField(max_length=256)
    title = models.CharField(choices=TITLE_CHOICES, max_length=3)
    birth_date = models.DateField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=100)
    #age = calculate_age(birth_date)
    weight = models.FloatField()
    height = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


    def get_absolute_url(self):
        return resolve_url('user_detail', pk=self.id )