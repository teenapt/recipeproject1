from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets

from recipe.serializers import RecipeSerializer

from recipe.models import Recipe

from recipe.serializers import UserSerializer

from recipe.models import RatingAndReview

from recipe.serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

class Recipedetails(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class Reviewrating(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = RatingAndReview.objects.all()
    serializer_class = ReviewSerializer

class CreateUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class search(APIView):
    def get(self,request):
        query=self.request.query_params.get('search')   #{paramas:{'search':'carrot'}} #default key search
        if (query):
            recipe=Recipe.objects.filter(Q(name__icontains=query) | Q(ingredients__icontains=query))
            serialized_recipe=RecipeSerializer(recipe,many=True)
            return Response(serialized_recipe.data)
        else:
            return Response([])