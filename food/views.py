from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import FoodForm, RecipeForm, BlogForm
from .models import Food, Recipe, Blog


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
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = "blog_detail.html"


class CreateBlogView(CreateView):
    template_name = 'blog_create.html'
    form_class = BlogForm
    model = Blog
    extra_context = {'page_name': 'Add BLOG Post'}