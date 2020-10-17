from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Clase, ClaseAlumno

admin.site.register(Usuario, UserAdmin)

admin.site.register(Clase)
admin.site.register(ClaseAlumno)

# Register your models here.
