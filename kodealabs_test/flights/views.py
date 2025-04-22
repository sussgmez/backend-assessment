from django.shortcuts import render
from django.views.generic import View, ListView
from .models import Itinerarie, Leg
import requests


class FetchFlights(View):
    def get(self, request):
        try: 
            response = requests.get('https://raw.githubusercontent.com/Skyscanner/full-stack-recruitment-test/main/public/flights.json')
            data = response.json()

            for l in data['legs']:
                leg = Leg.objects.get_or_create(
                    id = l['id'],
                    departure_airport = l['departure_airport'],
                    arrival_airport = l['arrival_airport'],
                    departure_time = l['departure_time'],
                    arrival_time = l['arrival_time'],
                    stops = l['stops'],
                    airline_name = l['airline_name'],
                    airline_id = l['airline_id'],
                    duration_mins = l['duration_mins'],
                )
           
            
            for i in data['itineraries']:
                itinerarie = Itinerarie.objects.get_or_create(
                    id = i['id'],
                    price = i['price'].split('£')[1],
                    agent = i['agent'],
                    agent_rating = i['agent_rating'],
                )

                for leg in list(i['legs']):
                    itinerarie[0].legs.add(Leg.objects.get(id=leg))
                    itinerarie[0].save()

        except:
            return render(request, 'flights/error.html')

        return render(request, 'flights/success.html')


class ItinerariesListView(ListView):
    model = Itinerarie
    template_name = "flights/itineraries_list.html"

    def get_queryset(self):
        itineraries = Itinerarie.objects.all()
        try:
            price = self.request.GET['price']
            itineraries = itineraries.filter(price__lte=price)
        except: pass
        try:
            rating = self.request.GET['rating']
            itineraries = itineraries.filter(agent_rating__gte=rating)
        except: pass

        return itineraries
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            price = self.request.GET['price']
            context["price"] = price
        except: pass
        try:
            rating = self.request.GET['rating']
            context["rating"] = rating
        except: pass

        return context
    

class LegListView(ListView):
    model = Leg
    template_name = "flights/leg_list.html"

    def get_queryset(self):
        legs = Leg.objects.all()
        try:
            airline_name = self.request.GET['airline_name']
            legs = legs.filter(airline_name__contains=airline_name)
        except: pass

        return legs
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            airline_name = self.request.GET['airline_name']
            context["airline_name"] = airline_name
        except: pass

        return context
    