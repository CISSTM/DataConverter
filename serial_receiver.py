import serial
from json_creater import total_function
ser  = serial.Serial('COM4')
while True:
    print (int.from_bytes(ser.readline()))

ser.close()