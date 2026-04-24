# Import des bibliothèques nécessaires
from mfrc522 import MFRC522          # Module pour le lecteur RFID RC522
from machine import Pin              # Gestion des broches GPIO
from utime import sleep              # Pause (temps)
import json                          # Lecture/écriture de fichiers JSON
import network                       # Gestion du WiFi
import socket
import time
from picozero import pico_temp_sensor, pico_led  # LED + capteur Pico
import machine
import rp2                           # Accès bouton BOOTSEL
import sys
import ubinascii                     # Conversion binaire -> texte
import requests                      # Requêtes HTTP

# Identifiants WiFi
ssid = 'wifirpi'
password = '88E4VB1YQBI15TM4UCK9KP1LWQ'

def connect():
    """
    Fonction de connexion au réseau WiFi.
    - Active l'interface réseau du Pico
    - Tente de se connecter avec SSID et mot de passe
    - Fait clignoter la LED pendant l'attente
    - Permet de quitter avec le bouton BOOTSEL
    - Retourne l'adresse IP une fois connecté
    """
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    while wlan.isconnected() == False:
        # Permet de quitter si on appuie sur BOOTSEL
        if rp2.bootsel_button() == 1:
            sys.exit()

        print('Waiting for connection...')
        pico_led.on()
        sleep(0.5)
        pico_led.off()
        sleep(0.5)

    # Récupération IP et MAC une fois connecté
    ip = wlan.ifconfig()[0]
    mac = ubinascii.hexlify(wlan.config('mac'),':').decode()
    print(f'Connected on {ip} / {mac}')
    pico_led.on()
    return ip
        
ip = connect()

print ('Connected - press BOOTSEL to quit')


# Initialisation du lecteur RFID RC522 avec les broches SPI
rc522 = MFRC522(spi_id=0, sck=6, miso=4, mosi=7, cs=5, rst=3)

# Configuration des LEDs (sortie GPIO)
led1 = Pin(13, Pin.OUT)  # led rouge
led2 = Pin(14, Pin.OUT)  # led jaune
led3 = Pin(15, Pin.OUT)  # led vert

# Etat initial des LEDs
led1.value(0)
led3.value(0)
led2.value(1)

def load_users():
    """
    Charge les utilisateurs depuis le fichier 'users.json'.
    - Si le fichier existe : retourne le dictionnaire JSON
    - Sinon : retourne un dictionnaire vide
    """
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except:
        return {}

users = load_users()

def uid_to_string(uid):
    """
    Convertit un UID RFID (liste d'octets) en chaîne hexadécimale.
    """
    return "".join("%02X" % b for b in uid)

def ask_pin():
    """
    Demande à l'utilisateur de saisir un code PIN à 4 chiffres.
    - Vérifie que chaque entrée est bien un chiffre
    - Masque l'affichage avec '*'
    - Retourne le PIN complet
    """
    pin = ""
    while len(pin) < 4:
        digit = input("Chiffre {} : ".format(len(pin) + 1))
        if digit.isdigit() and len(digit) == 1:
            pin += digit
            print("*")
    return pin

print("Approchez une carte RFID...\n")

def iso_to_timestamp(date_str):
    """
    Convertit une date au format texte (JJ/MM/AAAA HH:MM)
    en timestamp Unix
    - Retourne None si le format est invalide
    """
    try:
        d = int(date_str[0:2])
        m = int(date_str[3:5])
        y = int(date_str[6:10])
        h = int(date_str[11:13])
        mi = int(date_str[14:16])
        return int(time.mktime((y, m, d, h, mi, 0, 0, 0)))
    except:
        return None

ADMIN_UID = "B3F28D1A" # Carte blanche : admin

