from images.models import Image  # Import the Image model
from django.db import models

class Record(models.Model):
    record_id = models.AutoField(primary_key=True)  # New primary key
    name = models.CharField(max_length=255)
    type_of_document = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    specialization = models.BooleanField()
    date = models.DateField()
    paid = models.BooleanField()
    provider = models.CharField(max_length=255)
    description = models.TextField()
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="records")

    def __str__(self):
        return self.name
