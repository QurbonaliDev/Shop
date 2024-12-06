from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField()

class Product(models.Model):
    UZ = 'sum'
    RU = 'rubl'
    EN = 'dollar'

    type_money = (
        (UZ, 'Sum'),
        (RU, 'Rubl'),
        (EN, 'Dollar'),
    )

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    type = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField()
    price_type = models.CharField(
        max_length=10,  # CharField ishlatiladi
        choices=type_money,
        default=UZ,
    )
    price = models.PositiveIntegerField()
    image = models.ImageField()
