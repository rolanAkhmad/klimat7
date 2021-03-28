from django.db import models
from io import BytesIO
from django.core.files import File
from PIL import Image

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('ordering',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/%s/' % (self.slug)

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    detail_description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    is_featured = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="media/uploads/", blank=True, null=True)

    class Meta:
        ordering = ('-date_added', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s/%s/' % (self.category.slug, self.slug)
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/uploads/", blank=True, null=True)



