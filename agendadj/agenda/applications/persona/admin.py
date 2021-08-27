from django.contrib import admin

from .models import Hobby, Person, Reunion

admin.site.register(Hobby)
admin.site.register(Person)
admin.site.register(Reunion)
