from django.db import models
from django.shortcuts import resolve_url
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


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


class Blog(models.Model):
    class Meta:
        verbose_name_plural = 'Blog Profiles'
        verbose_name = 'Blog'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="blog")
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    # def __str__(self):
    #     return self.name

    def get_absolute_url(self):
        return resolve_url('blog_detail', pk=self.id)
