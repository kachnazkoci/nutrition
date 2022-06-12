from django.core.management.base import BaseCommand

import food
from food.models import Food
import csv


class Command(BaseCommand):
    help = 'Adds food to the database from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('food.csv', type=str)

    def handle(self, *args, **options):
        filename = options["food.csv"]
        with open('nutrition/management/food.csv', newline="") as f:
            r = csv.reader(f)
            next(r, None)
            food = []
            for row in r:
                food.append(Food(name=row[0], created='2022-06-01', kcal=row[1], carbs=row[2], protein=row[3],
                                 fats=row[4]))
        print(len(Food.objects.bulk_create(food)))
