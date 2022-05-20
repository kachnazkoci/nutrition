from django.urls import path
from user.views import UserListView, DeleteUserView, UserDetailView, CreateUserView, UpdateUserView
from nutrition.views import ContactView, HomeView


urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('users/', UserListView.as_view(), name='users'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('contact/', ContactView.as_view(), name='contact_view'),
    path('user/create/', CreateUserView.as_view(), name='create_user'),
    path('user/update/<int:pk>/', UpdateUserView.as_view(), name='update_user'),
    path('user/delete/<int:pk>/', DeleteUserView.as_view(), name='delete_user')
)
