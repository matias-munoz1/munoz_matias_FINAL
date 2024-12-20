# Generated by Django 5.1.1 on 2024-12-15 05:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Inscrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_participante', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('nro_personas', models.IntegerField()),
                ('telefono', models.CharField(max_length=15)),
                ('estado', models.CharField(choices=[('RESERVADO', 'Reservado'), ('CONFIRMADO', 'Confirmado')], max_length=50)),
                ('observacion', models.TextField(blank=True, null=True)),
                ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_seminario.institucion')),
            ],
        ),
    ]
