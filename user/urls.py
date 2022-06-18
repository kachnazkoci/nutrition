from django.urls import path, include
from user.views import UserListView, DeleteUserView, UserDetailView, CreateUserView, UpdateUserView
from nutrition.views import ContactView, HomeView

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('users/', UserListView.as_view(), name='users'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('contact/', ContactView.as_view(), name='contact_view'),
    path('user/create/', CreateUserView.as_view(), name='user_create'),
    path('user/update/<int:pk>/', UpdateUserView.as_view(), name='user_update'),
    path('user/delete/<int:pk>/', DeleteUserView.as_view(), name='user_delete'),
)
