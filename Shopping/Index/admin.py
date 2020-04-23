from django.contrib import admin
from django.contrib.auth.models import Permission
from django.utils.safestring import mark_safe
from Index.models import Product,Product_type,Review,Order_product
from Profile.models import My_User,Financial_detail,Payment,Promotion,Order
# Register your models here.

admin.site.register(Product)
admin.site.register(Product_type)
admin.site.register(My_User)
admin.site.register(Financial_detail)
admin.site.register(Payment)
admin.site.register(Promotion)
admin.site.register(Order)
admin.site.register(Review)

admin.site.register(Order_product)

