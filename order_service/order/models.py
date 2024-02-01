# order_service/order/models.py
from django.db import models

        
        
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.username

    
class Product(models.Model):
    product_id = models.IntegerField()
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    
class Order(models.Model):
    user_email = models.ForeignKey(User, models.CASCADE )
    product_name = models.ForeignKey(Product, models.CASCADE )
    # quantity = models.PositiveIntegerField()
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    # total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # def calculate_total_price(self):
    #     # Calculate total price based on quantity and price
    #     self.total_price = self.quantity * self.price
    #     return self.total_price

    # def save(self, *args, **kwargs):
    #     # Calculate total price before saving the object
    #     self.calculate_total_price()
    #     super().save(*args, **kwargs)
        
    # def __str__(self):
    #     return f"{self.product_name}{self.user_email}"
        
        
    