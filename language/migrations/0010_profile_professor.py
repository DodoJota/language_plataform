# Generated by Django 5.1.7 on 2025-03-26 10:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0009_material_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='professor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='language.profile'),
        ),
    ]
