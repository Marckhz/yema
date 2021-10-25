from datetime import date
from typing import List

import maya
from pydantic import BaseModel, Field, validator


class EmailDTO(BaseModel):
    recipient_list: List
    message: str
    subject: str = "Confirmacion de Cita"
    from_email: str = "yema.test.challenge@gmail.com"
