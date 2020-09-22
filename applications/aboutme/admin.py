from django.contrib import admin
from .models import Fallo, Perfil, Publicacion

# Register your models here.

admin.site.register(Perfil)
admin.site.register(Fallo)
admin.site.register(Publicacion)
