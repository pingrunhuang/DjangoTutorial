from django.urls import path
from .views import get_name, contact

urlpatterns = [
    path("name/", view=get_name),
    path("contact/", view=contact),
]