from django.contrib import admin
from .models import *

@admin.register(Application)
class StreetAdmin(admin.ModelAdmin):
    pass
