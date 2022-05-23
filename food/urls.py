from django.urls import path, re_path

from food.views import FoodListView, CreateFoodView, UpdateFoodView, DeleteFoodView, RecipeListView, \
    CreateRecipeView, UpdateRecipeView, DeleteRecipeView, FoodDetailView, RecipeDetailView, BlogView, BlogDetailView, \
    CreateBlogView, DeleteBlogView, UpdateBlogView
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
    path('blog/', BlogView.as_view(), name="blog"),
    path('blog/create/', CreateBlogView.as_view(), name='blog_create'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name="blog_detail"),
    path('blog/delete/<int:pk>/', DeleteBlogView.as_view(), name='blog_delete'),
    path('blog/update/<int:pk>/', UpdateBlogView.as_view(), name='blog_update'),
    path('contact/', ContactView.as_view(), name='contact_view')
)
