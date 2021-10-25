from django.core.exceptions import ValidationError
from django.db import IntegrityError

from appointments.models import Appointment, Patient

from .dto import AppointmentDTO, PayloadDTO, PersonaDTO


def create_patient(patient: dict):
    try:
        obj = Patient.objects.create(**patient)
        return obj
    except:
        raise ValidationError('Could not save')


def create_appointment(appointment: dict):
    try:
        hour = appointment.get('start_date').strftime("%H:%M:%S")
        start_date = appointment.get('start_date').strftime('%Y-%m-%d')
        appointment['start_date'] = start_date
        appointment['hour'] = hour
        Appointment.objects.create(**appointment)
    except IntegrityError as e:
        if 'UNIQUE constraint' in str(e.args):
            raise ValidationError(f'could not save date already exist')
        raise ValidationError('Some error')

def schedule_appointment(payload: PayloadDTO):
    payload = payload.dict()
    patient = payload.get('patient')
    appointment = payload.get('appointment')
    patient_id = create_patient(patient)
    appointment.update({'patient':patient_id})
    create_appointment(appointment)
