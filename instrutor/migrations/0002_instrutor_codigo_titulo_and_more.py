# Generated by Django 5.2.1 on 2025-06-06 23:18

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instrutor', '0001_initial'),
        ('titulo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrutor',
            name='codigo_titulo',
            field=models.ForeignKey(blank=True, db_column='titulo_codigo', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titulos', to='titulo.titulo'),
        ),
        migrations.AlterField(
            model_name='instrutor',
            name='dataNascimento',
            field=models.DateField(blank=True, default=datetime.datetime(2025, 6, 6, 23, 18, 49, 739877, tzinfo=datetime.timezone.utc), help_text='Informe a data de Nascimento', null=True),
        ),
    ]
