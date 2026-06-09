from django.urls import path, include
from .views import ItemsView, ManageItemsView, ExpenditureView, ManageExpeditureView, frontend
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router2 = DefaultRouter()

router.register('items',ManageItemsView, basename='items' ) #This statement registers the view and all its urls for CRUD operations into the router
router2.register('spent', ManageExpeditureView, basename = 'spent')

urlpatterns = [
    path("items/", ItemsView.as_view()),#This is the structure of the url for a class based view
    path('manage_items/', include(router.urls)), #This is the url to the router and its view. 
    path('Expenditure/', ExpenditureView.as_view()), #This is the view used to display and post money spent 
    path('manage_spent/', include(router2.urls)), #This view deletes, updates and retrieves specific expenditures
    path('', frontend)
]