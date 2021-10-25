from datetime import date, datetime
from parser import ParserError

import maya
from ninja import Schema
from pydantic import validator


class PersonaDTO(Schema):
    first_name: str
    last_name: str
    age: int
    phone_number: str
    

class AppointmentDTO(Schema):
    start_date: datetime

    @validator('start_date')
    def parse_date_strings_(cls, v):
        try:
            dt = maya.parse(v, day_first=True)
            return dt.datetime()
        except ParserError:
            raise ValueError("error parse")

class PayloadDTO(Schema):
    patient: PersonaDTO
    appointment: AppointmentDTO 


class Message(Schema):
    message: str