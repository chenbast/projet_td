from mfrc522 import MFRC522
from machine import Pin
from utime import sleep
import json
import network
import socket
import time
from picozero import pico_temp_sensor, pico_led
import machine
import rp2
import sys
import ubinascii
import requests

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


rc522 = MFRC522(spi_id=0, sck=6, miso=4, mosi=7, cs=5, rst=3)

led1 = Pin(13, Pin.OUT)  # led rouge pin
led2 = Pin(14, Pin.OUT)  # led jaune pin
led3 = Pin(15, Pin.OUT)  # led vert pin

led1.value(0)
led3.value(0)
led2.value(1)
def load_users():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except:
        return {}

users = load_users()

def uid_to_string(uid):
    return "".join("%02X" % b for b in uid)

def ask_pin():
    pin = ""
    while len(pin) < 4:
        digit = input("Chiffre {} : ".format(len(pin) + 1))
        if digit.isdigit() and len(digit) == 1:
            pin += digit
            print("*")
    return pin

print("Approchez une carte RFID...\n")

def add_user(uid):
    print("Nouveau badge")

    
    if uid in users:
        print("Badge déjà enregistré !")
        return

    name = input("Nom : ").strip()
    pin = ask_pin()

    
    users[uid] = {
        "name": name,
        "pin": pin
    }

    
    with open("users.json", "w") as f:
        json.dump(users, f)

    print("Badge enregistré")

    led2.value(0)
    led3.value(1)
    time.sleep(1)
    led3.value(0)
    led2.value(1)
    
    nom=""
    for c in name:
        if c==" ":
            nom+="_"
        else:
            nom+=c
    print(uid)
    print(pin)
    print(nom)
    response = requests.get(
    "http://193.48.125.177/etrs403/projet_td/web/communication/comm_pico.php?uid="+uid+"&nom="+nom+"&pin="+pin) # Remplacer URL 193.48.125.177*/
    response_code = response.status_code
    response_content = response.content
    print('Response code: ', response_code)
    print('Response content:', response_content)


last_uid = None
name=""
nom=""
pin_input=""
while True:
    stat, _ = rc522.request(rc522.REQIDL)

    if stat == rc522.OK:
        stat, uid = rc522.SelectTagSN()

        if stat == rc522.OK:
            uid_str = uid_to_string(uid)

            if uid_str == last_uid:
                sleep(0.5)
                continue

            last_uid = uid_str

            print("\nCarte détectée :", uid_str)

           
            if uid_str not in users:
                add_user(uid_str)
                print('Au revoir')
                break
            else:
                user = users[uid_str]

               
                if isinstance(user, dict):
                    name = user.get("name", "Utilisateur")
                    pin = user.get("pin", "")
                else:
                    name = user
                    pin = ""

                print("Utilisateur :", name)

                # PIN OBLIGATOIRE 
                if not pin:
                    print("Aucun PIN enregistré : accès refusé")
                    led1.value(1)  # allume la LED rouge
                    led2.value(0)  # éteinds la LED jaune
                    time.sleep(1)
                else:
                    attempts = 0
                    ok = False

                    while attempts < 3:
                        pin_input = ask_pin()

                        if pin_input == pin:
                            print("Accès autorisé")
                            ok = True
                            led3.value(1)  # allume la LED verte
                            led2.value(0)  # éteinds la LED jaune
                            time.sleep(1)
                            break
                        else:
                            attempts += 1
                            print("PIN incorrect ({}/3)".format(attempts))

                    if not ok:
                        print("Accès refusé")
                        led1.value(1)  # allume la LED rouge
                        led2.value(0)  # éteinds la LED jaune
                        time.sleep(1)

            print("Retirez la carte...")
            nom=""
            for c in name:
                if c==" ":
                    nom+="_"
                else:
                    nom+=c
            print(uid_str)
            print(pin_input)
            print(nom)
            response = requests.get(
            "http://193.48.125.177/etrs403/projet_td/web/communication/comm_pico.php?uid="+uid_str+"&nom="+nom+"&pin="+pin_input) # Remplacer URL 193.48.125.177*/
            response_code = response.status_code
            response_content = response.content
            print('Response code: ', response_code)
            print('Response content:', response_content)
            break

    sleep(0.2)
