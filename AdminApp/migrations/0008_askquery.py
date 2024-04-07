# Generated by Django 3.2.24 on 2024-04-07 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0007_postcategoryhealth_new_flag'),
    ]

    operations = [
        migrations.CreateModel(
            name='AskQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('mobile', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('submit_date', models.DateField(blank=True, default=None, null=True)),
                ('query_flag', models.BooleanField(default=False)),
            ],
        ),
    ]
