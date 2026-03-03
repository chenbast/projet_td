import network
import requests
from time import sleep
from picozero import pico_temp_sensor, pico_led
import machine
import rp2
import sys
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
    print(f'Connected on {ip}')
    pico_led.on()
    return ip
        
ip = connect()
print ('Connected - press BOOTSEL to quit')
while True:
    if rp2.bootsel_button() == 1:
        pico_led.off()
        print('ByBye')
        sys.exit()
    response = requests.get("http://193.48.125.163/test_liaison_rs_pico.php?valeur=10") # Remplacer URL 193.48.125.163*/
    response_code = response.status_code
    response_content = response.content
    print('Response code: ', response_code)
    print('Response content:', response_content)
    sleep(2)
