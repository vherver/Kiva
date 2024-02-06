from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand

import csv

from brand.models import Brand
from model.models import SubBrand


class Command(BaseCommand):
    help = (
        "Command to load vehicle model. If a model already exists,"
        " it will not be created again."
    )

    def handle(self, *args, **options):
        file_path = settings.BASE_DIR / "initial_data" / "model.csv"

        expected_columns = ["brand", "name", "slug"]

        try:
            with open(file_path, newline="", encoding="utf-8") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                headers = csv_reader.fieldnames

                if not headers == expected_columns:
                    raise ValidationError

                for row in csv_reader:
                    print(f"Processing row {row}")
                    brand = Brand.objects.filter(slug=row["brand"]).first()

                    if brand:
                        SubBrand.objects.get_or_create(
                            name=row["name"], slug=row["slug"], brand=brand
                        )

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR("File not found"))

        except ValidationError:
            self.stdout.write(
                self.style.ERROR(
                    "Columns must be brand, name, slug in the CSV"
                )
            )
