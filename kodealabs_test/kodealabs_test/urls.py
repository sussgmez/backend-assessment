from django.contrib import admin
from django.urls import path, include
from flights.views import ItinerariesListView, LegListView, FetchFlights

urlpatterns = [
    path('admin/flights/itinerarie/list/', ItinerariesListView.as_view(), name='itinerarie-list'),
    path('admin/flights/leg/list/', LegListView.as_view(), name='leg-list'),
    path('admin/', admin.site.urls),
    path('', FetchFlights.as_view(), name='home'),
]
