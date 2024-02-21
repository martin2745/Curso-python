#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# dates

from datetime import datetime
from datetime import date
from datetime import time

print("\n---------datetime---------\n")

now = datetime.now()

def info_fecha(date):
    print("Año:", date.year)
    print("Mes:", date.month)
    print("Día:", date.day)
    print("Hora", date.hour)
    print("Minuto:", date.minute)
    print("Segundo:", date.second)
    # Valor numérico en segundos desde la medianoche (00:00:00) del 01/01/1970
    print("Timestamp:", date.timestamp())

info_fecha(now)

anho_actual = datetime(2023, 1, 1)
info_fecha(anho_actual)

print("Fecha y hora actuales:", now)
print("Fecha y hora actuales:", anho_actual)

# Time
print("\n-----------time-----------\n")
tiempo_actual = time(21, 6, 0)
print("Horas:", tiempo_actual.hour)
print("Minutos:", tiempo_actual.minute)
print("Segundos", tiempo_actual.second)

# Date
print("\n-----------date-----------\n")

fecha_actual = date.today()

print("Año:", fecha_actual.year)
print("Mes:", fecha_actual.month)
print("Día:", fecha_actual.day)

fecha_actual = date(2023, 11, 5)