# Generated by Django 4.1.3 on 2022-11-24 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='store',
            options={'ordering': ['city'], 'verbose_name': 'Магазин', 'verbose_name_plural': 'Магазины'},
        ),
    ]
