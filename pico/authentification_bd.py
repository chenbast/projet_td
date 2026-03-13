from mfrc522 import MFRC522
from machine import Pin
from utime import sleep
import json
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

# -------- RFID --------
rc522 = MFRC522(spi_id=0, sck=6, miso=4, mosi=7, cs=5, rst=3)

# -------- BASE DE DONNÉES --------
def load_users():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except:
        return {}

def save_users(users):
    with open("users.json", "w") as f:
        json.dump(users, f)

users = load_users()

# -------- Conversion UID en hex --------
def uid_to_string(uid):
    return "".join("%02X" % b for b in uid)

# -------- Lecture du PIN via terminal --------
def ask_pin():
    pin = ""
    while len(pin) < 4:
        print("Entrez chiffre {} : ".format(len(pin)+1), end="")
        digit = input()
        if digit.isdigit() and len(digit) == 1:
            pin += digit
            print("*")
        else:
            print("Veuillez entrer un seul chiffre.")
    return pin

# -------- PROGRAMME PRINCIPAL --------

print("Approchez une carte RFID du lecteur.\n")

last_uid = None
autorisation="false"
while True:
    stat, _ = rc522.request(rc522.REQIDL)
    if stat == rc522.OK:
        stat, uid = rc522.SelectTagSN()
        if stat == rc522.OK:
            uid_str = uid_to_string(uid)

            # éviter double lecture
            if uid_str == last_uid:
                sleep(0.5)
                continue
            last_uid = uid_str

            print("Carte détectée :", uid_str)

            if uid_str not in users:
                print("Carte non enregistrée !")
            else:
                attempts = 0
                while attempts < 3:
                    pin_input = ask_pin()
                    if pin_input == users[uid_str]:
                        print("Accès autorisé !")
                        autorisation="true"
                        break
                    else:
                        attempts += 1
                        print("PIN incorrect. Tentative {}/3".format(attempts))
                else:
                    print("Accès refusé après 3 tentatives !")

    # attendre que la carte soit retirée

    sleep(0.2)

print('ici')
rfid_data=uid_str
response = requests.get("http://193.48.125.177/etrs403/projet_td/sql/test_pico.php?test="+rfid_data+"&autorisation="+autorisation) # Remplacer URL 193.48.125.177*/
response_code = response.status_code
response_content = response.content
print('Response code: ', response_code)
print('Response content:', response_content)
    


