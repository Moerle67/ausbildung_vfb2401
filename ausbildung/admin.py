from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Ausbilder)
admin.site.register(Gruppe)
admin.site.register(Fach)
admin.site.register(Thema)
admin.site.register(Lernerfolgskontrolle)
admin.site.register(Schueler)
admin.site.register(Ausbildungseinheit)