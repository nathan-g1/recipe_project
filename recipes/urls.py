# recipes/urls.py

from django.urls import path
from .views import (
    RecipeListCreateView,
    RecipeFetchView,
    RecipeUpdateView,
    RecipeDeleteView
)

urlpatterns = [
    path('recipes/', RecipeListCreateView.as_view(), name='recipe-list-create'),
    path('recipes/<int:pk>/', RecipeFetchView.as_view(), name='recipe-get'),
    path('recipes/<int:pk>/update/', RecipeUpdateView.as_view(), name='recipe-update'),
    path('recipes/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe-delete'),
]
