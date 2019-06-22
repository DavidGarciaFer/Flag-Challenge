import csv 
def populate():
    with open("countries.csv", "r") as f:
        reader = csv.reader(f)
        countries = list(reader)
        print(countries)

populate()