from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'registered_or_not')
    list_filter = ('registered_or_not', 'age')
    search_fields = ('name',)

# Alternatively, if you prefer the simpler method:
# admin.site.register(Student)
