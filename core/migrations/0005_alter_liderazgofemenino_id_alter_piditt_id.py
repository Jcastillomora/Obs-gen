# Generated by Django 4.2.11 on 2024-04-16 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_liderazgofemenino_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liderazgofemenino',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='piditt',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]