from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from django.conf import settings
from nutrition.views import HomeView, ContactView
from django.conf.urls.static import static

urlpatterns = [
                  path('', HomeView.as_view(), name='home'),
                  path('admin/', admin.site.urls),
                  path('contact/', ContactView.as_view(), name='contact'),
                  path('users/', include('user.urls'), name='users'),
                  path('food/', include('food.urls'), name='food'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
