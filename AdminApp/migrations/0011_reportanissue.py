# Generated by Django 3.2.24 on 2024-04-07 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0010_delete_askquery'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportAnIssue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('issue_message', models.TextField(blank=True, null=True)),
                ('submit_date', models.DateTimeField(auto_now_add=True)),
                ('issue_flag', models.BooleanField(default=False)),
            ],
        ),
    ]
