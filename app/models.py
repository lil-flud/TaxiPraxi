from django.db import models

# Create your models here.


class TaxiBusiness(models.Model):
    occupied = models.BooleanField()
    capacity = models.PositiveIntegerField()
    current_passengers = models.PositiveIntegerField()
    fare = models.FloatField()
    taxi_type = models.TextField()
    notes = models.TextField()
    taxi_number = 100
    amt_taxis = 1


def add_taxi(
    occupied, capacity, current_passengers, fare, taxi_type, taxi_number, notes
):
    taxi = TaxiBusiness(
        occupied=occupied,
        capacity=capacity,
        current_passengers=current_passengers,
        fare=fare,
        taxi_type=taxi_type,
        notes=notes,
    )
    taxi.save()
    taxi.taxi_number = taxi.taxi_number + (taxi.id * 11)
    taxi.save()
    return taxi


def start_fare(num_pass):
    unocc_taxis = TaxiBusiness.objects.filter(occupied=False, capacity__gte=num_pass)
    first_avail_taxi = unocc_taxis[0]
    first_avail_taxi.current_passengers += num_pass
    first_avail_taxi.occupied = True
    first_avail_taxi.save()
    return first_avail_taxi


# def add_taxi(
#     occupied, capacity, current_passengers, fare, taxi_type, taxi_number, notes
# ):
#     taxi = TaxiBusiness(
#         occupied=occupied,
#         capacity=capacity,
#         current_passengers=current_passengers,
#         fare=fare,
#         taxi_type=taxi_type,
#         taxi_number=taxi_number,
#         notes=notes,
#     )
#     taxi.save()
#     if len(TaxiBusiness.objects.all()) >= 1:
#         taxi.taxi_number += 11 * len(TaxiBusiness.objects.all())
#         taxi.save()
#         return taxi
#     else:
#         return taxi
