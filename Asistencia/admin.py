from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Lider, Persona, Asistencia, Reunion

# class AssignTimeInline(admin.TabularInline):
#      model = AssignTime
#      extra = 0
    
# class AssignAdmin(admin.ModelAdmin):
#     #  inlines = [AssignTimeInline]
#      list_display = ('teacher', 'created_at')
#      search_fields = ('teacher__name', 'created_at')
#      ordering = ['teacher', 'created_at']
#      raw_id_fields = ['teacher']

# class TeacherAdmin(admin.ModelAdmin):
#      list_display = ('name',)
#      search_fields = ('name',)
#      ordering = ['name']
    
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('persona', 'reunion',)
    search_fields = ('persona__nombre_completo','reunion',)
    ordering = ['persona__nombre_completo', 'created_at', 'reunion']
    raw_id_fields = ['persona', ]



# class ReunionAdmin(admin.ModelAdmin):
#     list_display = ('descripcion_reunion', 'fecha_evento',)
#     search_fields = ('descripcion_reunion', 'fecha_evento',)
#     ordering = ['descripcion_reunion', 'fecha_evento']



class PersonaAdmin(ImportExportModelAdmin):
    list_display = ('nombre_completo', 'cedula','telefono', 'lider_referido',)
    search_fields = ('nombre_completo', 'cedula', 'lider_referido__nombre_completo',)
    ordering = ['nombre_completo', 'cedula', 'lider_referido']
    raw_id_fields = ['lider_referido', ]

class LiderAdmin(ImportExportModelAdmin):
    list_display = ('nombre_completo',)
    search_fields = ('nombre_completo',)
    ordering = ['nombre_completo',]

#  Register your models here.
admin.site.register(Lider, LiderAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Asistencia, AsistenciaAdmin)
# admin.site.register(Reunion, ReunionAdmin)
