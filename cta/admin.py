from django.contrib import admin
from .models import Form, Cuantovaser

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "edad", "interpretacion", "domicilio", "calle",
                    "numero", "colonia", "municipio", "urgente", "nombre_2", "apellido_2", "celular")

# Register your models here.
class FormAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "edad", "interpretacion", "domicilio", "calle",
                    "numero", "colonia", "municipio", "urgente", "nombre_2", "apellido_2", "celular")

class CuantovaserAdmin(admin.ModelAdmin):
    list_display = ("address", )

admin.site.register(Cuantovaser, CuantovaserAdmin)
admin.site.register(Form, FormAdmin)