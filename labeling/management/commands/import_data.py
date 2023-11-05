import csv
import codecs
from django.core.management.base import BaseCommand
from labeling.models import MyModelFirst

class Command(BaseCommand):
    help = 'Import data from CSV file into database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        with codecs.open(csv_file, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            next(csv_reader)
            for row in csv_reader:
                # Заменяем пустые строки на None для полей, ожидающих числовые значения
                for key in row.keys():
                    if row[key] == '':
                        row[key] = None
                MyModelFirst.objects.create(**row)
