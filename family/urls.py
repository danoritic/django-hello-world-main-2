# example/urls.py
from django.urls import path

from family.views import family_view


urlpatterns = [
    path('family', family_view),
]