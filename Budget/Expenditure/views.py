from django.shortcuts import render, get_object_or_404
from .models import Items
from django.views.generic.edit import DeleteView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ItemsSerializer, DateSerializer, ExpenditureSerializer
from rest_framework import viewsets

class ItemsView(APIView): # This view is used to create and list out items in the budget.
    
    def post(self, request): 
        serializer = ItemsSerializer(data = request.data) #This is what is used to capture the information from the request
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"Detail": "Item added successfully."})
    
    def get(self, request): #This view overides the get method to implement custom logic for listing items.
        queryset = Items.objects.all()
        serializer = ItemsSerializer(queryset, many= True)
        
        return Response(serializer.data)
    

class ManageItemsView(viewsets.ModelViewSet): #This view is class bass view that carries out the CRUD operations 
    queryset = Items
    serializer_class = ItemsSerializer
    #Fix the error of 'ModelBase object is not iterable's
    
