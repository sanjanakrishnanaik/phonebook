from django.contrib import admin
from .models import Contact, Category
from import_export.admin import ImportExportModelAdmin

@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
