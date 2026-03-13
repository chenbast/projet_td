'''
Lecture du numéro (UID) d'un tag RFID.
'''
from mfrc522 import MFRC522 
from utime import sleep

def uidToString(uid):#conversion en hexadécimal
    mystring = ""
    for i in uid:
        mystring = "%02X" % i + mystring
    return mystring
                  
rc522 = MFRC522(spi_id=0,sck=6,miso=4,mosi=7,cs=5,rst=3)

print("")
print("Placez une carte RFID pres du lecteur.")
print("")

while True:

    (stat, tag_type) = rc522.request(rc522.REQIDL)

    if stat == rc522.OK: #detection de carte/badge
        (stat, uid) = rc522.SelectTagSN()
        
    if stat == rc522.OK:
        print("Carte detectee %s" % uidToString(uid))
        sleep(1) # delai pour éviter les lectures multiples
        
