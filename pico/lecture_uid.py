from mfrc522 import MFRC522
from utime import sleep
import requests
from time import sleep
import network
import requests
from picozero import pico_temp_sensor, pico_led
import machine
import rp2
import sys
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


def uidToString(uid):
    return ''.join("%02X" % i for i in uid)

# Initialisation du lecteur (SPI pins selon ta config)
rc522 = MFRC522(spi_id=0, sck=6, miso=4, mosi=7, cs=5, rst=3)

print("Placez une carte RFID pres du lecteur.")

rfid_data = ""  # variable pour stocker l'UID

while True:
    (stat, tag_type) = rc522.request(rc522.REQIDL)

    if stat == rc522.OK:
        (stat, uid) = rc522.SelectTagSN()

        if stat == rc522.OK:
            rfid_data = uidToString(uid)  # <-- stockage de l'UID
            print("Contenu de rfid_data :", rfid_data)
            break
            # Lecture optionnelle des données dans le bloc 8
            """stat, data = rc522.read(8)
            if stat == rc522.OK:
                text = ''.join(chr(i) for i in data if i != 0)
                print("Texte sur la carte :", text)"""
                
response = requests.get("http://193.48.125.177/etrs403/projet_td/sql/test_pico.php?test="+rfid_data) # Remplacer URL 193.48.125.177*/
response_code = response.status_code
response_content = response.content
print('Response code: ', response_code)
print('Response content:', response_content)
    

