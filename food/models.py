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
    ingredients = models.CharField()
    food = models.ManyToManyField(Food, related_name='recipes')
    kcal = models.IntegerField()
    protein = models.IntegerField()
    fats = models.IntegerField()
    carbs = models.IntegerField()

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return resolve_url('recipe_detail', pk=self.id)
