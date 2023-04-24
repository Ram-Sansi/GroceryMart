from django.contrib import admin
from Customer.models import *
# Register your models here.
admin.site.register(Cart)
admin.site.register(Bill)
admin.site.register(Billdetail)
admin.site.register(Client)

