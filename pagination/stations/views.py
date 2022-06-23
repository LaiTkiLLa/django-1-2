from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from pagination.settings import BUS_STATION_CSV
import urllib.parse


def index(request):
    return redirect(reverse('bus_stations'))

with open(BUS_STATION_CSV, encoding='utf-8', newline='') as file:
    reader = csv.DictReader(file)
    bus_stations_list = []
    for row in reader:
        bus_stations_list.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})

def bus_stations(request):

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(bus_stations_list,10)
    page = paginator.get_page(page_number)
    data = page.object_list


    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице


    context = {
        'bus_stations': data,
        'page': page_number,
    }
    return render(request, 'stations/index.html', context)
