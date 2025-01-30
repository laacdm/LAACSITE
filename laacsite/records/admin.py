from django.contrib import admin
from .models import Record

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_of_document', 'institution', 'specialization', 'date', 'paid', 'provider')