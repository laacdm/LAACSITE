import json
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from records.models import Record
from images.models import Image
from mongoengine.errors import DoesNotExist

class Command(BaseCommand):
    help = "Populate PostgreSQL with records from a JSON file"

    def handle(self, *args, **kwargs):
        # Define the path to the JSON file
        json_file_path = os.path.join(settings.BASE_DIR, "data", "records.json")

        # Open and load the JSON file
        with open(json_file_path, "r") as file:
            records = json.load(file)  # Read the file into a Python list of dictionaries

        for record_data in records:
            record_id = record_data["record_id"]
            image_id = record_data.get("image_id")  # Get image_id (if any)

            # Check if the image_id exists in MongoDB
            image_exists = None
            if image_id:
                try:
                    image_exists = Image.objects.get(image_id=image_id)  # Look up image in MongoDB
                except DoesNotExist:
                    self.stdout.write(self.style.WARNING(f"Image ID {image_id} not found in MongoDB"))

            # Create the record if it doesn’t already exist
            record, created = Record.objects.get_or_create(
                record_id=record_id,
                defaults={
                    "name": record_data["name"],
                    "type_of_document": record_data["type_of_document"],
                    "institution": record_data["institution"],
                    "specialization": record_data["specialization"],  # Boolean field
                    "date": record_data["date"],
                    "paid": record_data["paid"],  # Boolean field
                    "provider": record_data["provider"],
                    "description": record_data["description"],
                    "image_id": image_id if image_exists else None  # Assign image_id only if it exists in MongoDB
                }
            )

            # Print status
            if created:
                self.stdout.write(self.style.SUCCESS(f"Added: {record.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Skipped: {record.name} (already exists)"))
