import hashlib

def generarHash(cadena):
    m = hashlib.sha256()
    m.update(cadena)
    return (m.hexdigest())
        