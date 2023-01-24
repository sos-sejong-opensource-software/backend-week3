from django.contrib import admin
from .models import TodoModel

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    pass

admin.site.register(TodoModel)