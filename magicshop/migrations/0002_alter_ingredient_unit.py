# Generated by Django 3.2.5 on 2021-08-05 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magicshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(choices=[('Ea', 'Each'), ('g', 'grams'), ('mg', 'milligrams'), ('mL', 'millilitres'), ('L', 'litres'), ('cm', 'centimetres'), ('mm', 'millimetres'), ('Lea', 'leaves'), ('Crs', 'crystals'), ('Dps', 'pindrops'), ('Cks', 'chunks'), ('Wts', 'wotsits')], default='Ea', max_length=3),
        ),
    ]
