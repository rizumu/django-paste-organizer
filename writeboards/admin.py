from django.contrib import admin
from models import Writeboard

class WriteboardAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('writeboard_name',)}

admin.site.register(Writeboard, WriteboardAdmin)