# Generated by Django 5.1.7 on 2025-03-28 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0017_topico_resposta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resposta',
            old_name='criado_em',
            new_name='data_criacao',
        ),
        migrations.RenameField(
            model_name='topico',
            old_name='criado_em',
            new_name='data_criacao',
        ),
    ]
