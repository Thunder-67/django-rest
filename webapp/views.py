from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import categories,meals,search
from .serializers import categoriesSerializer,mealsSerializer,searchSerializer

# Create your views here.
class categorylist(APIView):

    def get(self,request):
        category1=categories.objects.all()
        serializer=categoriesSerializer(category1,many=True)
        return Response(serializer.data)

class meallist(APIView):

    def get(self,request):
        meal1=meals.objects.all()
        serializer=mealsSerializer(meal1,many=True)
        return Response(serializer.data)

class searchlist(APIView):

    def get(self,request):
        search1=search.objects.all()
        serializer=searchSerializer(search1,many=True)
        return Response(serializer.data)