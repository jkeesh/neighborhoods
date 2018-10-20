# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

from collections import Counter

from .models import CityComparison

NEW_YORK = [
    'West Village',
    'Williamsburg',
    'Chelsea',
    'Flatiron',
    'Times Square',
    'Midtown East',
    'Central Park',
    'Financial District',
    'Princeton',
    'Westchester',
    'Long Island',
    'Lower East Side',
    'Upper East Side',
    'Clinton Hill',
    'Dumbo',
    'Gramarcy Park',
    'Tribeca',
    'Union Square',
    'Greenwich Village',
    'Brooklyn',
    'Soho',
    'Kips Bay',
    'Flushing',
    'Alphabet City',
    'Upper West Side',
    'Central Park West',
    'East Village',
]

SAN_FRANCISCO = [
    'Mission',
    'Marina',
    'SOMA',
    'Fishermans Wharf',
    'Russian Hill',
    'Golden Gate Park',
    'Financial District',
    'Berkeley',
    'Palo Alto',
    'Mountain View',
    'Lower Haight',
    'Pac Heights',
    'Potrero',
    'Dogpatch',
    'Nob Hill',
    'Noe Valley',
    'Union Square',
    'North Beach',
    'Oakland',
    'Hayes Valley',
    'Sunset',
    'Richmond',
    'Castro',
    'Bernal Heights',
    'Presidio',
    'Haight Ashbury',
]

WASHINGTON_DC = [
    'Columbia Heights',
    'Georgetown',
    'K Street/Chinatown',
    'White House',
    'H Street',
    'National Mall',
    'Metro Center',
    'Tacoma Park',
    'Bethesda',
    'Fairfax',
    'Adam\'s Morgan',
    'Glover Park',
    'Navy Yard',
    'Federal Triangle',
    'Woodley Park',
    'Foggy Bottom',
    'Farragut Square',
    'Dupont Circle',
    'Clarendon',
    'Logan Circle',
    'NoMa',
    'Tacoma Park',
    'U Street',
    'Tenleytown',
    'Cleveland Park',
    'Shaw',
]

CHICAGO = [
    'Logan Square',
    'Magnificent Mile',
    'West Loop',
    'Millenium Park',
    'River North',
    'Grant Park',
    'The Loop',
    'Evanston',
    'Lake Forest',
    'Wilmette',
    'Wicker Park',
    'Gold Coast',
    'Bucktown',
    'Hyde Park',
    'Lakeview',
    'Old Town',
    'Lincoln Square',
    'Lincoln Park',
    'University Village',
    'Streeterville',
    'Uptown',
    'Chinatown',
    'Boystown',
    'Rogers Park',
    'Near North Side',
    'Ukrainian Village',
]

CITY_SLUGS = [
    ('San Francisco', 'sf'),
    ('New York', 'nyc'),
    ('Washington DC', 'dc'),
    ('Chicago', 'chicago'),
]

CITIES = {
    'New York': NEW_YORK,
    'San Francisco': SAN_FRANCISCO,
    'Washington DC': WASHINGTON_DC,
    'Chicago': CHICAGO,
}

def get_best_match(city1, city2, neighborhood1):
    """Find which neighborhood in city2 matches city1."""

    counter = Counter()

    results = CityComparison.objects.filter(
        start_city=city1, end_city=city2, neighborhood1=neighborhood1)

    for result in results:
        counter[result.neighborhood2] += 1

    top = counter.most_common(10)

    # No result
    if not top:
        return '', ''

    # Return the winner. The 0 index is the city, the 1 index is the count.
    # The third result in the tuple is the Counter object.
    return top[0][0], top[0][1], counter



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

def view(request, city1, city2):
    context = {
        'CITY_SLUGS': CITY_SLUGS,
        'START_NEIGHBORHOODS': CITIES[slug_to_name(city1)],
        'END_NEIGHBORHOODS': CITIES[slug_to_name(city2)],
        'city1': slug_to_name(city1),
        'city2': slug_to_name(city2),
        'city1slug': city1,
        'city2slug': city2,
    }
    return render(request, 'view.html', context)

def save(request):

    request.GET = request.GET.copy()

    start_city = request.GET['startCity']
    end_city = request.GET['endCity']

    username = request.GET['username']

    request.GET.pop('startCity', None)
    request.GET.pop('endCity', None)

    for key, value in request.GET.iteritems():
        print "%s %s" % (key, value)

        new_comparison = CityComparison(
            start_city=start_city,
            end_city=end_city,
            neighborhood1=key,
            neighborhood2=value,
            username=username
        )
        new_comparison.save()

    context = {
        'CITY_SLUGS': CITY_SLUGS,
    }

    return redirect('/view/' + name_to_slug(start_city) + '/' + name_to_slug(end_city))




