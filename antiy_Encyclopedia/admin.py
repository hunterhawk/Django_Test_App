from django.contrib import admin
from .models import Process_Test

# Register your models here.
class ProcessAdmin(admin.ModelAdmin):
    list_display = ('path','company','product','create_time','author')

admin.site.register(Process_Test, ProcessAdmin)
