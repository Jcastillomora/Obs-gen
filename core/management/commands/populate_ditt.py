import csv
from pathlib import Path
from django.conf import settings
from django.core.management.base import BaseCommand
from core.models import PIDitt

class Command(BaseCommand):
    help = 'Load data from wage file'

    def handle(self, *args, **kwargs):
        # clear records if they already exist
        if PIDitt.objects.exists():
            PIDitt.objects.all().delete()
        
        DATA_FILE1 = Path(settings.BASE_DIR) / 'data' / 'ditt.csv'
        assert DATA_FILE1.exists(), f"File '{DATA_FILE1}' does not exist."


        with open(DATA_FILE1, 'r', encoding='latin1') as csvfile:
            reader = csv.DictReader(csvfile)
            db_rows = []
            for row in reader:
                db_rows.append(PIDitt(
                    año=row['año'],
                    total_mujeres=row['total_mujeres'],
                    total_hombres=row['total_hombres'],
                    total_pi=row['total_PI']                    
                ))
            # bulk create records    	
            PIDitt.objects.bulk_create(db_rows, batch_size=1000)
      