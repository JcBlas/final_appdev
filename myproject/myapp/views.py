from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View
from .models import Person, Address, Document, Event, Job
# Create your views here.

class PersonListView(ListView):
    model = Person
    template_name = 'person_list.html'
    context_object_name = 'persons'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pagination_template'] = 'pagination.html'
        context['items'] = context[self.context_object_name]
        return context

class AddressListView(ListView):
    model = Address
    template_name = 'address_list.html'
    context_object_name = 'addresses'
    paginate_by = 5

class DocumentListView(ListView):
    model = Document
    template_name = 'document_list.html'
    context_object_name = 'documents'
    paginate_by = 5

class DocumentDetailView(View):
    template_name = 'document_detail.html'

    def get(self, request, pk):
        document = get_object_or_404(Document, pk=pk)
        return render(request, self.template_name, {'document': document})

class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'
    context_object_name = 'events'
    paginate_by = 5

class JobListView(ListView):
    model = Job
    template_name = 'job_list.html'
    context_object_name = 'jobs'
    paginate_by = 5

def default_view(request):
    return render(request, 'default_view.html')