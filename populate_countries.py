import csv

import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flag_challenge.settings')

import django
django.setup()
from names.models import Country

def add_country(name_es, name_en, name_fr, iso2, iso3):
    c = Country.objects.get_or_create(iso2=iso2, iso3=iso3, name_es=name_es, name_en=name_en, name_fr=name_fr)[0]
    return c

def populate():
    countries = []
    with open("countries.csv", "r") as f:
        reader = csv.reader(f)
        countries = list(reader)
    for c in countries:
        add_country(c[0], c[1], c[2], c[3], c[4])    
    for c in Country.objects.all():
        print('Added: ' + str(c))

if __name__ == '__main__':
    print("Starting country population script...")
    populate()
    