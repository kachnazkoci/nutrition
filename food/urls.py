from django.urls import path

from food.views import FoodListView, FoodDetailView, CreateFoodView, UpdateFoodView, DeleteFoodView
from user.views import UserListView, DeleteUserView, UserDetailView, CreateUserView, UpdateUserView
from nutrition.views import ContactView, HomeView


urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('food/', FoodListView.as_view(), name='food'),
    path('food/<int:pk>/', FoodDetailView.as_view(), name='food_detail'),
    path('contact/', ContactView.as_view(), name='contact_view'),
    path('food/create/', CreateFoodView.as_view(), name='create_food'),
    path('food/update/<int:pk>/', UpdateFoodView.as_view(), name='update_food'),
    path('food/delete/<int:pk>/', DeleteFoodView.as_view(), name='delete_food')
)
