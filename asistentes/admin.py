from django.contrib import admin
from asistentes.models import Participantes,Asistencia
# Register your models here.

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
    
admin.site.register(Participantes,ParticipantesAdmin)
admin.site.register(Asistencia,AsistenciaAdmin)
