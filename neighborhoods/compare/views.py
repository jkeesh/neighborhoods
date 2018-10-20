# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

from .models import CityComparison

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

def name_to_slug(name):
    for city_tuple in CITY_SLUGS:
        if city_tuple[0] == name:
            return city_tuple[1]

def index(request):
    context = {'CITY_SLUGS': CITY_SLUGS}
    return render(request, 'index.html', context)

    # return HttpResponse("Hello, world. You're at the index.")

def compare(request, city1, city2):
    context = {
        'CITY_SLUGS': CITY_SLUGS,
        'START_NEIGHBORHOODS': CITIES[slug_to_name(city1)],
        'END_NEIGHBORHOODS': CITIES[slug_to_name(city2)],
        'city1': slug_to_name(city1),
        'city2': slug_to_name(city2)
    }
    return render(request, 'compare.html', context)

def save(request):

    print request.GET


    request.GET = request.GET.copy()

    start_city = request.GET['startCity']
    end_city = request.GET['endCity']

    request.GET.pop('startCity', None)
    request.GET.pop('endCity', None)

    print request.GET

    # start_city = models.CharField(max_length=200)
    # neighborhood1 = models.CharField(max_length=200)

    # end_city = models.CharField(max_length=200)
    # neighborhood2 = models.CharField(max_length=200)

    # timestamp = models.DateTimeField(auto_now_add=True)
    # username = models.CharField(max_length=200, default='')

    for key, value in request.GET.iteritems():
        print "%s %s" % (key, value)

        new_comparison = CityComparison(
            start_city=start_city,
            end_city=end_city,
            neighborhood1=key,
            neighborhood2=value,
            username='jkeeshauto'
        )
        new_comparison.save()

    context = {
        'CITY_SLUGS': CITY_SLUGS,
        # 'START_NEIGHBORHOODS': CITIES[slug_to_name(city1)],
        # 'END_NEIGHBORHOODS': CITIES[slug_to_name(city2)],
        # 'city1': slug_to_name(city1),
        # 'city2': slug_to_name(city2)
    }

    return redirect('/view/' + name_to_slug(start_city) + '/' + name_to_slug(end_city))


    # return render(request, 'compare.html', context)





