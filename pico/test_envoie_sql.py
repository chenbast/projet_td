import urequests
import network
import socket
from time import sleep
from picozero import pico_temp_sensor, pico_led
import machine
import rp2
import sys
import ubinascii

#Wifi de la borne D-link DAP-1360 stockée dans la salle A214
ssid = 'wifirpi'
password = '88E4VB1YQBI15TM4UCK9KP1LWQ'

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        if rp2.bootsel_button() == 1:
            sys.exit()
        print('Waiting for connection...')
        pico_led.on()
        sleep(0.5)
        pico_led.off()
        sleep(0.5)
    ip = wlan.ifconfig()[0]
    mac = ubinascii.hexlify(wlan.config('mac'),':').decode()
    print(f'Connected on {ip} / {mac}')
    pico_led.on()
    return ip
        
ip = connect()

print ('Connected - press BOOTSEL to quit')
while True:
    if rp2.bootsel_button() == 1:
        pico_led.off()
        print('ByBye')
        sys.exit()
    sleep(0.5)
  

number = '10'  # must be text
r = urequests.get(url = 'http://193.48.125.177/etrs403/projet_td/sql/test_pico.php?nombre='+number)