# Generated by Django 3.2.24 on 2024-03-30 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WelfarePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(blank=True, max_length=120, null=True)),
                ('post_description', models.TextField(blank=True, null=True)),
                ('post_img', models.ImageField(blank=True, null=True, upload_to='welfare_images/')),
                ('post_age', models.IntegerField(blank=True, default=0, null=True)),
                ('post_category', models.CharField(blank=True, choices=[('Education', 'Education'), ('Healthcare', 'Healthcare'), ('Employment', 'Employment'), ('Social_Security', 'Social Security'), ('Housing', 'Housing'), ('Rural_Development', 'Rural Development'), ('Women_and_Child_Welfare', 'Women and Child Welfare'), ('Environment', 'Environment'), ('Disaster_Management', 'Disaster Management'), ('Minority_Welfare', 'Minority Welfare')], default='', max_length=60, null=True)),
                ('post_gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('All', 'All')], default='', max_length=3, null=True)),
                ('post_marital_status', models.CharField(blank=True, choices=[('S', 'Single'), ('M', 'Married'), ('Both', 'Both')], default='', max_length=5, null=True)),
                ('post_children', models.IntegerField(blank=True, default=0, null=True)),
                ('post_employment_status', models.CharField(blank=True, choices=[('Emp', 'Employed'), ('Unemp', 'Unemployed'), ('Self-emp', 'Self-employed'), ('Stud', 'Student'), ('Ret', 'Retired'), ('All', 'All')], default='', max_length=10, null=True)),
                ('post_occupation', models.CharField(blank=True, choices=[('Government_Employee', 'Government Employee'), ('Accountant', 'Accountant'), ('Actor/Actress', 'Actor/Actress'), ('Architect', 'Architect'), ('Artist', 'Artist'), ('Baker', 'Baker'), ('Banker', 'Banker'), ('Barista', 'Barista'), ('Bartender', 'Bartender'), ('Biologist', 'Biologist'), ('Carpenter', 'Carpenter'), ('Chef', 'Chef'), ('Cleaner', 'Cleaner'), ('Computer_Programmer', 'Computer Programmer'), ('Dentist', 'Dentist'), ('Doctor', 'Doctor'), ('Electrician', 'Electrician'), ('Engineer', 'Engineer'), ('Farmer', 'Farmer'), ('Firefighter', 'Firefighter'), ('Fisherman', 'Fisherman'), ('Flight_Attendant', 'Flight Attendant'), ('Graphic_Designer', 'Graphic Designer'), ('Hairdresser', 'Hairdresser'), ('Journalist', 'Journalist'), ('Lawyer', 'Lawyer'), ('Librarian', 'Librarian'), ('Mechanic', 'Mechanic'), ('Musician', 'Musician'), ('Nurse', 'Nurse'), ('Pharmacist', 'Pharmacist'), ('Photographer', 'Photographer'), ('Pilot', 'Pilot'), ('Plumber', 'Plumber'), ('Police_Officer', 'Police Officer'), ('Professor', 'Professor'), ('Psychologist', 'Psychologist'), ('Real_Estate_Agent', 'Real Estate Agent'), ('Receptionist', 'Receptionist'), ('Scientist', 'Scientist'), ('Software_Developer', 'Software Developer'), ('Teacher', 'Teacher'), ('Truck_Driver', 'Truck Driver'), ('Veterinarian', 'Veterinarian'), ('Waiter/Waitress', 'Waiter/Waitress'), ('Writer', 'Writer'), ('All', 'All')], default='', max_length=100, null=True)),
                ('post_monthly_income', models.FloatField(blank=True, default=0, null=True)),
                ('post_highest_education', models.CharField(blank=True, choices=[('Primary', 'Primary School'), ('Secondary', 'Secondary School'), ('High', 'High School'), ('Dip', 'Diploma'), ('Bachelors', "Bachelor's Degree"), ('Masters', "Master's Degree"), ('Doctorate', 'Doctorate'), ('All', 'All')], default='', max_length=15, null=True)),
                ('post_highest_education_mark', models.FloatField(blank=True, default=0, null=True)),
                ('post_caste', models.CharField(blank=True, choices=[('SC', 'Scheduled Caste (SC)'), ('ST', 'Scheduled Tribe (ST)'), ('OBC', 'Other Backward Class (OBC)'), ('General', 'General'), ('Prefer_not_to_say', 'Prefer not to say'), ('All', 'All'), ('NA', 'NA')], default='', max_length=20, null=True)),
                ('post_religion', models.CharField(blank=True, choices=[('Hin', 'Hinduism'), ('Isl', 'Islam'), ('Chr', 'Christianity'), ('Sik', 'Sikhism'), ('Bud', 'Buddhism'), ('Jai', 'Jainism'), ('All', 'All')], default='', max_length=15, null=True)),
                ('post_has_disabilities', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('All', 'All')], default='', max_length=3, null=True)),
                ('post_active', models.BooleanField(default=True)),
                ('post_verified', models.BooleanField(default=False)),
                ('post_read', models.BooleanField(default=False)),
                ('post_create_date', models.DateTimeField(auto_now_add=True)),
                ('post_start_date', models.DateField(blank=True, default=None, null=True)),
                ('post_end_date', models.DateField(blank=True, default=None, null=True)),
            ],
        ),
    ]