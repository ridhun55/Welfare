# Generated by Django 3.2.24 on 2024-04-13 03:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AdminApp', '0013_alter_welfarepost_post_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostCategoryMinorityWelfare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_applied', models.BooleanField(default=False)),
                ('is_approved', models.BooleanField(default=False)),
                ('is_pending', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
                ('new_flag', models.BooleanField(default=True)),
                ('submit_date', models.DateField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostCategoryRuralDevelopment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_applied', models.BooleanField(default=False)),
                ('is_approved', models.BooleanField(default=False)),
                ('is_pending', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
                ('new_flag', models.BooleanField(default=True)),
                ('submit_date', models.DateField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='welfarepost',
            name='post_category',
            field=models.CharField(blank=True, choices=[('Education', 'Education'), ('Healthcare', 'Healthcare'), ('Employment', 'Employment'), ('Housing', 'Housing'), ('Rural_Development', 'Rural Development'), ('Minority_Welfare', 'Minority Welfare')], default='', max_length=60, null=True),
        ),
        migrations.DeleteModel(
            name='PostCategoryWomanAndChild',
        ),
        migrations.AddField(
            model_name='postcategoryruraldevelopment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.welfarepost'),
        ),
        migrations.AddField(
            model_name='postcategoryruraldevelopment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='postcategoryminoritywelfare',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.welfarepost'),
        ),
        migrations.AddField(
            model_name='postcategoryminoritywelfare',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
