from django.db import models


class Product(models.Model):
    GENDER_CHOICES = (
        ('men', 'Men'),
        ('women', 'Women'),
    )

    name = models.CharField(max_length=50)
    category = models.CharField(
        max_length=25, choices=GENDER_CHOICES, default="M")
    price = models.IntegerField(default=0)
    size = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)
    # needs to install pillow
    # file will be uploaded to MEDIA_ROOT / uploads
    image = models.ImageField(upload_to='products/', default='defaultImg.png')
    description = models.CharField(max_length=100, blank=True, null=True)
