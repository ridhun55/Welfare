# Generated by Django 3.2.24 on 2024-04-12 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AdminApp', '0011_reportanissue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportanissue',
            name='issue_flag',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='PostCategoryWomanAndChild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health_center_nearby', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('school_nearby', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('ration_card_no', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('overall_health', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('financial_status', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('is_applied', models.BooleanField(default=False)),
                ('is_approved', models.BooleanField(default=False)),
                ('is_pending', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
                ('new_flag', models.BooleanField(default=True)),
                ('submit_date', models.DateField(blank=True, default=None, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.welfarepost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostCategoryHousing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ration_card_no', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('land_area', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('survey_no', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('no_of_members', models.IntegerField(blank=True, default=0, null=True)),
                ('location', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('is_applied', models.BooleanField(default=False)),
                ('is_approved', models.BooleanField(default=False)),
                ('is_pending', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
                ('new_flag', models.BooleanField(default=True)),
                ('submit_date', models.DateField(blank=True, default=None, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.welfarepost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostCategoryEmployment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('job_entry_date', models.DateField(blank=True, default=None, null=True)),
                ('retirement_date', models.DateField(blank=True, default=None, null=True)),
                ('job_post', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('salary_per_month', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('is_applied', models.BooleanField(default=False)),
                ('is_approved', models.BooleanField(default=False)),
                ('is_pending', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
                ('new_flag', models.BooleanField(default=True)),
                ('submit_date', models.DateField(blank=True, default=None, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.welfarepost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
