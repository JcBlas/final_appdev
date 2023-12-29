# myapp/urls.py

from django.urls import path
from .views import DocumentDetailView, PersonListView, AddressListView, DocumentListView, EventListView, JobListView, default_view

urlpatterns = [
    path('persons/', PersonListView.as_view(), name='person_list'),
    path('persons/<int:pk>/', DocumentDetailView.as_view(), name='person_detail'),  # Correct the import statement
    path('addresses/', AddressListView.as_view(), name='address_list'),
    path('documents/', DocumentListView.as_view(), name='document_list'),
    path('events/', EventListView.as_view(), name='event_list'),
    path('jobs/', JobListView.as_view(), name='job_list'),
    path('documents/<int:pk>/', DocumentDetailView.as_view(), name='document_detail'),
    path('', default_view, name='default_view'),
]
