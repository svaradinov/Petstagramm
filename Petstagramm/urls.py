from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Petstagramm.common.urls')),
    path('pets/', include('Petstagramm.pets.urls')),
]
