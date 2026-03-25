from mfrc522 import MFRC522
from machine import Pin
from utime import sleep
import json
import time

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

last_uid = None


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
                print("Badge inconnu")

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

            while True:
                stat_check, _ = rc522.request(rc522.REQIDL)
                if stat_check != rc522.OK:
                    break
                sleep(0.2)

            last_uid = None

    sleep(0.2)