import csv
from unicodedata import name


# python3 manage.py runscript s_load

from gview.models import Person


def run():
    fhand = open('data/load.csv')
    reader = csv.reader(fhand)
    next(reader)  

    Person.objects.all().delete()

    for row in reader:
        print(row)

        p = Person(name = row[0], gender = row[1], birthdate = row[2])
        p.save()