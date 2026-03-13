from mfrc522 import MFRC522
from machine import Pin, SPI
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

# -------- Saisie PIN via terminal --------
def read_pin():
    pin = ""
    print("Entrez un code PIN à 4 chiffres :")
    while len(pin) < 4:
        print("Chiffre {} : ".format(len(pin)+1), end="")
        digit = input()  # juste input() sans argument
        if digit.isdigit() and len(digit) == 1:
            pin += digit
            print("*")  # affiche * pour le chiffre saisi
        else:
            print("Veuillez entrer un seul chiffre.")
    print("PIN saisi :", pin)
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

            if uid_str in users:
                print("Carte déjà enregistrée avec le PIN :", users[uid_str])
            else:
                pin = read_pin()
                users[uid_str] = pin
                save_users(users)
                print("Carte enregistrée !")

            # attendre que la carte soit retirée avant d'accepter une autre
            print("Retirez la carte")
            while True:
                stat_check, _ = rc522.request(rc522.REQIDL)
                if stat_check != rc522.OK:
                    break
                sleep(0.2)

            last_uid = None

    sleep(0.2)
