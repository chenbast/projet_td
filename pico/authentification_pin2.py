from mfrc522 import MFRC522
from machine import Pin
from utime import sleep
import json

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
                        break
                    else:
                        attempts += 1
                        print("PIN incorrect. Tentative {}/3".format(attempts))
                else:
                    print("Accès refusé après 3 tentatives !")

            # attendre que la carte soit retirée
            print("Retirez la carte...")
            while True:
                stat_check, _ = rc522.request(rc522.REQIDL)
                if stat_check != rc522.OK:
                    break
                sleep(0.2)

            last_uid = None

    sleep(0.2)

    

