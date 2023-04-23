from django.contrib import admin
from . models import todo


# Register your models here.

@admin.register(todo)

class todoAdmin(admin.ModelAdmin):
     """ Customizing the way models are displayed"""
     list_display = ("task", "completed", "user", "updated")
     list_filter = ("task", "updated", "user")
     search_fields = ("task","user")
     date_hierarchy = ("updated")
     raw_id_fields = ("user",) # raw field must be a list or a tuple