# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render


NEW_YORK = [
    'West Village',
    'East Village',
    'SoHo',
    'Dumbo',
    'Upper West Side',
]

SAN_FRANCISCO = [
    'Mission',
    'Marina',
    'Hayes Valley',
    'Potrero Hill',
    'Tenderloin',
    'Civic Center',
]

CITY_SLUGS = [
    ('San Francisco', 'sf'),
    ('New York', 'nyc'),
]

CITIES = {
    'New York': NEW_YORK,
    'San Francisco': SAN_FRANCISCO
}


def slug_to_name(slug):
    for city_tuple in CITY_SLUGS:
        if city_tuple[1] == slug:
            return city_tuple[0]

def index(request):
    context = {'CITY_SLUGS': CITY_SLUGS}
    return render(request, 'index.html', context)

    # return HttpResponse("Hello, world. You're at the index.")

def compare(request, city1, city2):
    context = {
        'CITY_SLUGS': CITY_SLUGS,
        'city1': slug_to_name(city1),
        'city2': slug_to_name(city2)
    }
    return render(request, 'compare.html', context)








