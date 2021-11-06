import hashlib
import re 

def generarHash(cadena):
    patron = r'0000[0-9a-zA-Z]+'
    nonce = 0
    
    while True:
        suma = cadena + bytes(nonce)
        id_hash =  hashlib.sha256(suma).hexdigest()
        nonce +=1
        if re.match(patron, id_hash):
            return id_hash
        