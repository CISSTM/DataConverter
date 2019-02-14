#Imported libaries
import json
import logging
from os import path
basepath = path.dirname(__file__)
write_path =  basepath + 'export.json'

def total_function(x):
    #Your variable that you received from the sattelite.
    s = 0

    #Changes the variable into a string (and back). This way you can read a specific part of your number.
    y = str(x)
    z = int(y[2:4])

    #Checks the type of data (t = temperature; p = pressure; a = alltitude)
    if z == 1:
        t = int(y[4:8])
    elif z != 1:
        t = None

    if z == 2:
        p = int(y[4:8])
    elif z != 2:
        p = None

    if z == 3:
        a = int(y[4:8])
    elif z != 3:
        a = None

    #Check type to save
    if t is not None:
        save_data("temperature", t)
    elif p is not None:
        save_data("pressure", p)
    elif a is not None:
        save_data("altitude", a)
    else:
        return "Wrong data error"

def save_data(topic, data):
    current_data = {
        topic: data
    }
    write_array = []
    with open(write_path, 'r') as curr:
        write_array = json.load(curr)

    with open(write_path, 'w+') as f:
        write_array.append(current_data)
        print (write_array)
        f.write(json.dumps(write_array))


