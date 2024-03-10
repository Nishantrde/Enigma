# Generated by Django 4.2.9 on 2024-03-08 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0007_rename_reflect_reflector'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='user_id',
            field=models.CharField(default='DOG', max_length=20),
        ),
        migrations.AddField(
            model_name='keyboard',
            name='user_id',
            field=models.CharField(default='DOG', max_length=20),
        ),
        migrations.AddField(
            model_name='plugboard',
            name='user_id',
            field=models.CharField(default='DOG', max_length=20),
        ),
        migrations.AddField(
            model_name='reflector',
            name='user_id',
            field=models.CharField(default='DOG', max_length=20),
        ),
        migrations.AddField(
            model_name='rotor_i',
            name='user_id',
            field=models.CharField(default='DOG', max_length=20),
        ),
        migrations.AddField(
            model_name='rotor_ii',
            name='user_id',
            field=models.CharField(default='DOG', max_length=20),
        ),
        migrations.AddField(
            model_name='rotor_iii',
            name='user_id',
            field=models.CharField(default='DOG', max_length=20),
        ),
    ]