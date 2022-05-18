from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from nutrition.views import HomeView
from user.views import UserListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('user/', UserListView.as_view(), name='users'),
]


urlpatterns += staticfiles_urlpatterns()
