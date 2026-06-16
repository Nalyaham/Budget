from rest_framework import serializers
from .models import expenditure, Items, Date

class ItemsSerializer(serializers.ModelSerializer): #this is the serializer for the items table
    class Meta:
        model = Items
        fields = ['id', 'Category']

class ExpenditureSerializer(serializers.ModelSerializer): #This is the serializer for the Expenditure 
    Categories = ItemsSerializer(many=True, read_only = True) #This nesting handles the relationship between the models and keeps the models related

    class Meta:
        model = expenditure
        fields = ['id', 'Spent', 'Item', 'Categories', 'date']

class DateSerializer(serializers.ModelSerializer): #This is the serializer for the date of expenditure
    Categories = ItemsSerializer(many=True, read_only = True)

    class Meta:
        model = Date
        fields = ['Item', 'Date', 'Categories']
