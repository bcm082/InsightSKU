from django.contrib.auth.models import User
from django.db import models

class Client(models.Model):
    client_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=40)
    asin = models.CharField(max_length=40, blank=True)
    title = models.CharField(max_length=255)
    main_image = models.URLField()
    images_url = models.URLField()
    videos_url = models.URLField()
    a_plus_content_url = models.URLField()
    tags = models.ManyToManyField(Tag, blank=True)
    notes = models.TextField(blank=True)
    date_listed = models.DateTimeField(null=True, blank=True)  # Automatically sets the date when the product is created

    def __str__(self):
        return self.title