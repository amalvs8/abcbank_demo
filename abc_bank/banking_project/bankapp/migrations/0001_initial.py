# Generated by Django 4.2.3 on 2023-09-01 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=255, unique=True)),
                ('wiki_link', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=255, unique=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.district')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('phone_no', models.IntegerField()),
                ('email_address', models.EmailField(max_length=30, unique=True)),
                ('address', models.CharField(max_length=30)),
                ('account_type', models.CharField(choices=[('Savings Account', 'Savings Account'), ('Current Account', 'Current Account')], max_length=30)),
                ('material_provided', models.CharField(max_length=50)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.branch')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.district')),
            ],
        ),
    ]
