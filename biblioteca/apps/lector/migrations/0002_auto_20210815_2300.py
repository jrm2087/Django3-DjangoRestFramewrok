# Generated by Django 3.2.3 on 2021-08-16 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lector', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lector',
            options={'ordering': ['nombres'], 'verbose_name': 'Lector', 'verbose_name_plural': 'Lectores'},
        ),
        migrations.AlterModelOptions(
            name='prestamo',
            options={'ordering': ['libro'], 'verbose_name': 'Prestamo', 'verbose_name_plural': 'Prestamos'},
        ),
    ]
