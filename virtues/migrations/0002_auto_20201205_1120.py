# Generated by Django 3.0.7 on 2020-12-05 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtues', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='virtues',
            name='virtue',
            field=models.PositiveIntegerField(choices=[(1, 'Charity'), (2, 'Chastity'), (3, 'Diligence'), (4, 'Humility'), (5, 'Patience'), (6, 'Temperance'), (7, 'Kindness')], default=1),
        ),
    ]
