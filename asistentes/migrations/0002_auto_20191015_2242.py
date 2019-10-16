# Generated by Django 2.2.4 on 2019-10-16 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asistentes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participantes',
            name='fecha_registro',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='participantes',
            name='telefono',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_uno', models.DateField(blank=True, null=True)),
                ('dia_dos', models.DateField(blank=True, null=True)),
                ('dia_tres', models.DateField(blank=True, null=True)),
                ('participante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='asistentes.Participantes')),
            ],
        ),
    ]