from django.db import models

# Create your models here.

class ShopDetail(models.Model):
    shop_name = models.CharField(max_length=40)
    

    def __str__(self):
        return self.shop_name


class SupplierInfo(models.Model):
    supplier_name = models.CharField(max_length=40)
    address = models.CharField(max_length=200)
    shops_detail = models.ManyToManyField(ShopDetail)



   
