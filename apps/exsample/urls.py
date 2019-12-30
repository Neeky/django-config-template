from django.urls import path

from .views import main_view, get_all_person


urlpatterns = [
    path('', main_view),
    path('apis/persons', get_all_person)
]
