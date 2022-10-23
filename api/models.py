from django.db import models

# Create your models here.


class Location(models.Model):
    locationName = models.CharField(max_length=100, unique=True)

    # When in admin panel will show name rather than ID
    def __str__(self):
        return self.locationName


# Many to one relationship = ForeignKey
# A location can have many items

class Item(models.Model):
    itemName = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)
    itemLocation = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.itemName

