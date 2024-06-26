# Generated by Django 3.2.24 on 2024-03-30 06:03

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AdminApp', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('aadhar_no', models.CharField(max_length=12, unique=True)),
                ('profile_img', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('full_name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('dob', models.DateField(blank=True, default=None, null=True)),
                ('age', models.IntegerField(blank=True, default=0, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='', max_length=1, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('mobile_no', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('aadhar_img', models.ImageField(blank=True, null=True, upload_to='aadhar_images/')),
                ('father', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('mother', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('marital_status', models.CharField(blank=True, choices=[('S', 'Single'), ('M', 'Married')], default='', max_length=1, null=True)),
                ('children_no', models.IntegerField(blank=True, default=0, null=True)),
                ('employment_status', models.CharField(blank=True, choices=[('Emp', 'Employed'), ('Unemp', 'Unemployed'), ('Self-emp', 'Self-employed'), ('Stud', 'Student'), ('Ret', 'Retired')], default='', max_length=10, null=True)),
                ('occupation', models.CharField(blank=True, choices=[('Government_Employee', 'Government Employee'), ('Accountant', 'Accountant'), ('Actor/Actress', 'Actor/Actress'), ('Architect', 'Architect'), ('Artist', 'Artist'), ('Baker', 'Baker'), ('Banker', 'Banker'), ('Barista', 'Barista'), ('Bartender', 'Bartender'), ('Biologist', 'Biologist'), ('Carpenter', 'Carpenter'), ('Chef', 'Chef'), ('Cleaner', 'Cleaner'), ('Computer_Programmer', 'Computer Programmer'), ('Dentist', 'Dentist'), ('Doctor', 'Doctor'), ('Electrician', 'Electrician'), ('Engineer', 'Engineer'), ('Farmer', 'Farmer'), ('Firefighter', 'Firefighter'), ('Fisherman', 'Fisherman'), ('Flight_Attendant', 'Flight Attendant'), ('Graphic_Designer', 'Graphic Designer'), ('Hairdresser', 'Hairdresser'), ('Journalist', 'Journalist'), ('Lawyer', 'Lawyer'), ('Librarian', 'Librarian'), ('Mechanic', 'Mechanic'), ('Musician', 'Musician'), ('Nurse', 'Nurse'), ('Pharmacist', 'Pharmacist'), ('Photographer', 'Photographer'), ('Pilot', 'Pilot'), ('Plumber', 'Plumber'), ('Police_Officer', 'Police Officer'), ('Professor', 'Professor'), ('Psychologist', 'Psychologist'), ('Real_Estate_Agent', 'Real Estate Agent'), ('Receptionist', 'Receptionist'), ('Scientist', 'Scientist'), ('Software_Developer', 'Software Developer'), ('Teacher', 'Teacher'), ('Truck_Driver', 'Truck Driver'), ('Veterinarian', 'Veterinarian'), ('Waiter/Waitress', 'Waiter/Waitress'), ('Writer', 'Writer')], default='', max_length=100, null=True)),
                ('monthly_income', models.FloatField(blank=True, default=0, null=True)),
                ('highest_education', models.CharField(blank=True, choices=[('Primary', 'Primary School'), ('Secondary', 'Secondary School'), ('High', 'High School'), ('Dip', 'Diploma'), ('Bachelors', "Bachelor's Degree"), ('Masters', "Master's Degree"), ('Doctorate', 'Doctorate')], default='', max_length=15, null=True)),
                ('highest_education_mark', models.FloatField(blank=True, default=0, null=True)),
                ('caste', models.CharField(blank=True, choices=[('SC', 'Scheduled Caste (SC)'), ('ST', 'Scheduled Tribe (ST)'), ('OBC', 'Other Backward Class (OBC)'), ('General', 'General'), ('Prefer_not_to_say', 'Prefer not to say')], default='', max_length=20, null=True)),
                ('religion', models.CharField(blank=True, choices=[('Hin', 'Hinduism'), ('Isl', 'Islam'), ('Chr', 'Christianity'), ('Sik', 'Sikhism'), ('Bud', 'Buddhism'), ('Jai', 'Jainism')], default='', max_length=15, null=True)),
                ('has_disabilities', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=3, null=True)),
                ('disabilities_specify', models.CharField(blank=True, default='_', max_length=255, null=True)),
                ('bank_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('account_number', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('ifsc_code', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('identity_img', models.FileField(blank=True, null=True, upload_to='identity_images/')),
                ('verified_flag', models.BooleanField(default=False)),
                ('profile_updated_flag', models.BooleanField(default=False)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CategoryEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_school', models.CharField(max_length=255)),
                ('grade', models.CharField(max_length=255)),
                ('academic_performance', models.CharField(max_length=255)),
                ('reason_for_application', models.TextField()),
                ('is_applied', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.welfarepost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
