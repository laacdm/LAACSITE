from django.http import FileResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Image
from .serializers import ImageSerializer

class ImageList(APIView):
    def get(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ImageDownload(APIView):
    def get(self, request, image_id):
        image = Image.objects.get(image_id=image_id)
        return FileResponse(image.image, content_type="application/pdf", as_attachment=True, filename=image.name)