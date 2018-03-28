from django.contrib import admin
from .models import *

@admin.register(
    Application,
    AppTypes,
    AppStatus,
    AppError,
    AppSuccess,
    Apartment,
    House,
    Street
)
class StreetAdmin(admin.ModelAdmin):
    pass
