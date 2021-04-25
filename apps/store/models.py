from django.db import models
from django.shortcuts import reverse
from io import BytesIO
from django.core.files import File
from PIL import Image

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, SmartResize

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
        return reverse('category_detail', kwargs={'slug': self.slug})

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
    in_stock = models.BooleanField(verbose_name="В наличии", default=True)
    manufacturer = models.CharField(verbose_name="Производитель", max_length=100, blank=True, null=True)

    class Meta:
        ordering = ('-date_added', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"category_slug": self.category.slug, 'slug': self.slug})

    def get_main_image(self):
        try:
            product_galery_list = self.images.all()
            return product_galery_list[0].thumbnail
            # for product_galery in product_galery_list:
            #     if product_galery.is_main:
            #         return product_galery.thumbnail
        except:
            return ''

    def get_image_gallery(self):
        try:
            return self.images.all()
        except: 
            return []


class ProductGalery(models.Model):
    product = models.ForeignKey(Product, verbose_name="Товар", on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(verbose_name='Изображение', upload_to='media')
    thumbnail = ImageSpecField(source="image", processors=[ResizeToFill(200,200)])
    medium_image = ImageSpecField(source='image', processors=[ResizeToFill(500,500)])
    is_main = models.BooleanField(verbose_name="Главное изображение", default=False)