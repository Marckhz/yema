from typing import Dict, List

from django.db import router
from django.http import response
from ninja import NinjaAPI, Router

from appointments.models import Appointment, Patient

from .dto import AppointmentDTO, Message, PayloadDTO
from .repository import schedule_appointment as create_appointment

api = Router()

@api.get('/', response=List[AppointmentDTO])
def schudeled_appointment(request):
    # show intervals of one hour?
    qs = Appointment.objects.filter(Appointment.accepted == True)
    return qs


@api.post('/schedule', response={201:Message})
def schedule_appointment(request,payload:PayloadDTO):
    try:
        create_appointment(payload)
        return 201, {'message':'Sucessfully'}
    except Exception as e:
        return 500, {'message': f'Something went wrong {e}'}


@api.get('/hello', response=Dict)
def hello_world(request):
    return {"data":"Hello World"}
