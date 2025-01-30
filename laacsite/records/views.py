from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from records.models import Record  # Correct the import path
from .serializers import RecordSerializer

class RecordList(APIView):
    model = Record
    template_name = 'records/record_list.html'  # Define your template path
    context_object_name = 'records'
    paginate_by = 10  # Optional: Add pagination

    def get(self, request):
        records = Record.objects.all()
        serializer = RecordSerializer(records, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_queryset(self):
        queryset = Record.objects.all()
        sort_field = self.request.GET.get('sort', 'name')  # Default sort by 'name'
        order = self.request.GET.get('order', 'asc')  # Default order is ascending

        if order == 'desc':
            sort_field = f'-{sort_field}'  # Prefix with '-' for descending order

        # Ensure the sort_field is valid to avoid errors
        if sort_field.lstrip('-') in [f.name for f in Record._meta.get_fields()]:
            return queryset.order_by(sort_field)
        return queryset
    
class RecordCreateView(APIView):
    def post(self, request):
        serializer = RecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)