from django.core.management.base import BaseCommand
from tqdm import tqdm
import csv
import codecs
import time
from labeling.models import MyModelFirst  # Замените на фактический путь к вашей модели

class Command(BaseCommand):
    help = 'Import data from CSV file into database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        with codecs.open(csv_file, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            next(csv_reader)
            total_rows = sum(1 for row in csv_reader)  # Получаем общее количество строк в CSV
            file.seek(0)  # Возвращаем указатель в начало файла
            next(csv_reader)  # Пропускаем заголовок
            for row in tqdm(csv_reader, total=total_rows, desc="Импорт данных"):
                # Заменяем пустые строки на None для полей, ожидающих числовые значения
                for key in row.keys():
                    if row[key] == '':
                        row[key] = None
                MyModelFirst.objects.create(**row)

        self.stdout.write(self.style.SUCCESS("Данные успешно добавлены!"))
