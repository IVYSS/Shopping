from django.db import models
from django.contrib.auth.models import User
from Index.models import Order_products,Address


# Create your models here.
class My_User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    age = models.IntegerField()
    Gender = (
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),
    )
    
    gender = models.CharField(max_length=1, choices=Gender)
    def __str__(self):
        return '%s %s (%s)' % (self.user.first_name, self.user.last_name, self.gender)

class Financial_detail(models.Model):
    title = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(auto_now=False, auto_now_add=False)
    Financial_type = (
        ('revenue','revenue'),
        ('expense','expense'),
    )
    financial_type = models.CharField(max_length=8, choices=Financial_type)
    financial_user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Payment(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    upload = models.ImageField(blank=True, null=True)
    Method = (
        ('paypal','paypal'),
        ('creditcard','creditcard'),
        ('truewallet','truewallet')
    )
    method = models.CharField(max_length=10, choices=Method)
    financial_user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Promotion(models.Model):
    name = models.CharField(max_length=255)
    available = models.BooleanField(default=True)
    discount = models.IntegerField()
    
class Order(models.Model):
    date =  models.DateField(auto_now=False, auto_now_add=True)
    delivery_place = models.ForeignKey(Address,on_delete=models.SET_NULL,null=True, blank=True)
    ordered = models.BooleanField(default=False)
    products = models.ManyToManyField(Order_products)
    Status = (
        ('NS','Notyetshipped'),
        ('S','Shipping'),
        ('D','Delivered'),
    )
    status = models.CharField(max_length=2, choices=Status)
    user= models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_products in self.products.all():
            total += order_products.get_final_price()
        return total
 
