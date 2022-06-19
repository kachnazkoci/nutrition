from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from nutrition.views import HomeView, ContactView
from django.conf import settings
from django.conf.urls.static import static

from user.views import LogoutView, SignUp

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('user/registration/login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/registration/register/', SignUp.as_view(), name='register'),
    path('admin/', admin.site.urls),
    path('contact/', ContactView.as_view(), name='contact'),
    path('users/', include('user.urls'), name='users'),
    path('food/', include('food.urls'), name='food'),
 ]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
