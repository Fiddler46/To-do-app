from django.contrib import admin
from .models import Todo #add this , importing todo model that we created 
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')
# Register your models here
admin.site.register(Todo, TodoAdmin)