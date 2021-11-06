from rest_framework import serializers
from .models import categories,meals

class categoriesSerializer(serializers.ModelSerializer):
    strcategory=serializers.CharField(max_length=30)
    strcategorythumb=serializers.URLField(max_length=100)
    strcategorydescribtion=serializers.CharField(max_length=300)
    class Meta:
        model=categories
        fields='__all__'

class mealsSerializer(serializers.ModelSerializer):
    strmeal=serializers.CharField(max_length=100)
    strmealthumb=serializers.URLField(max_length=100)
    idmeal=serializers.IntegerField()
    class Meta:
        model=meals
        fields='__all__'