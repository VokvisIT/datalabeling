# Generated by Django 4.2.2 on 2023-10-31 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labeling', '0004_alter_mymodelfirst_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodelfirst',
            name='Views',
            field=models.IntegerField(),
        ),
    ]
