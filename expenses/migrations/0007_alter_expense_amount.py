# Generated by Django 5.0.6 on 2024-06-18 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0006_alter_expense_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
