from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=20, default='+0123456789')
    email = models.EmailField(max_length=70, unique=True)
    user_description = models.TextField(max_length=9000)
    user_image = models.ImageField(upload_to='profile_picture/', default='profile_picture/no_image.jpg')
    profile = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'User'

class Portfolio(models.Model):
    text = models.CharField(max_length=20)
    image = models.ImageField(upload_to='portfolio_picture/', default='portfolio_picture/no_image.jpg')
    category = models.CharField(max_length=20)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Portfolio'

class Contact(models.Model):
    description = models.TextField(max_length=9000)
    address = models.CharField(max_length=2000)
    phone_number = models.CharField(max_length=20, default='+0123456789')
    email = models.EmailField(max_length=70, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name_plural = 'Contact'