from django.contrib import admin
from .models import fileDetails, tvDetails
from .forms import fileDetailsAdminForm

# Register your models here.

@admin.register(fileDetails)
class fileDetailsModel(admin.ModelAdmin):
    form = fileDetailsAdminForm
    list_display = ('title', 'file_path')

@admin.register(tvDetails)
class tvDetailsModel(admin.ModelAdmin):
    list_display = ('tv_name', 'tv_description', 'tv_location')