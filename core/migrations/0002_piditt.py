# Generated by Django 5.0.3 on 2024-03-26 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PIDitt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('año', models.IntegerField()),
                ('total_mujeres', models.IntegerField()),
                ('total_hombres', models.IntegerField()),
                ('total_pi', models.IntegerField()),
            ],
        ),
    ]