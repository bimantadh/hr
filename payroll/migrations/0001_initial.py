# Generated by Django 5.0 on 2023-12-23 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payroll_name', models.CharField(max_length=50)),
                ('amount', models.CharField(max_length=15)),
                ('deposited_date', models.DateField()),
                ('payed_to', models.CharField(max_length=50)),
                ('payed_by', models.CharField(max_length=50)),
            ],
        ),
    ]
