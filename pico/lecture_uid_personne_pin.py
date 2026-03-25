from mfrc522 import MFRC522
from machine import Pin
from utime import sleep
import json
import time

# --- Initialisation RFID et LED ---
rc522 = MFRC522(spi_id=0, sck=6, miso=4, mosi=7, cs=5, rst=3)
led1 = Pin(13, Pin.OUT)  # rouge
led2 = Pin(14, Pin.OUT)  # jaune
led3 = Pin(15, Pin.OUT)  # vert

led1.value(0)
led2.value(1)
led3.value(0)

# --- Chargement des utilisateurs ---
def load_users():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except:
        return {}

users = load_users()

# --- Fonctions utilitaires ---
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

# --- Conversion ISO 8601 -> timestamp ---
def iso_to_timestamp(iso_str):
    # "YYYY-MM-DDTHH:MM:SS"
    try:
        y = int(iso_str[0:4])
        m = int(iso_str[5:7])
        d = int(iso_str[8:10])
        h = int(iso_str[11:13])
        mi = int(iso_str[14:16])
        s = int(iso_str[17:19])
        return int(time.mktime((y, m, d, h, mi, s, 0, 0)))
    except:
        return None

# --- Ajouter un utilisateur ---
def add_user(uid):
    print("Nouveau badge")
    
    if uid in users:
        print("Badge déjà enregistré !")
        return

    name = input("Nom : ").strip()
    pin = ask_pin()
    
    # Date d'expiration optionnelle
    valid_input = input("Date d'expiration (YYYY-MM-DDTHH:MM:SS) ou laisser vide : ").strip()
    if valid_input:
        valid_until = valid_input  # stocker au format ISO
    else:
        valid_until = None
    
    users[uid] = {
        "name": name,
        "pin": pin,
        "valid_until": valid_until
    }
    
    with open("users.json", "w") as f:
        json.dump(users, f)

    print("Badge enregistré")
    led2.value(0)
    led3.value(1)
    time.sleep(1)
    led3.value(0)
    led2.value(1)

# --- Boucle principale ---
last_uid = None
print("Approchez une carte RFID...\n")

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
            else:
                user = users[uid_str]

                # Récupération nom, PIN et expiration
                name = user.get("name", "Utilisateur")
                pin = user.get("pin", "")
                valid_until = user.get("valid_until", None)

                print("Utilisateur :", name)

                # Vérification expiration
                valid_ts = iso_to_timestamp(valid_until) if valid_until else None
                if valid_ts is not None and time.time() > valid_ts:
                    print("Badge expiré ! Accès refusé")
                    led1.value(1)
                    led2.value(0)
                    time.sleep(1)
                    last_uid = None
                    continue

                # Vérification PIN
                if not pin:
                    print("Aucun PIN enregistré : accès refusé")
                    led1.value(1)
                    led2.value(0)
                    time.sleep(1)
                else:
                    attempts = 0
                    ok = False
                    while attempts < 3:
                        pin_input = ask_pin()
                        if pin_input == pin:
                            print("Accès autorisé")
                            ok = True
                            led3.value(1)
                            led2.value(0)
                            time.sleep(1)
                            break
                        else:
                            attempts += 1
                            print("PIN incorrect ({}/3)".format(attempts))
                    if not ok:
                        print("Accès refusé")
                        led1.value(1)
                        led2.value(0)
                        time.sleep(1)

            print("Retirez la carte...")

            # Attente que la carte soit retirée
            while True:
                stat_check, _ = rc522.request(rc522.REQIDL)
                if stat_check != rc522.OK:
                    break
                sleep(0.2)
            last_uid = None

    sleep(0.2)
