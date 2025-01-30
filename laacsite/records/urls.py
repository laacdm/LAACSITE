from django.urls import path
from .views import RecordList
from .views import RecordCreateView

urlpatterns = [
    path('', RecordList.as_view(), name='record-list'),
    path('records/create/', RecordCreateView.as_view(), name='record-create'),
]