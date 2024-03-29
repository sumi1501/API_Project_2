from django.db import models

# Create your models here.
class Productcatogury(models.Model):
    prod_id=models.IntegerField()
    prod_name=models.IntegerField()

    def __str__(self):
        return self.prod_name

class Product(models.Model):
    prod_id=models.ForeignKey(Productcatogury,on_delete=models.CASCADE)
    product_id=models.IntegerField()
    product_name=models.CharField(max_length=100)
    product_prize=models.IntegerField()