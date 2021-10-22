from django.db import router
from django.http import response
from ninja import Router, NinjaAPI
from typing import Dict, List
from appointments.models import Appointment
from appointments.models import Patient
from .dto import AppointmentDTO, PayloadDTO
from .repository import schedule_appointment as create_appointment
api = Router()

@api.get('/', response=List[AppointmentDTO])
def schudeled_appointment(request):
    # show intervals of one hour?
    qs = Appointment.objects.filter(Appointment.accepted == True)
    return qs


@api.post('/schedule')
def schedule_appointment(request, payload: PayloadDTO):
    try:
        create_appointment(payload)
        return {'msg':'Sucessfully'}
    except Exception as e:
        return {'msg': f'Something went wrong {e}'}


@api.get('/hello', response=Dict)
def hello_world(request):
    return {"data":"Hello World"}
