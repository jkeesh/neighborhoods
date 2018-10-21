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
    'Alphabet City',
    'Astoria',
    'Bedford-Stuyvesant',
    'Brooklyn',
    'Bushwick',
    'Central Park West',
    'Central Park',
    'Chelsea',
    'Chinatown',
    'Clinton Hill',
    'Dumbo',
    'East Village',
    'Financial District',
    'Flatiron',
    'Flushing',
    'Gramarcy Park',
    'Greenwich Village',
    'Harlem',
    'Hell\'s Kitchen',
    'Jamaica',
    'Kips Bay',
    'Little Italy',
    'Long Island',
    'Lower East Side',
    'Meatpacking District',
    'Midtown East',
    'Murray Hill',
    'Nolita',
    'Princeton',
    'Soho',
    'Theater District',
    'Times Square',
    'Tribeca',
    'Union Square',
    'Upper East Side',
    'Upper West Side',
    'Washington Heights',
    'West Village',
    'Westchester',
    'Williamsburg',
]

SAN_FRANCISCO = [
    'Berkeley',
    'Bernal Heights',
    'Castro',
    'Dogpatch',
    'Financial District',
    'Fishermans Wharf',
    'Golden Gate Park',
    'Haight Ashbury',
    'Hayes Valley',
    'Lower Haight',
    'Marina',
    'Mission',
    'Mountain View',
    'Nob Hill',
    'Noe Valley',
    'North Beach',
    'Oakland',
    'Pac Heights',
    'Palo Alto',
    'Potrero',
    'Presidio',
    'Richmond',
    'Russian Hill',
    'SOMA',
    'Sunset',
    'Union Square',
]

WASHINGTON_DC = [
    'Adam\'s Morgan',
    'Bethesda',
    'Clarendon',
    'Cleveland Park',
    'Columbia Heights',
    'Dupont Circle',
    'Fairfax',
    'Farragut Square',
    'Federal Triangle',
    'Foggy Bottom',
    'Georgetown',
    'Glover Park',
    'H Street',
    'K Street/Chinatown',
    'Logan Circle',
    'Metro Center',
    'National Mall',
    'Navy Yard',
    'NoMa',
    'Shaw',
    'Tacoma Park',
    'Tacoma Park',
    'Tenleytown',
    'U Street',
    'White House',
    'Woodley Park',
]

CHICAGO = [
    'Boystown',
    'Bucktown',
    'Chinatown',
    'Evanston',
    'Gold Coast',
    'Grant Park',
    'Hyde Park',
    'Lake Forest',
    'Lakeview',
    'Lincoln Park',
    'Lincoln Square',
    'Logan Square',
    'Magnificent Mile',
    'Millenium Park',
    'Near North Side',
    'Old Town',
    'River North',
    'Rogers Park',
    'Streeterville',
    'The Loop',
    'Ukrainian Village',
    'University Village',
    'Uptown',
    'West Loop',
    'Wicker Park',
    'Wilmette',
]

LOS_ANGELES = [
    'Bel-Air',
    'Brentwood',
    'Echo Park',
    'Hollywood',
    'Koreatown',
    'Los Feliz',
    'Marina del Rey',
    'Silver Lake',
    'Venice',
    'Westwood',
]

DENVER = [
    'Aurora',
    'Boulder',
    'Broomfield',
    'Cap Hill',
    'Cheesman Park',
    'Cherry Creek',
    'Cherry Hills',
    'City Park',
    'Congress Park',
    'Country Club',
    'Glendale',
    'Golden',
    'Golden Triangle',
    'Hilltop',
    'Lakewood',
    'LoDo',
    'LoHi',
    'Lowry',
    'Park Hill',
    'Platt Park',
    'RiNo',
    'Sloan Lake',
    'Stapleton',
    'Sunnyside',
    'Tech Center',
    'Wash Park',
]

SEATTLE = [
    'Bainbridge',
    'Beacon Hill',
    'Ballard',
    'Belltwon',
    'Capitol Hill',
    'Chinatown-International District',
    'Columbia City',
    'Downtown Seattle',
    'Fremont',
    'Pike Place Market',
    'Pioneer Square',
    'Queen Anne',
    'SoDo',
    'South Lake Union',
    'University District',
    'Waterfront',
    'West Seattle',
    'Woodinville',
]

CITY_SLUGS = [
    ('San Francisco', 'sf'),
    ('New York', 'nyc'),
    ('Washington DC', 'dc'),
    ('Chicago', 'chicago'),
    ('Los Angeles', 'la'),
    ('Denver', 'denver'),
    ('Seattle', 'seattle'),
]

CITIES = {
    'New York': NEW_YORK,
    'San Francisco': SAN_FRANCISCO,
    'Washington DC': WASHINGTON_DC,
    'Chicago': CHICAGO,
    'Los Angeles': LOS_ANGELES,
    'Denver': DENVER,
    'Seattle': SEATTLE,
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
        if key == "username":
            continue

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




