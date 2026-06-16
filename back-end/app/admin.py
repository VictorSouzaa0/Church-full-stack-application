from django.contrib import admin
from .models import Church, People, Role, Archdiocese
# Register your models here.
admin.site.register(Church)
admin.site.register(People)
admin.site.register(Role)
admin.site.register(Archdiocese)