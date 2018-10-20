# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

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


CITIES = {
    'New York': NEW_YORK,
    'San Francisco': SAN_FRANCISCO
}



def index(request):
    return HttpResponse("Hello, world. You're at the index.")
