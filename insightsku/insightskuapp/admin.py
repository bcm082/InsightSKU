from django.contrib import admin
from .models import Client, UserProfile, Product, Tag

admin.site.site_header = 'InsightSKU Admin'
admin.site.register(Client)
admin.site.register(UserProfile)
admin.site.register(Product)
admin.site.register(Tag)



