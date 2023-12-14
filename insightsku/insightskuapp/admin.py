from django.contrib import admin
from .models import Client, UserProfile, Product, Content, ReturnsData

admin.site.register(Client)
admin.site.register(UserProfile)
admin.site.register(Product)
admin.site.register(Content)
admin.site.register(ReturnsData)
