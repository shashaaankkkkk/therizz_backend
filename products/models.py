from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    SIZES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Double Extra Large'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    size = models.CharField(max_length=3, choices=SIZES, blank=True)  # Size options
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # Discount percentage
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    cover_photo = models.ImageField(upload_to='products/covers/')
    photo_gallery = models.ImageField(upload_to='products/gallery/', blank=True)

    def __str__(self):
        return self.name
