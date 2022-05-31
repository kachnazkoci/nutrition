from django.core.management.base import BaseCommand

import food
from food.models import Food
import csv


class Command(BaseCommand):
    help = 'Adds food to the database from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)

    def handle(self, *args, **options):
        filename = options["filename"]
        with open(filename, newline="") as f:
            r = csv.reader(f)
            animals = []
            for row in r:
                food.append(Food(name=row[0], kcal=row[1], protein=row[2]), fats=row[3], carbs=row[4])
        print(len(Food.objects.bulk_create(food)))
