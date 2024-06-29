from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Ausbilder)
admin.site.register(Gruppe)
admin.site.register(Fach)
#admin.site.register(Thema)
admin.site.register(Lernerfolgskontrolle)
# admin.site.register(Schueler)
admin.site.register(Ausbildungseinheit)

@admin.register(Schueler)
class SchuelerAdmin(admin.ModelAdmin):
    list_display = ['name', 'gruppe']
    search_fields = ['name']
    list_filter = ['gruppe', 'name']

@admin.register(Thema)
class ThemaAdmin(admin.ModelAdmin):
    search_fields = ['inhalt']
    list_filter = ['fach']

