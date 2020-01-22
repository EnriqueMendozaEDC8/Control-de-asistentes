from django.contrib import admin
from asistentes.models import Participantes,Asistencia,Recursos,TemasRecursos,Rol
# Register your models here.

class RolAdmin(admin.ModelAdmin):
    list_display = ('id','nombre_rol')

class ParticipantesAdmin(admin.ModelAdmin):
    list_display = ('id','nombres', 'apellidos', 'email')
    search_fields = ('id','nombres', 'apellidos','email')

class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('get_idparticipante','get_participante','dia_uno', 'dia_dos','dia_tres')
    list_filter = ('dia_uno',)

    def get_participante(self, obj):
        return obj.participante.email

    def get_idparticipante(self, obj):
        return obj.participante.id
        
    get_participante.short_description = 'Participante'
    get_idparticipante.short_description = 'Id participante'

class TemasRecursosAdmin(admin.ModelAdmin):
    list_display = ('id','nombre_tema')
    search_fields = ('id','nombre_tema')

class RecursosAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'informacion_recurso', 'get_tema')
    search_fields = ('id','nombre', 'informacion_recurso', 'tema')

    def get_tema(self, obj):
        return obj.tema.nombre_tema

    get_tema.short_description = 'Tema'
    
admin.site.register(Rol,RolAdmin)
admin.site.register(Participantes,ParticipantesAdmin)
admin.site.register(Asistencia,AsistenciaAdmin)
admin.site.register(Recursos,RecursosAdmin)
admin.site.register(TemasRecursos,TemasRecursosAdmin)
