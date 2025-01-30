from rest_framework import serializers
from images.models import Image
from records.models import Record

class RecordSerializer(serializers.ModelSerializer):
    image_id = serializers.PrimaryKeyRelatedField(queryset=Image.objects.all())

    class Meta:
        model = Record
        fields = ['model_id', 'name', 'description', 'image_id']  # Ensure image_id is included