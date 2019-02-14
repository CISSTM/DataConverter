import serial
import json_creater
import csv_creater
ser  = serial.Serial('COM4')

while True:
    try:
        message = int.from_bytes(ser.readline(), 'big')
        if message:
            json_creater.total_function(message)
    except Exception:
        pass
ser.close()
