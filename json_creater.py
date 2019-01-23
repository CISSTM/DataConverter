#Imported libaries
import json
import logging
from os import path
basepath = path.dirname(__file__)


#Your variable that you received from the sattelite.
x = 1103101222
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


def return_data():
    if t is not None:
        save_data("temperature", t)
    elif p is not None:
        save_data("pressure", p)
    elif a is not None:
        save_data("altitude", a)
    else:
        return "Wrong data error"

def save_data(topic, data):
    to_write = {
        topic: data
    }
    with open(basepath + 'joepie.json', 'w+') as f:
        f.write(json.dumps(to_write))

return_data()
