# Generated by Django 3.2.24 on 2024-03-30 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0004_postcategoryhealth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcategoryhealth',
            old_name='blood',
            new_name='blood_group',
        ),
        migrations.RenameField(
            model_name='postcategoryhealth',
            old_name='state',
            new_name='blood_pressure_condition',
        ),
        migrations.AddField(
            model_name='postcategoryhealth',
            name='hearing_condition',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='postcategoryhealth',
            name='ration_card_no',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='postcategoryhealth',
            name='vision_condition',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]