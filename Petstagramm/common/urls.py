from django.urls import path

from Petstagramm.common.views import landing_page

urlpatterns = [
    path('', landing_page, name='home'),
]