from django.db import models
from django.shortcuts import resolve_url
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

#from food.forms import BlogForm
from user.models import User


class Food(models.Model):
    name = models.CharField(max_length=256)
    created = models.DateField()
    kcal = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    carbs = models.FloatField()

    def __str__(self):
        return self.name

    # class Meta:
    #     abstract = True

    def get_absolute_url(self):
        return resolve_url('food_detail', pk=self.id)


class Plate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)


class Recipe(models.Model):
    name = models.CharField(max_length=256)
    created = models.DateField()
    ingredients = models.ForeignKey(Food, on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)
    procedure = RichTextField(default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return resolve_url('recipe_detail', pk=self.id)


class Amount(models.Model):
    food_choice_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    recipe_weight_food = models.ForeignKey(Food, on_delete=models.CASCADE)
    amount = models.IntegerField()


class Blog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="{% static 'images' %}")
    is_active = models.BooleanField(default=True)

    # def save(self, commit=True):
    #     blog = super(BlogForm, self).save(commit=commit)
    #     blog.food.add(*self.cleaned_data.get('food'))
    #     return blog

    # def __str__(self):
    #     return self.name
    class Meta:
        verbose_name = 'Blog'
        ordering = ["timestamp"]

    def get_absolute_url(self):
        return resolve_url('blog_detail', pk=self.pk)



# class BlogPost(models.Model):
#     title = models.CharField(max_length=255, blank=False, null=False)
#     body = RichTextField(blank=False, null=False)

# class BMICounter(models.Model):
#     GENDER_MALE = 'male'
#     GENDER_FEMALE = 'female'
#
#     GENDER_CHOICES = (
#         (GENDER_MALE, 'male'),
#         (GENDER_FEMALE, 'female')
#     )
#
#     height = User.height
#     weight = User.weight
#     gender = User.gender
#
#
#     def get_absolute_url(self):
#         return resolve_url('counter_BMI', pk=self.id)
