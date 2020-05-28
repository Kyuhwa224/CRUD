from django.db import models

class Cafe(models.Model): 
    product_name = models.CharField(max_length=20)
    product_price = models.IntegerField()
    

    


    
