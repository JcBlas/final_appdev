from django.contrib import admin
from .models import Person, Address, Job, Event, Document
# Register your models here.

admin.site.register(Person)
admin.site.register(Address)
admin.site.register(Job)
admin.site.register(Event)
admin.site.register(Document)