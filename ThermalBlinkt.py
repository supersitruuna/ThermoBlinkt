# Adapted from blinkt_thremo.py
from time import sleep
from sys import exit
import requests
import blinkt

API_KEY =''
CITY_ID=''
url = 'http://api.openweathermap.org/data/2.5/weather'
temp = 0

def update_weather():
    global temp
    payload = {
        'id':CITY_ID,
        'units':'metric',
        'appid': API_KEY
        }
    try:
        r = requests.get(url=url, params=payload)
        temp = r.json().get('main').get('temp')
        print('Temperature = ' + str(temp) + ' C')

    except requests.exceptions.ConnectionError:
        print('Connection Error')


def show_graph(v,r,g,b,):
    v *= blinkt.NUM_PIXELS
    for x in range (blinkt.NUM_PIXELS):
        if v < 0:
            r,g,b = 0,0,0

        else:
            r,g,b = [int(min(v, 1.0) * c) for c in [r,g,b]]
        blinkt.set_pixel(x,r,g,b)
        v -= 1
    blinkt.show()

def draw_thermo(temp):
    v = abs(temp)
    v /= 40
    v += (1/8)
    r,g,b = set_colours(temp)
    show_graph(v, r,g,b)

blinkt.set_brightness(0.035)

def set_colours(temp):
    if temp >= 35:
        r,g,b = 139, 0, 0
    elif temp >= 30:
        r,g,b = 142,10,0
    elif temp >= 25:
        r,g,b = 250,54, 0
    elif temp >= 20:
        r,g,b = 255,76, 0
    elif temp >= 15:
        r,g,b = 171,142,5
    elif temp >= 10:
        r,g,b = 49, 111, 15
    elif temp >= 5:
        r,g,b = 9,66,60
    elif temp >= 0:
        r,g,b = 75,75,75
    elif temp >= -5:
        r,g,b = 37, 105, 248
    elif temp >= -10:
        r,g,b = 100, 48, 253
    elif temp >= -15:
        r,g,b = 255, 0, 255
    else:
        r,g,b =  56, 101, 224

    return r,g,b


while 1:
    update_weather()
    draw_thermo(temp)
    sleep(120)



