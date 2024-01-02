#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Martín Gil Blanco"

# dates

from datetime import datetime
from datetime import date
from datetime import time

now = datetime.now()

def info_fecha(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

info_fecha(now)

anho_actual = datetime(2023, 1, 1)

info_fecha(anho_actual)


# Time

tiempo_actual = time(21, 6, 0)

print(tiempo_actual.hour)
print(tiempo_actual.minute)
print(tiempo_actual.second)


# Date

fecha_actual = date.today()

print(fecha_actual.year)
print(fecha_actual.month)
print(fecha_actual.day)

fecha_actual = date(2023, 11, 5)

# Operaciones con fechas

diff = anho_actual - now
print(diff)

diff = anho_actual.date() - fecha_actual
print(diff)