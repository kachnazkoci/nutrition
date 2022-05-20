from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from nutrition.views import HomeView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('contact/', ContactView.as_view(), name='contact'),
    path('users/', include('user.urls'), name='users'),
    path('food/', include('food.urls'), name='food'),
]


urlpatterns += staticfiles_urlpatterns()
