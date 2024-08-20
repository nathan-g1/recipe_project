# recipes/views.py

from django.http import HttpResponse
from rest_framework import generics
from .models import Recipe
from .serializers import RecipeSerializer
from datetime import datetime

def home(request):
    current_datetime = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    html = f"""
    <html>
        <body>
            <h1>Welcome to the Recipe Project API</h1>
            <p>Current date: {current_datetime}</p>
            <p><a href="/api/recipes/">Access Recipes API</a></p>
        </body>
    </html>
    """
    return HttpResponse(html)

class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeUpdateView(generics.UpdateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field = 'pk'

class RecipeDeleteView(generics.DestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field = 'pk'
