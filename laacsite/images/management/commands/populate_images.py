from django.core.management.base import BaseCommand
from images.models import Image
import os
from mongoengine.errors import NotUniqueError

class Command(BaseCommand):
    help = "Populate MongoDB with PDF images"

    def handle(self, *args, **kwargs):
        pdf_directory = "path_to_your_pdf_files"
        for file_name in os.listdir(pdf_directory):
            if file_name.endswith(".pdf"):
                image_id = file_name.split(".")[0]  # Use filename (without .pdf) as ID
                with open(os.path.join(pdf_directory, file_name), "rb") as pdf_file:
                    try:
                        image = Image(
                            image_id=image_id,
                            name=file_name,
                        )
                        image.image.put(pdf_file, content_type="application/pdf")
                        image.save()
                        self.stdout.write(self.style.SUCCESS(f"Uploaded {file_name} with ID {image_id}"))
                    except NotUniqueError:
                        self.stdout.write(self.style.WARNING(f"Skipping {file_name}: already exists"))