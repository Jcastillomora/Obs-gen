# Generated by Django 4.2.13 on 2024-06-11 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_rename_doctorado_academicosdap_tipos_claustro_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='academicosdap_tipos',
            old_name='nucelo',
            new_name='nucleo',
        ),
    ]
