from django.contrib import admin
from .models import Client, UserProfile, Product, Content, ReturnsData, ProductType, Tag, ImageDetail

admin.site.site_header = 'InsightSKU Admin'
admin.site.register(Client)
admin.site.register(UserProfile)
admin.site.register(Product)
admin.site.register(Content)
admin.site.register(ReturnsData)
admin.site.register(ProductType)
admin.site.register(Tag)
admin.site.register(ImageDetail)


