# Generated by Django 5.0.6 on 2024-06-18 05:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.CASCADE, to='expenses.category'),
        ),
    ]
