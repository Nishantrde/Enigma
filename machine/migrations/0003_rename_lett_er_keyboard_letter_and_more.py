# Generated by Django 4.2.9 on 2024-03-08 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0002_keyboard_lett_er_keyboard_signal_plugboard_pairs_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='keyboard',
            old_name='lett_er',
            new_name='letter',
        ),
        migrations.RenameField(
            model_name='rotors_i',
            old_name='lett_er',
            new_name='letter',
        ),
        migrations.RenameField(
            model_name='rotors_ii',
            old_name='lett_er',
            new_name='letter',
        ),
        migrations.RenameField(
            model_name='rotors_iii',
            old_name='lett_er',
            new_name='letter',
        ),
    ]
