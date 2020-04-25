from django.contrib import admin
from django.contrib.auth.models import Permission
from django.utils.safestring import mark_safe
from Index.models import Product,Product_type,Review,Order_products,Address,Promotion
from Profile.models import My_User,Financial_detail,Payment,Order
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered','status']
admin.site.register(Product)
admin.site.register(Product_type)
admin.site.register(My_User)
admin.site.register(Financial_detail)
admin.site.register(Payment)
admin.site.register(Promotion)
admin.site.register(Order,OrderAdmin)
admin.site.register(Review)
admin.site.register(Address)

admin.site.register(Order_products)

