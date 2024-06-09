from django.contrib import admin
from .models import *
admin.site.register(CUSTOMER)
admin.site.register(BOOK)
admin.site.register(TAG)
admin.site.register(Order)