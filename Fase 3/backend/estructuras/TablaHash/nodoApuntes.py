class NodoApuntes:
    def __init__(self, id, titulo, contenido):
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.siguiente = None
        self.anterior = None
