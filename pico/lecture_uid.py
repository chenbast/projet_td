from mfrc522 import MFRC522
from utime import sleep

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
            # Lecture optionnelle des données dans le bloc 8
            """stat, data = rc522.read(8)
            if stat == rc522.OK:
                text = ''.join(chr(i) for i in data if i != 0)
                print("Texte sur la carte :", text)"""
                

    sleep(2)

