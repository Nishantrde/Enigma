# Generated by Django 4.2.9 on 2024-03-08 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0008_inventory_user_id_keyboard_user_id_plugboard_user_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rotor_i',
            name='letter',
        ),
        migrations.RemoveField(
            model_name='rotor_i',
            name='signal',
        ),
        migrations.RemoveField(
            model_name='rotor_ii',
            name='letter',
        ),
        migrations.RemoveField(
            model_name='rotor_ii',
            name='signal',
        ),
        migrations.RemoveField(
            model_name='rotor_iii',
            name='letter',
        ),
        migrations.RemoveField(
            model_name='rotor_iii',
            name='signal',
        ),
    ]