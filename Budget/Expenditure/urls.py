from django.urls import path, include
from .views import ItemsView, ManageItemsView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('items',ManageItemsView, basename='items' ) #This statement registers the view and all its urls for CRUD operations into the router

urlpatterns = [
    path("items/", ItemsView.as_view()),#This is the structure of the url for a class based view
    path("manage_items/<int:pk>/", include(router.urls)) #This is the url to the router and its view. 
]