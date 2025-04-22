from django.db import models
from django.utils.translation import gettext_lazy as _  


class Leg(models.Model):
    id = models.CharField(_("id"), max_length=10, primary_key=True)
    departure_airport = models.CharField(_("Departure airport"), max_length=3)
    arrival_airport = models.CharField(_("Arrival airport"), max_length=3)
    departure_time = models.DateTimeField(_("Departure time"))
    arrival_time = models.DateTimeField(_("Arrival time"))
    stops = models.IntegerField(_("Stops"))
    airline_name = models.CharField(_("Airline name"), max_length=50)
    airline_id = models.CharField(_("Airline ID"), max_length=2)
    duration_mins = models.IntegerField(_("Duration mins"))


class Itinerarie(models.Model):
    id = models.CharField(_("id"), max_length=10, primary_key=True)
    legs = models.ManyToManyField(Leg, verbose_name=_("Legs"))
    price = models.FloatField(_("Price"))
    agent = models.CharField(_("Agent"), max_length=50)
    agent_rating = models.FloatField(_("Agent rating"))
