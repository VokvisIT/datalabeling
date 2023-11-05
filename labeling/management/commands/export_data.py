import csv
from django.core.management.base import BaseCommand
from labeling.models import MyModelFirst

class Command(BaseCommand):
    help = 'Export data to CSV file'

    def add_arguments(self, parser):
        parser.add_argument('output_file', type=str)

    def handle(self, *args, **options):
        output_file = options['output_file']
        data = MyModelFirst.objects.all()
        with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            # Write headers
            writer.writerow([
                'id',
                'Data',
                'Time',
                'Resource_Name',
                'Header',
                'Text',
                'Comments_Count',
                'Views',
                'Rating',
                'Count_Positive_Reactions',
                'Count_Negative_Reactions',
                'Reposts',
                'Comment_Text',
                'Type',
                'Garbage',
                'Healthcare',
                'Housing_and_Public_Utilities',
                'Education',
                'Infrastructure',
                'Culture',
                'Environmental_Conditions',
                'Social_Security',
                'Politics',
                'Safety',
                'Availability_of_Goods_and_Services',
                'Official_Statements',
                'Tourism',
                'Facts',
                'Positive',
                'Negative',
                'Neutral',
            ])
            # Write data
            for record in data:
                writer.writerow([
                    record.id,
                    record.Data,
                    record.Time,
                    record.Resource_Name,
                    record.Header,
                    record.Text,
                    record.Comments_Count,
                    record.Views,
                    record.Rating,
                    record.Count_Positive_Reactions,
                    record.Count_Negative_Reactions,
                    record.Reposts,
                    record.Comment_Text,
                    record.Type,
                    record.Garbage,
                    record.Healthcare,
                    record.Housing_and_Public_Utilities,
                    record.Education,
                    record.Infrastructure,
                    record.Culture,
                    record.Environmental_Conditions,
                    record.Social_Security,
                    record.Politics,
                    record.Safety,
                    record.Availability_of_Goods_and_Services,
                    record.Official_Statements,
                    record.Tourism,
                    record.Facts,
                    record.Positive,
                    record.Negative,
                    record.Neutral,
                ])
