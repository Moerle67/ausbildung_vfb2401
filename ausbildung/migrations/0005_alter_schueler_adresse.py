# Generated by Django 5.0.6 on 2024-06-29 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ausbildung', '0004_ausbildungseinheit_schueler_lernerfolgskontrolle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schueler',
            name='adresse',
            field=models.TextField(blank=True, null=True, verbose_name='Adresse'),
        ),
    ]
