from django.urls import path

from food.views import FoodListView, CreateFoodView, UpdateFoodView, DeleteFoodView, RecipeListView, \
    CreateRecipeView, UpdateRecipeView, DeleteRecipeView, FoodDetailView, RecipeDetailView
from nutrition.views import ContactView, HomeView


urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('food/', FoodListView.as_view(), name='food'),
    path('food/<int:pk>/', FoodDetailView.as_view(), name='food_detail'),
    path('food/create/', CreateFoodView.as_view(), name='food_create'),
    path('food/update/<int:pk>/', UpdateFoodView.as_view(), name='food_update'),
    path('food/delete/<int:pk>/', DeleteFoodView.as_view(), name='food_delete'),
    path('recipe/', RecipeListView.as_view(), name='recipes'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/create/', CreateRecipeView.as_view(), name='recipe_create'),
    path('recipe/update/<int:pk>/', UpdateRecipeView.as_view(), name='recipe_update'),
    path('recipe/delete/<int:pk>/', DeleteRecipeView.as_view(), name='recipe_delete'),
    path('contact/', ContactView.as_view(), name='contact_view')
)
