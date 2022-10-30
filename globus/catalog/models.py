from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    # photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name

# class User(models.Model):
#     name = models.CharField()
#     surname = models.CharField()
#     email = models.EmailField()
#     password = models.CharField()
#     phone = models.CharField()


#class shopping_cart(models.Model)

