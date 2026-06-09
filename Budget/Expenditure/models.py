from django.db import models

# Create your models here.
class Items (models.Model): #this is the table that has the items(that money is spent on) and their ids 
    Category = models.CharField(unique=False, max_length=10) #Django developes a default primary key for each model

class expenditure(models.Model): #this table shows the amount of money spent on each item 
    Item = models.ForeignKey(Items, on_delete=models.CASCADE)
    Spent = models.IntegerField(null=True)
    date = models.DateField(auto_now_add= True, null =True)

class Date(models.Model): #this table is for the day the money was spent
    Item = models.ForeignKey(Items, on_delete=models.CASCADE)
    Date = models.DateField()