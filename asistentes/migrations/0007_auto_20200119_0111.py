# Generated by Django 3.0.2 on 2020-01-19 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asistentes', '0006_auto_20200119_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantes',
            name='rol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='asistentes.Rol'),
        ),
    ]