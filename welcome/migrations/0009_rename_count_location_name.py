# Generated by Django 4.2 on 2023-05-06 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0008_remove_animalname_animal_animaldata_animal_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='count',
            new_name='name',
        ),
    ]