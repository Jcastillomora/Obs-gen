# Generated by Django 4.2.11 on 2024-04-17 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_liderazgofemenino_id_alter_piditt_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiderazgoPublicaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('año', models.IntegerField()),
                ('total_mujeres', models.IntegerField()),
                ('total_hombres', models.IntegerField()),
                ('total_publicaciones', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='liderazgofemenino',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='piditt',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]