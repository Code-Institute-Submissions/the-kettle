from django.db import models

# Create your models here.

# Product model


class Product(models.Model):

    name = models.CharField(max_length=254, default='')
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    flavour = models.ForeignKey('Flavour', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='static/img')
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name


# Category model

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name



# Flavour model

class Flavour(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name



