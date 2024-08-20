# recipes/urls.py

from django.urls import path
from .views import RecipeListCreateView, RecipeUpdateView

urlpatterns = [
    path('recipes/', RecipeListCreateView.as_view(), name='recipe-list-create'),
    path('recipes/<int:pk>/', RecipeUpdateView.as_view(), name='recipe-update'),
]
