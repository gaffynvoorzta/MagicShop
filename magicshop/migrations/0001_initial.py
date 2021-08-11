# Generated by Django 3.2.5 on 2021-08-02 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('quantity', models.FloatField(default=0)),
                ('unit', models.CharField(max_length=200)),
                ('price_per_unit', models.FloatField(default=0)),
                ('restricted', models.CharField(choices=[('FA', 'Faerie'), ('TX', 'Toxic'), ('NC', 'Necromantic'), ('EX', 'Explosive'), ('--', '---')], default='--', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='PotionItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], default='S', max_length=2)),
                ('price', models.FloatField(default=0.0)),
                ('description', models.CharField(max_length=300)),
                ('is_restricted', models.BooleanField(default=False, verbose_name='Restricted Item')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeRequirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(default=0)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magicshop.ingredient')),
                ('potion_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magicshop.potionitem')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('potion_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magicshop.potionitem')),
            ],
        ),
    ]