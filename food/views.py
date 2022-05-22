from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import FoodForm, RecipeForm
from .models import Food, Recipe, BMICounter


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


class BMIcounterView(ListView):
    template_name = 'counter_BMI.html'
    model = BMICounter
    success_url = reverse_lazy('user')
    # extra_context = {'page_name': User}