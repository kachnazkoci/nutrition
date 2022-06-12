from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from food.cal_counter_user import basal_metabolic_rate, activity_calorie_input, ideal_calories_intake
from user.check import calcul_age
from user.views import UserDetailView

from .forms import FoodForm, RecipeForm, BlogForm
from .models import Food, Recipe, Blog, Plate, User


#########################################
#####              FOOD             #####
#########################################
# def food_list_view(request):
#     users = Food.objects.all()
#     context = {
#         'users': users
#     }
#     return render(request, 'food.html', context)


# def user_search_view(request):
#     context = {}
#     return render(request, 'search/search_user.html',
#                   context=context)


class FoodListView(ListView):
    model = Food
    template_name = 'food.html'
    extra_context = {'page_name': 'Food'}

    def get_queryset(self):
        return Food.objects.order_by('name')


class FoodDetailView(DetailView):
    model = Food
    template_name = 'food_detail.html'
    extra_context = {'page_name': Food.name}

    def get_context_data(self, **kwargs):
        context = super(FoodDetailView, self).get_context_data(**kwargs)
        context.update({'page_name': self.object.name})
        return context


class CreateFoodView(CreateView):
    template_name = 'food_create.html'
    form_class = FoodForm
    model = Food
    extra_context = {'page_name': 'Add FOOD'}


class UpdateFoodView(UpdateView):
    template_name = 'food_update.html'
    form_class = FoodForm
    model = Food
    extra_context = {'page_name': 'Food'}


class DeleteFoodView(DeleteView):
    template_name = 'food_delete.html'
    model = Food
    success_url = reverse_lazy('food')
    extra_context = {'page_name': 'Food'}


#########################################
#####            PLATE              #####
#########################################


def calories_intake(user):
    user_height = user.height
    user_weight = user.weight
    user_gender = user.gender
    user_age = user.get_age()
    user_activity = user.activity
    user_target = user.target
    bmr = basal_metabolic_rate(user_gender, user_height, user_weight, user_age)
    aci = activity_calorie_input(bmr, user_activity)
    return ideal_calories_intake(aci, user_target)


def index(request):
    # user = request.user
    user = User.objects.first()
    if request.method == 'POST':
        food_name = request.POST['food_consumed']
        quantity = int(request.POST['quantity'])
        food = Food.objects.get(name=food_name)  # out of food object it will take food as an object
        plate = Plate(user=User.objects.get(id=user.id), quantity=quantity, food_consumed=food)
        plate.save()
    foods = Food.objects.order_by('name').all()
    plates = Plate.objects.filter(user=request.user.id)
    total_kcal = 0
    total_protein = 0
    total_fats = 0
    total_carbs = 0
    for plate in plates:
        plate.kcal_amount = round(plate.food_consumed.kcal * plate.quantity)
        total_kcal += plate.kcal_amount
        plate.protein_amount = round(plate.food_consumed.protein * plate.quantity)
        total_protein += plate.protein_amount
        plate.fats_amount = round(plate.food_consumed.fats * plate.quantity)
        total_fats += plate.fats_amount
        plate.carbs_amount = round(plate.food_consumed.carbs * plate.quantity)
        total_carbs += plate.carbs_amount
    return render(request, 'plate.html',
                  {'foods': foods, 'plates': plates, 'ideal_calories_intake': calories_intake(user),
                   'total_kcal': total_kcal, 'total_carbs': total_carbs, 'total_fats': total_fats,
                   'total_protein': total_protein}, )


def delete_consumed_food(request, id):
    consumed_food = Plate.objects.get(id=id)
    if request.method == "POST":
        consumed_food.delete()
        return redirect('/food/plate')
    return render(request, 'delete_from_plate.html')


# class CreatePlateView(CreateView):
#     template_name = 'plate.html'
#     form_class = PlateForm
#     model = Plate
#     extra_context = {'page_name': 'Create plate'}


#########################################
#####            RECIPES            #####
#########################################
class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes.html'
    extra_context = {'page_name': 'Recipes'}


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
    extra_context = {'page_name': Recipe.name}

    def get_context_data(self, **kwargs):
        context = super(RecipeDetailView, self).get_context_data(**kwargs)
        context.update({'page_name': self.object.name})
        return context


class CreateRecipeView(CreateView):
    template_name = 'recipe_create.html'
    form_class = RecipeForm
    model = Recipe
    extra_context = {'page_name': 'Add RECIPE'}


class UpdateRecipeView(UpdateView):
    template_name = 'recipe_update.html'
    form_class = RecipeForm
    model = Recipe
    extra_context = {'page_name': Recipe}


class DeleteRecipeView(DeleteView):
    template_name = 'recipe_delete.html'
    model = Recipe
    success_url = reverse_lazy('recipes')
    extra_context = {'page_name': Recipe}


#########################################
#####              BLOG             #####
#########################################
class BlogView(generic.ListView):
    model = Blog
    template_name = "blog.html"
    # paginate_by = 10
    extra_context = {'page_name': 'Blog'}

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog_detail.html"


class CreateBlogView(CreateView):
    template_name = 'blog_create.html'
    form_class = BlogForm
    model = Blog
    extra_context = {'page_name': 'Add BLOG Post'}


class DeleteBlogView(DeleteView):
    template_name = 'blog_delete.html'
    model = Blog
    success_url = reverse_lazy('blog')
    extra_context = {'page_name': Blog}


class UpdateBlogView(UpdateView):
    template_name = 'blog_update.html'
    form_class = BlogForm
    model = Blog
    extra_context = {'page_name': Blog}
