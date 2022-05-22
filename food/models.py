from django.db import models
from django.shortcuts import resolve_url


class Food(models.Model):
    name = models.CharField(max_length=256)
    created = models.DateField()
    kcal = models.IntegerField()
    protein = models.IntegerField()
    fats = models.IntegerField()
    carbs = models.IntegerField()

    def __str__(self):
        return self.name

    # class Meta:
    #     abstract = True

    def get_absolute_url(self):
        return resolve_url('food_detail', pk=self.id)


class Recipe(models.Model):
    name = models.CharField(max_length=256)
    created = models.DateField()
    ingredients = models.CharField(max_length=256)
    food = models.ManyToManyField(Food, related_name='recipes')
    kcal = models.IntegerField()
    protein = models.IntegerField()
    fats = models.IntegerField()
    carbs = models.IntegerField()

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return resolve_url('recipe_detail', pk=self.id)


class BMICounter(models.Model):
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'

    GENDER_CHOICES = (
        (GENDER_MALE, 'male'),
        (GENDER_FEMALE, 'female')
    )

    height = models.IntegerField()
    weight = models.IntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=100)


    def get_absolute_url(self):
        return resolve_url('counter_BMI', pk=self.id)