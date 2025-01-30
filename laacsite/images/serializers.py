from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.Serializer):
    image_id = serializers.CharField()  # Primary key
    name = serializers.CharField()
    image_url = serializers.SerializerMethodField()

    def get_image_url(self, obj):
        return f"/api/images/{obj.image_id}/download"