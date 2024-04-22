# Generated by Django 5.0.3 on 2024-03-26 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicosDAP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=100)),
                ('area_acreditacion', models.CharField(max_length=100)),
                ('tipo_programa', models.CharField(max_length=100)),
                ('contrato', models.CharField(max_length=100)),
                ('vigencia', models.CharField(max_length=100)),
            ],
        ),
    ]
