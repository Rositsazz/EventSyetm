from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return "{}".format(self.name)


class Place(models.Model):
    name = models.CharField(max_length=128)
    capacity = models.PositiveIntegerField()
    city = models.ForeignKey(City)

    def __str__(self):
        return "{name} in {city}".format(name=self.name, city=self.city)


class Event(models.Model):
    WEDDING = 1
    BALL = 2
    CONFERENCE = 3

    EVENT_TYPE_CHOICES = (
        (WEDDING, 'Wedding'),
        (BALL, 'Ball'),
        (CONFERENCE, 'Conference'),
    )
    start_date = models.DateField()
    end_date = models.DateField()
    capacity = models.PositiveIntegerField()
    place = models.OneToOneField(Place)
    # organiser = models.OneToOneField(Organiser)
    event_type = models.SmallIntegerField(choices=EVENT_TYPE_CHOICES)

    def __str__(self):
        return "{event_type} in {place}, {start_date}".format(
            event_type=self.event_type,
            place=self.place,
            start_date=self.start_date)