def add_user(uid):
    """
    Ajoute un nouvel utilisateur RFID.
    1. Vérifie un badge ADMIN
    2. Demande nom + PIN
    3. Option d'ajout d'une date d'expiration
    4. Sauvegarde dans users.json
    5. Envoie les données au serveur web
    """

    print("Pour enregistrer ce nouveau badge, badgez d'abord avec le badge ADMIN...")
    led1.value(0)
    led2.value(1)
    led3.value(0)

    admin_verified = False

    # Boucle jusqu'à validation du badge admin
    while not admin_verified:
        stat, _ = rc522.request(rc522.REQIDL)
        if stat == rc522.OK:
            stat, admin_uid_bytes = rc522.SelectTagSN()
            if stat == rc522.OK:
                admin_uid_str = uid_to_string(admin_uid_bytes)

                # Vérification UID admin
                if admin_uid_str == ADMIN_UID:
                    admin_verified = True
                    print("Admin reconnu !")
                    led2.value(0)
                    led3.value(1)
                    sleep(3)
                    led3.value(0)
                    led2.value(1)
                else:
                    print("Badge non autorisé pour ajout !")
                    led1.value(1)
                    sleep(2)
                    led1.value(0)
        sleep(0.2)

    print("Nouveau badge")
    led1.value(0)
    led2.value(1)
    led3.value(0)

    # Vérifie si déjà existant
    if uid in users:
        print("Badge déjà enregistré !")
        return

    # Saisie utilisateur
    name = input("Prénom et nom : ").strip()
    pin = ask_pin()

    # Gestion expiration
    rep = input("Ajouter une date d'expiration ? (o/n) : ").strip().lower()

    if rep == "o":
        while True:
            valid_input = input("Expiration (JJ/MM/AAAA HH:MM) : ").strip()
            if iso_to_timestamp(valid_input):
                valid_until = valid_input
                break
            else:
                print("Format invalide")
    else:
        valid_until = None

    # Ajout dans dictionnaire
    users[uid] = {
        "name": name,
        "pin": pin,
        "valid_until": valid_until
    }

    # Sauvegarde JSON
    with open("users.json", "w") as f:
        json.dump(users, f)

    print("Badge enregistré")

 
    led2.value(0)
    led3.value(1)
    time.sleep(3)
    led3.value(0)
    led2.value(1)
    
    # Préparation nom pour URL (remplace espaces)
    nom=""
    for c in name:
        if c==" ":
            nom+="_"
        else:
            nom+=c

    # Debug
    print(uid)
    print(pin)
    print(nom)

    # Envoi HTTP vers serveur
    response = requests.get(
    "http://193.48.125.177/etrs403/projet_td/web/communication/comm_pico.php?uid="+uid+"&nom="+nom+"&pin="+pin)

    response_code = response.status_code
    response_content = response.content

    print('Response code: ', response_code)
    print('Response content:', response_content)

print("Approchez une carte RFID...\n")

led2.value(1)
last_uid = None
name=""
nom=""
pin_input=""

# Boucle principale du programme
while True:
    stat, _ = rc522.request(rc522.REQIDL)

    # Si une carte est détectée
    if stat == rc522.OK:
        stat, uid = rc522.SelectTagSN()

        if stat == rc522.OK:
            uid_str = uid_to_string(uid)

            # Evite double lecture
            if uid_str == last_uid:
                sleep(0.5)
                continue

            last_uid = uid_str
            print("\nCarte détectée :", uid_str)

            # Si utilisateur connu
            if uid_str in users:

                user = users[uid_str]
                name = user.get("name", "Utilisateur")
                pin = user.get("pin", "")
                valid_until = user.get("valid_until")

                print("Utilisateur :", name)

                # Vérification expiration
                valid_ts = iso_to_timestamp(valid_until) if valid_until else None

                if valid_ts and time.time() > valid_ts:
                    print("Badge expiré ! Suppression...")

                    led1.value(1)
                    led2.value(0)
                    time.sleep(1)

                    # Suppression utilisateur
                    del users[uid_str]

                    with open("users.json", "w") as f:
                        json.dump(users, f)

                    print("Badge supprimé du système")

                    # Option de réenregistrement
                    rep = input("Réenregistrer ce badge ? (o/n) : ")
                    if rep.lower() == "o":
                        add_user(uid_str)

                    led1.value(0)
                    led2.value(1)
                    time.sleep(1)
                    last_uid = None
                    continue

                # Vérification PIN
                if not pin:
                    print("Pas de PIN")
                    led1.value(1)
                    led2.value(0)
                    time.sleep(1)

                else:
                    ok = False
                    for i in range(3):
                        pin_input = ask_pin()
                        if pin_input == pin:
                            print("Accès autorisé")
                            led3.value(1)
                            led2.value(0)
                            time.sleep(3)
                            ok = True
                            break
                        else:
                            print(f"Erreur ({i+1}/3)")

                    if not ok:
                        print("Accès refusé")
                        led1.value(1)
                        led2.value(0)
                        time.sleep(1)

            else:
                # Badge inconnu -> ajout utilisateur
                print("Badge inconnu")
                add_user(uid_str)

            print("Retirez la carte...")

            led1.value(0)
            led2.value(1)
            led3.value(0)

            last_uid = None

            # Préparation nom pour URL (remplace espaces)
            nom=""
            for c in name:
                if c==" ":
                    nom+="_"
                else:
                    nom+=c

            # Debug
            print(uid_str)
            print(pin_input)
            print(nom)

            # Envoi serveur
            response = requests.get(
            "http://193.48.125.177/etrs403/projet_td/web/communication/comm_pico.php?uid="+uid_str+"&nom="+nom+"&pin="+pin_input)

            response_code = response.status_code
            response_content = response.content

            print('Response code: ', response_code)
            print('Response content:', response_content)

            # Attente retrait carte
            while True:
                stat, _ = rc522.request(rc522.REQIDL)
                if stat != rc522.OK:
                    break
                sleep(0.1)

    sleep(0.2)
