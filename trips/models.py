from django.db import models

# Create your models here.
class Continent(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Country(models.Model):
    name = models.CharField(max_length=100)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE,related_name='countries')

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return self.name

class Airport(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='airports')

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name =models.CharField(max_length=100)
    stars = models.IntegerField()
    descriptions = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hotels')

    def __str__(self):
        return self.name

class Trip(models.Model):

    BB = 'Bed & Breakfast'
    HB = 'Half Board'
    FB = 'Full Board'
    AI = 'All Inclusive'
    TYPE_CHOICES = [(t, t) for t in (BB, HB, FB, AI)]

    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='departures')
    from_airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='destinations')
    to_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    to_airpoprt = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    departure_date = models.DateField()
    return_date = models.DateField()
    trip_type = models.CharField(max_length=15, choices=TYPE_CHOICES, default=BB)
    price_adult = models.DecimalField(max_digits=10, decimal_places=2)
    price_child = models.DecimalField(max_digits=10, decimal_places=2)
    promoted = models.BooleanField(default=False)
    available_adults = models.IntegerField()
    available_children = models.IntegerField()
    description = models.TextField()

class TripPurchase(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='purchases')
    buyer_name = models.CharField(max_length=100)
    buyer_email = models.EmailField()
    num_adults = models.IntegerField()
    num_children = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)