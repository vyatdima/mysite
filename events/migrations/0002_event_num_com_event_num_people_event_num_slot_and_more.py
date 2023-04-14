# Generated by Django 4.2 on 2023-04-11 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='num_com',
            field=models.IntegerField(blank=True, default=0, verbose_name='Количество команд'),
        ),
        migrations.AddField(
            model_name='event',
            name='num_people',
            field=models.IntegerField(blank=True, default=0, verbose_name='Количество участников'),
        ),
        migrations.AddField(
            model_name='event',
            name='num_slot',
            field=models.IntegerField(blank=True, default=0, verbose_name='Количество слотов'),
        ),
        migrations.AddField(
            model_name='peopleevent',
            name='mesto',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
