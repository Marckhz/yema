from django.contrib import admin

from utils.email import send_email

from .dto import EmailDTO
from .models import Appointment, Patient, Staff


def build_message(**kwargs):
    confirmed = "Accepteda" if kwargs['accepted'] == True else 'Rechazada'
    msg =  (
            f'Querido Paciente {kwargs["first_name"]} \n'
            f'Su cita ha sido {confirmed} para el dia {kwargs["start_date"]} '
            f'y hora {kwargs["hour"]} '
            f'con el doctor {kwargs["doctor"]} \n'
            f'Comentarios: \n'
            f'{kwargs["comments"]}'
            )
    return msg


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    pass

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    pass

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):

        first_name = obj.patient.first_name
        email = obj.patient.email
        accepted = form.cleaned_data.get('accepted')
        comments = form.cleaned_data.get('comments')
        doctor = form.cleaned_data.get('doctor')
        start_date = form.cleaned_data.get('start_date')
        hour = form.cleaned_data.get('hour')
        msg = build_message(first_name=first_name, accepted=accepted, comments=comments,
                      doctor=doctor, start_date=start_date, hour=hour
                     )
        email_dto = EmailDTO(recipient_list=[email], message=msg)
        obj.save()
        send_email(email_dto.dict())
    
admin.site.site_header = 'Yema Test Marco Hernandez '

