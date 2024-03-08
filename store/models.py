from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class ItemImage(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to="store/images")

    def __str__(self):
        return self.item.name
