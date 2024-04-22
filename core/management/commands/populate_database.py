import csv
from pathlib import Path
from django.conf import settings
from django.core.management.base import BaseCommand
from core.models import AcademicosDAP

class Command(BaseCommand):
    help = 'Load data from wage file'

    def handle(self, *args, **kwargs):
        # clear records if they already exist
        if AcademicosDAP.objects.exists():
            AcademicosDAP.objects.all().delete()

       
        DATA_FILE = Path(settings.BASE_DIR) / 'data' / 'academicos_dap.csv'
        assert DATA_FILE.exists(), f"File '{DATA_FILE}' does not exist."


        with open(DATA_FILE, 'r', encoding='latin1') as csvfile:
            reader = csv.DictReader(csvfile)
            db_rows = []
            for row in reader:
                db_rows.append(AcademicosDAP(
                    rut=row['rut'],
                    nombre=row['nombre'],
                    area_acreditacion=row['area_acreditacion'],
                    tipo_programa=row['tipo_programa'],
                    contrato=row['contrato'],
                    vigencia=row['vigencia']
                ))
            # bulk create records    	
            AcademicosDAP.objects.bulk_create(db_rows, batch_size=1000)
      