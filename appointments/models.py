from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Patient(models.Model):
    first_name = models.TextField(null=False)
    last_name = models.TextField(null=False)
    age = models.IntegerField(null=False)
    phone_number = models.TextField(null=False)
    email = models.EmailField(null=False)

    def __str__(self) -> str:
        return f'{self.first_name}'


class Staff(models.Model):
    name = models.TextField(null=False)

    def __str__(self) -> str:
        return f'{self.name}'


class Appointment(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, null=True)
    start_date = models.DateField(unique=True)
    accepted = models.BooleanField(default=False)
    comments = models.TextField(null=True)
    doctor = models.TextField(null=True)
    hour = models.TimeField()


    def __str__(self) -> str:
        return f'Cita  Paciente: {self.patient.first_name} fecha {self.start_date}'