from django.db import models
from Profile.models import My_User,Order


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
    price = models.DecimalField(max_digits=8, decimal_places=2)
    product_type_id = models.ForeignKey(Product_type, on_delete=models.CASCADE)
    sale_user_id = models.ForeignKey(My_User, on_delete=models.CASCADE)

    def __str__(self):
        product_type_id = ",".join(str(seg)for seg in self.product_type_id.all())
        return '%s (%s) %s฿ (%s)' % (self.name, product_type_id,self.price,self.stock)

    def product_type(self):
        return ",".join(str(seg)for seg in self.product_type_id.all())

class Product_picture(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    picture_url = models.ImageField(blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.id,self.product_id.name)
    

class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    create_by = models.CharField(max_length=255)
    create_date = models.DateField(auto_now=False, auto_now_add=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_user_id = models.ForeignKey(My_User, on_delete=models.CASCADE)
    def __str__(self):
        return '(%s) %s' % (self.create_by, self.text)

class Order_product(object):
    order_no = models.IntegerField(primary_key = True)
    unit = models.IntegerField()
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)