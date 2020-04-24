from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django_countries.fields import CountryField


class Product_type (models.Model):
    name = models.CharField(max_length=255)
    
    desc = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class Product (models.Model):
    is_hide = models.BooleanField(default=False)
    name = models.CharField(max_length=255)

    desc = models.TextField(null=True, blank=True)
    stock = models.IntegerField()
    discount_price = models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    picture_url = models.ImageField()
    product_type_id = models.ForeignKey(Product_type, on_delete=models.CASCADE)
    sale_user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s (%s) %sชิ้น' % (self.name, self.product_type_id,self.stock)

    def product_type(self):
        return ",".join(str(seg)for seg in self.product_type_id)
        
    def get_absolute_url(self):
        return reverse("product_detail", kwargs={
            'product_id': self.id
        })

    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={
            'product_id': self.id  
        })
    
    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart", kwargs={
            'product_id': self.id  
        })


    def get_cat_list(self):
        k = self.product_type_id # for now ignore this instance method
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]

    

class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    create_by = models.CharField(max_length=255)
    create_date = models.DateField(auto_now=False, auto_now_add=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return '(%s) %s' % (self.create_by, self.text)


class Order_products(models.Model):
   
    quantity = models.IntegerField(default=1)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    user= models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    def __str__(self):
        return '%s  %sชิ้น' % (self.product_id.name, self.quantity)

    def get_total_product_price(self):
        return self.quantity * self.product_id.price

    def get_total_discount_product_price(self):
        return self.quantity * self.product_id.discount_price

    def get_amount_saved(self):
        return self.get_total_product_price () - self.get_total_discount_product_price()
        
    def get_final_price(self):
        if self.product_id.discount_price:
            return self.get_total_discount_product_price()
        return self.get_total_product_price()

class Address(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100,null=True, blank=True)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    default = models.BooleanField(default=False,blank=True)
    Option = (
    ('S', 'Stripe'),
    ('P', 'PayPal')
    )
    payment_option = models.CharField(null=True, max_length=1,
        default=None, choices=Option)

    def __str__(self):
        return self.user.username