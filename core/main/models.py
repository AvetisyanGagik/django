from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField('Category name', max_length=25)


    def __str__(self) -> str:
        return self.name


    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Category_details(models.Model):
    name = models.CharField('Category Details Name', max_length=25)

    def __str__(self) -> str:
        return self.name


    class Meta:
        verbose_name = 'categorydetail'
        verbose_name_plural = 'categorydetails'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name = 'catprod')
    category_detail = models.ForeignKey(Category_details, on_delete=models.CASCADE, related_name = 'detailcat', null = True)
    name = models.CharField('Product name', max_length=25)
    price = models.IntegerField('Product price')
    img = models.ImageField('Product image', upload_to = 'media')



